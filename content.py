import requests
from bs4 import BeautifulSoup
import json
import re


def isTitle (myString):

	if myString.get() is None:
		return True
	else:
		return False

req = requests.get('http://helpline.nih.go.kr/cdchelp/disease.gst?method=detailView&NO_DISEASE_CODE_SEQ=734&Kof=&Enf=&cateCode=&searchKind=&searchWord=&mediExpenses=&dic_use=Y&potalDis=Y&curPage=&frm=')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

'''titles = soup.select(
		'h4 > img'
	)

print(titles[0].get('alt'))
'''
divs = soup.select("#detail_list > div")

for div in divs:

	print(div.img.get('alt'))

	if isTitle(div):
		print(div.text)
	else:
		print(div.img.get('alt'))
	'''title = div.img.get('alt')
	if isBlank(title):
		
	else:
		print(title)
	'''


	#for title in div.img.find_all('alt'):
	#	print(title)


#isBlank(divs)


#for div in divs.find_all()
	

'''for div in range(len(divs)):
	if(divs[])'''


#generalD 개요
#detail_list > div:nth-child(2) > div.dlist_txt
#symptoms 증상
#detail_list > div:nth-child(3) > div.dlist_txt
#causes
#detail_list > div:nth-child(4) > div.dlist_txt
#diagnosis
#detail_list > div:nth-child(5) > div.dlist_txt
#treatment
#detail_list > div:nth-child(6) > div.dlist_txt


#
