#!/usr/bin/env python
import dryscrape
from bs4 import BeautifulSoup
import os

class FlashScore(object):
	def __init__(self):
		self.url="http://www.flashscore.com/"
		self.timeout=20
		self.useragent="Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"
		dryscrape.start_xvfb()
	
	def fetch_page(self,link=None,loadFinished='.ifmenu'):

		# set up a web scraping session
		if link is None:
			link=self.url
		sess = dryscrape.Session(base_url = self.url)

		sess.visit('/')
		sess.at_css(loadFinished, timeout=self.timeout) #wait until the JavaScript-generated scores portion has finished loading
		response = sess.body()

		return response

	def load_dict(self):
		keywords={}
		with open( os.path.dirname(os.path.abspath(__file__)) + '/dict.txt','r') as document:
			for line in document:
				line = line.split("||")
				if not line: #empty line
					continue
				keywords[line[0]]=line[1:]
		return keywords

	def switch_browser(self,browser):
		if browser=="firefox":
			self.useragent="Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"
		elif browser=="chrome":
			self.useragent="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
		elif browser=="opera":
			self.useragent="Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16"
		elif browser=="ie":
			self.useragent="Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
		elif browser=="safari":
			self.useragent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
		else:
			raise ValueError("invalid browser name given")
