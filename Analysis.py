
import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库

def analysis(url):
	res = requests.get(url)
	# 返回一个response对象，赋值给res
	html = res.text
	print(res.status_code)
	soup = BeautifulSoup( html,'html.parser') 
	return soup 