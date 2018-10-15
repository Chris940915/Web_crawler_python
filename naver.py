import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.naver.com')

soup = BeautifulSoup(req.content , 'html.parser')

links = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')

for link in links:
	print(link.text)	






