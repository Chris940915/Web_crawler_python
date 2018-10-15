import requests
from bs4 import BeautifulSoup
import json
import os


req = requests.get("https://beomi.github.io/beomi.github.io_old/")


html = req.text 

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
	'h3 > a'
	)

data = { }

for title in my_titles:
		data[title.text] = title.get("href") + "\n"



with open(os.path.join("C:/Users/sub/Documents", 'result.json'), 'w+') as json_file :
	json.dump(data, json_file) 