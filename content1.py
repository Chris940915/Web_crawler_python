import requests
from bs4 import BeautifulSoup
import os

req = requests.get('http://helpline.nih.go.kr/cdchelp/disease.gst?method=detailView&NO_DISEASE_CODE_SEQ=1368&Kof=&Enf=&cateCode=&searchKind=&searchWord=&mediExpenses=&dic_use=Y&potalDis=E&curPage=1&frm=')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select(
	'#detail_list > div'
)

name = soup.select(
	'#detailbd_tit > h3'
	
	)



name1 = name[0].text
name2 = name1.replace(name1[-65:],"")
print(name2)

'''
for title in titles:

	print(title.img.get('alt'))
	print(title.text)

'''
	#detailbd_tit > h3
	#detailbd_tit > h3 > noscript