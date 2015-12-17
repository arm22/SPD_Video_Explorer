import folium
from bs4 import BeautifulSoup
from google.appengine.ext import db
import models

def makeMap():
	map1 = folium.Map(location=[47.6236, -122.2750], tiles='Stamen Toner', width=500, height = 300)
	q = models.Video.all()
	for item in q:
		map1.simple_marker([item.lat, item.longit], popup='Date:'+str(item.date)+'<br>Desc:'+str(item.desc)+'<br><a target=_blank href='+item.url+'/>Police Footage</a><br>Case #:'+item.external_id)
	html = map1.create_map()
	soup = BeautifulSoup(html, 'html.parser')
	insert_html = {}
	insert_html["head"] = soup.head.contents
	insert_html["body"] = soup.body.contents
	return insert_html