# -*- coding: utf-8 -*-
"""

@author: Shashank Sapaliga, Shashwat Sagar, Ishpreet Kaur, Dhwani Shah
"""

import nltk

#rp = ResourceParser()

class Tagger():
    taggedReviews = []
    review_set = []
    def __init__(self):
        
        with open ('OnePlus8_reviews.csv', 'r', encoding='utf-8') as f:
            for i in f:
                self.review_set.append([i])   
            for j in self.review_set:
                for k in j:
                    text = nltk.word_tokenize(k.lower())
                    self.taggedReviews.append(nltk.pos_tag(text))

