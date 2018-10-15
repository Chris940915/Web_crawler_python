import re
import requests
from bs4 import BeautifulSoup
import json
import collections


def page_check():

	req_last_list = requests.get('http://helpline.nih.go.kr/cdchelp/disease.gst?method=listView')
	html_last_list = req_last_list.text
	soup_last_list = BeautifulSoup(html_last_list, 'html.parser')

	try:
		btn_last_lists = soup_last_list.select(
					'#page_box > li > a > img'
					)	
			
		for btn_last_list in btn_last_lists:
			print(btn_last_list.get('alt'))

		link_last_lists = soup_last_list.select(
					'#page_box > li > a'
					)	

		req  = requests.get('http://helpline.nih.go.kr/cdchelp/' + str(link_last_lists[-1]['href']))    	
		html = req.text	
		soup = BeautifulSoup(html, 'html.parser')

		page = soup.select(
	  		'#page_box > li > a > span'
	  		)  	  
		global last_list
		last_list = page[-1].text
		print(last_list)
	except:
		print("last list don't exists")
page_check()

def page_check():


	req  = requests.get('http://helpline.nih.go.kr/cdchelp/disease.gst?method=listView&frm=&OMIM_ID=&Enf=&cateCode=&searchKind=&Kof=&mediExpenses=&searchWord=&curPage=101')    	
	html = req.text	
	soup = BeautifulSoup(html, 'html.parser')

	page = soup.select(
  		'#page_box > li > a > span'
  	)  	  
	global last_list
	last_list = page[-1].text

	print (last_list)  