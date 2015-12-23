from google.appengine.ext import db
import models
import json

def toJson():
	collection = []
	objects = models.Video.all()
	for item in objects:
		raw = {}
		raw['external_id'] = item.external_id
		raw['evidence_id'] = item.evidence_id
		raw['url'] = item.url
		raw['lat'] = item.lat
		raw['longit'] = item.longit
		raw['desc'] = item.desc
		raw['date'] = str(item.date)
		collection.append(raw)
	print (json.dumps(collection))