import re
import requests
import json
import collections
import sys
from bs4 import BeautifulSoup
from urllib.parse import quote
from decimal import Decimal

#

numbers = []
with open("C:/Users/sub/Documents/translation/111.json") as link_json :
	link = json.load(link_json)

	for i in range(1,5): # TODO 저절로 되게 
		for j in range(1,5):
			before_url = link[str(i)][str(j)] 
			number = re.findall("\d+" , before_url)[0]
			numbers.append(number)

print(numbers)



with open("C:/Users/sub/Documents/translation/222.json", 'w', encoding = 'UTF8') as json_file :

	dict = {}


#주소가 사라진거, 잠시접속불가 가정들에 대한 조건들, 내용이 바뀐거나 html 구조 바뀐거 detect 
#  다시 크롤링했을때 바뀐게 있나 확인 

#파일명 보기 좋게 바꾸기. 
	for i in numbers :
		req = requests.get("http://helpline.nih.go.kr/cdchelp/disease.gst?method=detailView&NO_DISEASE_CODE_SEQ=" +str(i)+ "&Kof=&Enf=&cateCode=&searchKind=&searchWord=&mediExpenses=&dic_use=Y&potalDis=Y&curPage=&frm")
		soup = BeautifulSoup(req.content, 'html.parser')
		

		titles = soup.select(
			'#detail_list > div'
		)	
		name = soup.select(
			'#detailbd_tit > h3'
		)

		#detailbd_tit > h3
		#병명 
		for title in titles:
			name1 = name[0].text
			name2 = name1.replace(name1[-65:], "")
			print(name2)

			dict = {'subtitle' : title.img.get("alt") , 'content' : title.text}
		
			dict1 = {'name' : name2 , 'code' : i , 'data ':
						{
							'subtitle' : title.img.get("alt") , 'content' : title.text
						}
					}
			print(dict1) # print 과감히 지워 
			json.dump(dict1, json_file, ensure_ascii=False, indent=3)		
			json_file.write('\n')
		

			


'''content_of_article = soup.select('#detail_list > div > div.dlist_txt > p')	
		print(content_of_article[0])
		# content_of_article 이 list 형식으로 나옴. 
		

		'''



	 