import requests
from bs4 import BeautifulSoup



req = requests.get('https://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1168000000&articleOrderCode=&cpId=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&siteOrderCode=&cmplYn=')
html = req.text
soup = BeautifulSoup(html, 'html.parser')


link_title = soup.select(
	'#depth4Tab0Content > div > table > tbody > tr > td.align_l.name > div > a.sale_title'
	)
link_price = soup.select(
	'#depth4Tab0Content > div > table > tbody > tr > td.num.align_r > div > strong'
	)

print(type(link_title))


for link in range(len(link_title)):
	print(link_title[link].get_text())

	
	#board_tb > table > tbody > tr:nth-child(1) > td:nth-child(4) > find_all
	#board_tb > table > tbody > tr:nth-child(1) > td:nth-child(4) > a


	#board_tb


	#body > h3:nth-child(7) > a

	#board_wrap

	#depth4Tab0Content > div > table > tbody > tr:nth-child(1) > td.align_l.name > div


	#depth4Tab0Content > div > table > tbody > tr:nth-child(1) > td.align_l.name > div > a