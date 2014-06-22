# -*- coding: utf-8 -*-
import json
import urllib2
import sys

def count(location,road,year):
	count = 0
	sum = 0
	for i in j:
		if i[u'鄉鎮市區'] == location:
			if road in i[u'土地區段位置或建物區門牌']:
				if year in str(i[u'交易年月']):
					#print i[u'土地區段位置或建物區門牌'] 
					#print i[u'總價元']
					#print i[u'交易年月']
					sum = sum + i[u'總價元']
					count = count + 1
	sum = sum / count	
	print sum		    
if __name__ == '__main__':
	inpu = sys.argv
	url = inpu[1]
	data = urllib2.urlopen(url) #get url
	j = json.load(data)
	unicode_location = inpu[2].decode("utf8") #get location
	unicode_roads = inpu[3].decode("utf8") #get road
	unicode_year = inpu[4] #get year
	count(unicode_location,unicode_roads,unicode_year)
