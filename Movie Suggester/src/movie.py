'''
Created on Aug 28, 2010

@author: ashwin
'''

class Movie:
	def __init__(self, title=None, genres=None, actors=None, directors=None, producers=None, year=None):
		
		self.title = title if title else ''
		self.genres = genres if genres else []
		self.actors = actors if actors else []
		self.directors = directors if directors else []
		self.producers = producers if producers else []
		self.year = int(year) if year else 0
		self.watched = 0
		
		self.genres.sort()
		self.actors.sort()
		self.directors.sort()
		self.producers.sort()