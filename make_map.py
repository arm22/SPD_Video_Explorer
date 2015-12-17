import folium
from bs4 import BeautifulSoup
from google.appengine.ext import db
import models

#makes a map, returns the needed html
def makeMap():
	map1 = folium.Map(location=[47.6236, -122.3150], tiles='Stamen Toner', height = 400, zoom_start=12)
	q = models.Video.all()
	#build popups for each item
	for item in q:
		map1.circle_marker([item.lat, item.longit], radius=40, line_color='#67809F', fill_color='#34495E', fill_opacity=0.9, popup='<b>Date:</b>'+str(item.date)+'<br><b>Desc:</b>'+str(item.desc)+'<br><a target=_blank href='+item.url+'/>Police Footage</a><br><b>Case #:</b>'+item.external_id)
	html = map1.create_map()
	#build a ds with the head and body returned form folium
	soup = BeautifulSoup(html, 'html.parser')
	head = soup.head.contents
	soup.style.decompose()
	insert_html = {}
	insert_html["head"] = head
	insert_html["body"] = soup.body.contents
	return insert_html