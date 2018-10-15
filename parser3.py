import requests
from bs4 import BeautifulSoup
import json
import os
import collections

x = 1


#with open(os.path.join('C:/Users/sub/Documents/translation/crawler/result.json'), 'w+') as json_file:


def tree():
	return collections.defaultdict(tree)

dict = {}
# dict 주석적을때 주석 붙여서 띄워쓰기 


with open('C:/Users/sub/Documents/translation/111.json', 'w') as json_file:
	while x < 111: # TODO 111의 변수명 변수 변경되도 체크
			
		req = requests.get('http://helpline.nih.go.kr/cdchelp/disease.gst?method=listView&frm=&OMIM_ID=&Enf=&cateCode=&searchKind=&Kof=&mediExpenses=&searchWord=&curPage='+str(x))

		soup = BeautifulSoup(req.content, 'html.parser')

		links = soup.select('#board_tb > table > tbody > tr > td > a')
		#links 에 list 형식으로 저장 

		#data = {}
		i = 0
		
		for link in links:
			print(str(x) + '\t' + str(i))
			dict[x][i] = link['href']
			
			i += 1 
		#for link in links:
		#	data[link.text] = link['href']

		#	json.dump(data, json_file)
		x += 1 
	json.dump(dict, json_file)

#detail_list > div:nth-child(2) > div.dlist_txt > p

		


#board_tb > table > tbody > tr:nth-child(1) > td:nth-child(4)
#board_tb > table > tbody > tr > td > a