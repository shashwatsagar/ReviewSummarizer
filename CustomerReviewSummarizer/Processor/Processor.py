# -*- coding: utf-8 -*-
"""

@author: Shashank Sapaliga, Shashwat Sagar, Ishpreet Kaur, Dhwani Shah
"""

from Tagger.Tagger import Tagger
from Resources.ResourceBuilder import ResourceParser

class Processor():
    orientedReviews = {}    
    finalOrientation = {}
    
    def __init__(self):
        self.t = Tagger()
        self.rp = ResourceParser()
    def addReview(self,w,i,orientation,negated):
        map = {}
        if negated:
            orientation *= -1   
        if w == "misc":
            map = Processor.orientedReviews["misc"]
        else:
            map = Processor.orientedReviews[self.rp.features[w]]
        if i not in map:
            map[i] = orientation
        if w == "misc":
            Processor.orientedReviews["misc"]=map
        else:
           Processor.orientedReviews[self.rp.features[w]]=map
    def summarize(self): 
        for i in range(0,len(self.t.taggedReviews)):
            fullReview = self.t.taggedReviews[i]
            count = 0
            added = False
            orientation = 0
            done = 0
            negated = False
            while count < len(fullReview):
                opinionIndex = -1
                featureIndex = -1
                index = 0
                orientation = 0
                done =0 
                negated = False
                featureList = []
                taglist = []
                while count < len(fullReview) and (fullReview[count][1]) not in ('.',',',';',':'):
                    taglist.append(fullReview[count])
                    count+=1
                count+=1
                
                for word in taglist:
                    if word[0] in self.rp.negations:
                        negated = True
                        
                    elif word[0] in self.rp.positives or word[0] in self.rp.negatives:
                        opinionIndex = index
                        if word[0] in self.rp.positives:
                            orientation += 1
                        elif word[0] in self.rp.negatives:
                            orientation += -1
                        if done == 2:
                            if abs(featureIndex-opinionIndex)<=5:
                                for w in featureList:
                                    Processor.addReview(self,w,i,orientation,negated)
                                added = True
                                done=0
                                negated = False
                                orientation = 0
                                featureList = []
                        else:
                            done=1
                    elif word[0] in self.rp.features:
                        featureIndex = index
                        if done == 1:
                            if abs(featureIndex-opinionIndex)<=5:
                                Processor.addReview(self,word[0],i,orientation,negated)
                                added = True
                                done=0
                                negated = False
                                orientation = 0
                                featureList = []
                        else:
                            done = 2
                            featureList.append(word[0])
                    index += 1
                if orientation == 0 and negated:
                    for w in featureList:
                        Processor.addReview(w,i,1,negated)
                    added = True
            if done == 1 and (not added):
                Processor.addReview(self,"misc",i,orientation,negated)
    
    def createOrientedReviewsMap(self):
        allKeys = []
        for v in self.rp.features.values():
             allKeys.append(v)
        keys = set(allKeys)
        for key in keys:
            self.orientedReviews[key] = {}
        self.orientedReviews['misc'] = {}    #FOR UI 
         
    def removeFeaturesWithNoReview(self):
        keySet = []
        for i in self.orientedReviews.keys():
            keySet.append(i)
        keySet = set(keySet)
        emptyFeatures = []
        for key in keySet:
            if key not in self.orientedReviews:
                emptyFeatures.append(key)
        for features in emptyFeatures:
            self.orientedReviews.pop(features)
    
    def separatePositiveAndNegative(self):
        self.finalOrientation
        self.orientedReviews
        keys = []
        for i in self.orientedReviews.keys():
            keys.append(i)
        keys = set(keys)
        
        for key in keys:
            reviewSet = []
            positive = []
            negative = []
            indexing = self.orientedReviews[key]
            index=[]
            for i in indexing.keys():
                index.append(i)
            index = set(index)
            
            for j in index:
                if indexing[j] > 0:
                    positive.append(j)
                elif indexing[j] < 0:
                    negative.append(j)
            
            if len(positive) > 0 or len(negative) > 0:
                reviewSet.append(positive)
                reviewSet.append(negative)
                self.finalOrientation[key] = reviewSet
