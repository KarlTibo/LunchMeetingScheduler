# -*- coding: utf-8 -*-
from numpy import *
from datetime import date, timedelta
import copy

class Calendar(object):
    def __init__(self, name = None, startDate = date.today(), endDate = None, talkDay = "Monday"):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.talkDay = talkDay
        self.dateList = []
        self.year = self.startDate.year
        self.offset = 0

    def findOffset(self)

    def dateList(self):
        d = date(self.year,1,1)
        d = += timedelta(days = )
    



class Groups(object):
    def __init__(self, name = None):
        self.name = name
        self.nOfSpeakers = 0
            
            
if __name__ == "__main__":

    nOfTeams = int(input("How many teams are in your tournament?"))
        
    theTeamList = [Team('Team_'+str(i)) for i in range(1, nOfTeams+1)]
    theTournament = SingleElimination(theTeamList)
    theTournament.makeMatchTree()
    theTournament.show()
    
