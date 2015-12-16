from google.appengine.ext import db
import json
### Utility functions you may want to use
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def parse(dir_name):
	with open(dir_name) as data_file:    
		return (json.load(data_file)["data"])

class Video(db.Model):
	"""Models a video object"""
	vid_id = db.StringProperty()
	db_id = db.StringProperty()