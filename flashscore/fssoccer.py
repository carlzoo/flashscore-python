#!/usr/bin/env python
from fsbase import *

class FSSoccer(FlashScore):
	def __init__(self):
		FlashScore.__init__(self)
		self.url="http://www.flashscore.com/"
		self.standingsurls=""

	def find_team(self,query):
		q=query.lower()

		results=[]
		soup=BeautifulSoup(self.fetch_page(self.url))
		leagues=soup.findAll('table',{'class':'soccer'})

		#first try to search in league name
		for league in leagues:
			thead=league.find('thead')
			name=thead.find('span',{'class':'country_part'}).text.strip() + thead.find('span',{'class':'tournament_part'}).text.strip()
			name_lc=name.lower()
			if q in name_lc:
				matches=league.find('tbody').findAll('tr')
				for match in matches:
					home=match.find('td',{'class':'team-home'}).text.strip()
					away=match.find('td',{'class':'team-away'}).text.strip()
					score=match.find('td',{'class':'score'}).text.strip()
					matchtimer=match.find('td',{'class':'timer'}).text.strip()

					if not matchtimer: #match has not started
						matchstatus=match.find('td',{'class':'time'}).text.strip()
					elif matchtimer == "Finished": #match finished
						matchstatus = "FT"
					else: #any other case
						matchstatus=matchtimer

					item = home + " " + score + " " + away + " " + matchstatus
					results.append(item.replace(u'\xa0', u' ')) #replace the non-space break character with space
		
		#then search in team name
		for league in leagues:
			matches=league.find('tbody').findAll('tr')
			for match in matches:
				home=match.find('td',{'class':'team-home'}).text.strip()
				home_lc=home.lower()
				away=match.find('td',{'class':'team-away'}).text.strip()
				away_lc=away.lower()
				if (q in home_lc) or (q in away_lc): #we have a match
					score=match.find('td',{'class':'score'}).text.strip()		 
					matchtimer=match.find('td',{'class':'timer'}).text.strip()

					if not matchtimer: #match has not started
						matchstatus=match.find('td',{'class':'time'}).text.strip()
					elif matchtimer == "Finished": #match finished
						matchstatus = "FT"
					else: #any other case
						matchstatus=matchtimer

					item = home + " " + score + " " + away + " " + matchstatus
					results.append(item.replace(u'\xa0', u' ')) #replace the non-space break character with space
		return results

	'''	
	not working at the moment
	def get_standings(self,query):
		results=[]
		q=query.lower()
		replacement=self.keywords.get(q) #replace the keyword if found in dictionary
		if replacement:  #replace the keyword if found in dictionary
			q=replacement
		#link=self.standingsurls.get(q)
		link="http://www.flashscore.com/soccer/belarus/vysshaya-liga/standings/"
		if not link:
			return False
		soup=BeautifulSoup(self.fetch_page(link,'#glib-stats-data'))
		print soup.find('div',{'id':'glib-stats-data'})
		teams=soup.findAll('span',{'class':'team_name_span'})
		points=soup.findAll('td',{'class':'goals'})
		print teams
		count=len(teams)
		for i in range(0,count):
			results.append(teams[i] + " - " + points[i*2])
		return results
	'''
