from google.appengine.ext import db
import json
from datetime import datetime
import models

def putAll():
	with open('data.json') as data_file:    
		data = json.load(data_file)['data']
	for item in data:
		v = models.Video()
		v.evidence_id = item['evidence_id']
		v.url = item['url']
		v.lat = item['lat']
		v.longit = item['longit']
		v.desc = item['desc']
		v.date = item['date']
		v.external_id = item['external_id']
		v.put()