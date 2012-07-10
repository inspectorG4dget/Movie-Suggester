'''
Created on Aug 30, 2010

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

from suggest import *
from movie import *
import cPickle, sys

PROGRAM_TITLE = "Ashwin's Suggester"

def loadData(database_file):
	f = open(database_file ,'r')
	d = cPickle.load(f)
	f.close()

	return d

def saveData(data, database_file):
	f = open(database_file, 'w')
	cPickle.dump(data, f)    
	f.close()
	
def addMovie(data):
	info = easygui.multenterbox(title=PROGRAM_TITLE, fields=("Title", "Year", "Actors (comma separated)", "Directors (comma separated)", "Producers (comma separated)", "Genres (comma separated)"))
	title, year, actors, directors, producers, genres = info
	
	year = year.strip()
	title = title.strip() + " [%s]" %year
	actors = [a.strip() for a in actors.split(",")]
	directors = [d.strip() for d in directors.split(",")]
	producers = [p.strip() for p in producers.split(",")]
	genres = [g.strip() for g in genres.split(",")]
	m = Movie(title=title, genres=genres, actors=actors, directors=directors, producers=producers, year=year)
	
	if title not in data.keys():
		data[title] = m
		easygui.msgbox(title=PROGRAM_TITLE, msg="%s has been Added to the database" %title)
		
	else:
		easygui.msgbox(title=PROGRAM_TITLE, msg="That movie already exists in the database")
	
def removeMovie(data):
	choice = easygui.choicebox(title=PROGRAM_TITLE, choices=data.keys())
	data.pop(choice)
	easygui.msgbox(title=PROGRAM_TITLE, msg="%s Removed from Database" %choice)
	
def editMovie(data):
	choice = data[easygui.choicebox(title=PROGRAM_TITLE, choices=data.keys())]
	
	info = easygui.multenterbox(title=PROGRAM_TITLE, 
								fields=("Title", "Year", "Actors (comma separated)", "Directors (comma separated)", "Producers (comma separated)", "Genres (comma separated)"), 
								values=(choice.title, choice.year, 
									', '.join(choice.actors), 
									', '.join(choice.directors), 
									', '.join(choice.producers), 
									', '.join(choice.genres) ))

	title, year, actors, directors, producers, genres = info
	
	year = year.strip()
	title = title.strip() + " [%d]" %year
	actors = [a.strip() for a in actors.split(",")]
	directors = [d.strip() for d in directors.split(",")]
	producers = [p.strip() for p in producers.split(",")]
	genres = [g.strip() for g in genres.split(",")]
	data[choice] = Movie(title=title, genres=genres, actors=actors, directors=directors, producers=producers, year=year)
	
	easygui.msgbox(title=PROGRAM_TITLE, msg="%s successfully edited" %choice.title)
	
if __name__ == "__main__":
	
	filename = easygui.fileopenbox(title=PROGRAM_TITLE, msg="Choose Database File")
	if filename:
		data = loadData(filename)
	else:
		easygui.msgbox(msg="No Database File Selected. Program Will Exit", title=PROGRAM_TITLE)
		sys.exit(0)
	
	nameToFunc = {
					"Add Movie" 		: addMovie,
					"Remove Movie" 		: removeMovie,
					"Edit Movie" 		: editMovie,
					"List By Year" 		: listByYear,
					"List By Actors" 	: listByActors,
					"List By Genres"	: listByGenres,
					"List By Directors" : listByDirectors,
					"List By Producers" : listByProducers,
					"List All Movies"	: listAll,
					"Save Database"		: saveData,
					"Load Database"		: loadData
				  }
	
	while True:
		
		operation = easygui.choicebox(title=PROGRAM_TITLE, choices=nameToFunc.keys())
		
		if operation:	# an operation was chosen
			if operation == "Load Database":
				filename = easygui.fileopenbox(title=PROGRAM_TITLE, msg="Choose Database File")
				loadData(filename)
			
			elif operation == "Save Database":
				filename = easygui.fileopenbox(title=PROGRAM_TITLE, msg="Choose Database File")
				saveData(data, filename)
				
			elif "List By " in operation:
				params = easygui.enterbox(msg="Enter %s (comma separated):" %operation.split()[-1], title=PROGRAM_TITLE)
				params = [p.strip() for p in params.split(',')]
				exec("listBy%s(data, params)" %operation.split()[-1])
				
			else:
				nameToFunc[operation](data)
		
		else:
			sys.exit(0)	