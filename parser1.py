import requests
from bs4 import BeautifulSoup as bs



LOGIN_INFO = {
	'userId' : 'sostkr',
	'userPassword' : 'shinhs94'
}



with requests.Session() as s:

	first_page  = s.get('https://www.clien.net/service')
	html = first_page.text
	soup = bs(html, 'html.parser')
	csrf = soup.find('input' , {'name' : '_csrf'})
	print(csrf['value'])

	LOGIN_INFO = {**LOGIN_INFO, **{'_csrf' : csrf['value']}}
	print(LOGIN_INFO)

	login_req = s.post("https://www.clien.net/service/login", data=LOGIN_INFO)

	print(login_req.status_code)

	#div_content > div.post_title.symph_row > h3
	#div_content > div.post_title.symph_row 
