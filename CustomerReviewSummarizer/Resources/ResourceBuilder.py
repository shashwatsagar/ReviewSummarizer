# -*- coding: utf-8 -*-
"""
@author: Shashank Sapaliga, Shashwat Sagar, Ishpreet Kaur, Dhwani Shah
"""
import csv
import numpy as np

class ResourceParser():
    features={}
    positives = np.empty((0, 0), int)
    negatives = np.empty((0, 0), int)
    negations = np.empty((0, 0), int)
    def __init__(self):
        with open ('features.txt', 'r') as f:
            for row in csv.reader(f, delimiter=','):
                pass
            for i in row:
                self.features[(i.split('=',1)[0]).strip()] = (i.split('=',1)[1]).strip()
                
        #Reading and storing positives data in dictionary    
        
        with open ('positive.txt', 'r') as f:
            for row in csv.reader(f, delimiter='\n'):
                self.positives = np.append(self.positives,row[0])    
        
        #Reading and storing negatives data in dictionary    
        
        with open ('negative.txt', 'r') as f:
            for row in csv.reader(f, delimiter='\n'):
                self.negatives = np.append(self.negatives,row[0])
        
        ##Reading and storing negations data in dictionary
        
        with open ('negations.txt', 'r') as f:
            for row in csv.reader(f, delimiter='\n'):
                self.negations = np.append(self.negations,row[0])