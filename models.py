from google.appengine.ext import db

#Defines the video object
class Video(db.Model):
	"""Models a video object"""
	evidence_id = db.StringProperty()
	external_id = db.StringProperty()
	url = db.StringProperty()
	lat = db.FloatProperty()
	longit = db.FloatProperty()
	desc = db.StringProperty()
	date = db.StringProperty()