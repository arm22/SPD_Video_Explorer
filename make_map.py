import sys
sys.path.append("folium/")
import folium
def makeMap():
	map_osm = folium.Map(location=[45.5236, -122.6750])
	map_osm.create_map(path='search.html')