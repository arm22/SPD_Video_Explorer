from google.appengine.ext import db

#Defines the video object
class Video(db.Model):
	"""Models a video object"""
	evidence_id = db.StringProperty()
	external_id = db.StringProperty()
	url = db.StringProperty()