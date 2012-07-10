'''
Created on Aug 28, 2010

@author: ashwin

 Licensed to Ashwin Panchapakesan under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 Ashwin licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
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