import json
import sys 
import urllib.request
from bs4 import BeautifulSoup
import os
from urllib.parse import quote
import collections


with open("C:/Users/sub/Documents/translation/111.json") as document_link : 
	document = json.load(document_link)	

print(document)

def get_text(URL, output_file):
	source_code_from_url = urllib.request.urlopen(URL)
	soup = BeautifulSoup(source_code_from_url, 'lxml' , from_encoding ='utf-8')
	content_of_article = soup.select('div.dlist_txt')
	for item in content_of_article:
		string_item = str(item.find_all(text==True))
		output_file.write(string_item)

for i in range(1,10):
	for j in range(0,10):
		get_text("https:" + str(document[i][j]), "C:/Users/sub/Documents/translation/222.json")
#		req = requests.get('document[str(i)][str(j)]')
#		soup = BeautifulSoup(req.content, 'html.parser')
#		links = soup.select('#detail_list > div > div.dlist_txt > p')


#		print(links.text)


