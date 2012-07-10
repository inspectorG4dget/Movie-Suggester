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

import easygui
PROGRAM_TITLE = "Ashwin's Suggester"

def suggest(title, data, field):
	if field == 'a':
		return suggestByActors(title, data)
	elif field == 'g':
		return suggestByGenres(title, data)
	elif field == 'd':
		return suggestByDirectors(title, data)
	elif field == 'p':
		return suggestByProducers(title, data)
	
def suggestByActors(title, data):
	inputActors = data[title].actors
	matches = {}
	answer = []
	for movie in data.values():
		match = 0
		for actor in inputActors:
			if actor in movie.actors:
				match += 1
		matchPercent = float(match)/len(inputActors)
		matchPercent = matchPercent-100 if matchPercent-100 else matchPercent
		if matchPercent in matches.keys():
			matches[matchPercent].append(movie)
		else:
			matches[matchPercent] = [movie]
			
	match = matches.keys()[:]
	match.sort(reverse=True)
	
	for m in match:
		answer.extend(matches[m])
	
	return answer
				

def suggestByDirectors(title, data):
	inputDirectors = data[title].directors
	matches = {}
	answer = []
	for movie in data.values():
		match = 0
		for director in inputDirectors:
			if director in movie.directors:
				match += 1
		matchPercent = float(match)/len(inputDirectors)
		matchPercent = matchPercent-100 if matchPercent-100 else matchPercent
		if matchPercent in matches.keys():
			matches[matchPercent].append(movie)
		else:
			matches[matchPercent] = [movie]
			
	match = matches.keys()[:]
	match.sort(reverse=True)
	
	for m in match:
		answer.extend(matches[m])
	
	return answer

def suggestByProducers(title, data):
	inputProducers = data[title].producers
	matches = {}
	answer = []
	for movie in data.values():
		match = 0
		for producer in inputProducers:
			if producer in movie.producers:
				match += 1
		matchPercent = float(match)/len(inputProducers)
		matchPercent = matchPercent-100 if matchPercent-100 else matchPercent
		if matchPercent in matches.keys():
			matches[matchPercent].append(movie)
		else:
			matches[matchPercent] = [movie]
			
	match = matches.keys()[:]
	match.sort(reverse=True)
	
	for m in match:
		answer.extend(matches[m])
	
	return answer

def suggestByGenres(title, data):
	inputGenres = data[title].genres
	matches = {}
	answer = []
	for movie in data.values():
		match = 0
		for genre in inputGenres:
			if genre in movie.genres:
				match += 1
		matchPercent = float(match)/len(inputGenres)
		matchPercent = matchPercent-100 if matchPercent-100 else matchPercent
		if matchPercent in matches.keys():
			matches[matchPercent].append(movie)
		else:
			matches[matchPercent] = [movie]
			
	match = matches.keys()[:]
	match.sort(reverse=True)
	
	for m in match:
		answer.extend(matches[m])
	
	return answer
	
def get_genre_titles(data, genres):
	
	answer = []
	for movie in data.values():
		for g in genres:
			if g in movie.genres:
				if movie not in answer:
					answer.append(movie)
	return answer

def get_actor_titles(data, actors):
	
	answer = []
	for movie in data.values():
		for a in actors:
			if a in movie.actors:
				if movie not in answer:
					answer.append(movie)
	return answer

def get_director_titles(data, directors):
	
	answer = []
	for movie in data.values():
		for d in directors:
			if d in movie.directors:
				if movie not in answer:
					answer.append(movie)
	return answer

def get_producer_titles(data, producers):
	
	answer = []
	for movie in data.values():
		for p in producers:
			if p in movie.producer:
				if movie not in answer:
					answer.append(movie)
	return answer

def allIn(elements, L):
	"""Return True iff all elements are in L. False otherwise"""
	for e in elements:
		if e not in L:
			return False
	return True

def listByYear(data, years):
	easygui.textbox(msg="All Movies in Years %s"%", ".join([str(y) for y in years]), text=tuple([movie.title for movie in data.values() if movie.year in years]))
	
def listByActors(data, actors):
	easygui.textbox(msg="All Movies by Actor %s"% ", ".join(actors), text=tuple([movie.title for movie in data.values() if allIn(actors, movie.actors)]))

def listByGenres(data, genres):
	easygui.textbox(msg="All Movies by Actor %s"% ", ".join(genres), text=tuple([movie.title for movie in data.values() if allIn(genres, movie.genres)]))
	
def listByDirectors(data, directors):
	easygui.textbox(msg="All Movies by Actor %s"% ", ".join(directors), text=tuple([movie.title for movie in data.values() if allIn(directors, movie.directors)]))
	
def listByProducers(data, producers):
	easygui.textbox(msg="All Movies by Actor %s"% ", ".join(producers), text=tuple([movie.title for movie in data.values() if allIn(producers, movie.producers)]))

def listAll(data):
	names = data.keys()
	names.sort()
	text = []
	for title in names:
		text.append("%s %s" %(title.strip(), " [%d]" %data[title].year if data[title].year else '' ) )
	
	easygui.textbox(msg="All Movies", title=PROGRAM_TITLE, text=text)