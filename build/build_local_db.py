from google.appengine.ext import db
import json, urllib
from datetime import datetime
import models
import keys

### Utility function you may want to use
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

#Reads and loads a file into json
def parseFile(dir_name):
	with open(dir_name) as data_file:    
		return (json.load(data_file)["data"])

#Makes URL requests and handles errors
def safeGet(url):
    try:
        return urllib.urlopen(url)
    except urllib.HTTPError, e:
        print "The server couldn't fulfill the request." 
        print "Error code: ", e.code
    except urllib.URLError, e:
        print "We failed to reach a server"
        print "Reason: ", e.reason
    return None

#Makes request to the Youtube search API
#https://www.googleapis.com/youtube/v3/search?part=snippet&q=F5FCE46D-C622-4741-AC8C&key={YOUR_API_KEY}
def youtubRequest(baseurl = 'https://www.googleapis.com/youtube/v3/search', api_key = keys.youtube, params={} ):
	params['part'] = "snippet"
	params['key'] = api_key
	url = baseurl + "?" + urllib.urlencode(params)
	return safeGet(url)

#Checks the conditions for a model and adds it to the datastore
def makeObject(vid_id, ext_id, latitude, longitude, description, date):
	vals = {}
	vals['q'] = vid_id
	data = json.load(youtubRequest(params=vals))
	if ((data["pageInfo"]["totalResults"] >= 1) and (data is not None)):
		#https://www.youtube.com/watch?v=TSBqJPLjNUQ
		v = models.Video()
		v.evidence_id = vid_id
		v.external_id = ext_id
		v.url = "https://www.youtube.com/watch?v=" + data["items"][0]["id"]["videoId"]
		v.lat = latitude
		v.longit = longitude
		v.desc = description
		v.date = date
		v.put()

def build():
	video_data = parseFile("data/video-data.json")
	incident_data = parseFile("data/incident-response.json")
	call_data = parseFile("data/911-response.json")
	for item in video_data:
		found = False
		vid = item[8]
		ext = item[9]
		if ext is not None:
			ext = ext.replace("-", "").replace(" ","")
		for rec in call_data:
			if rec[10] == ext:
				found = True
				coord = rec[22]
				lat = float(coord[1].encode('utf-8'))
				longit = float(coord[2].encode('utf-8'))
				desc = rec[12]
				dated = rec[26].encode('utf-8')
				dated = datetime.strptime(dated, '%Y-%m-%dT%H:%M:%S').date()
				makeObject(vid, ext, lat, longit, desc, dated)
				break
		if (found is False):
			for x in incident_data:
				if x[9] == ext:
					found = True
					coord = x[24]
					lat = float(coord[1].encode('utf-8'))
					longit = float(coord[2].encode('utf-8'))
					desc = x[14]
					dated = x[15].encode('utf-8')
					dated = datetime.strptime(dated, '%Y-%m-%dT%H:%M:%S').date()
					makeObject(vid, ext, lat, longit, desc, dated)
					break