# -*- coding: utf-8 -*-
"""

@author: Shashank Sapaliga, Shashwat Sagar, Ishpreet Kaur, Dhwani Shah
"""

from Processor.Processor import Processor
from WebScrapper.Scrapper import Scrapper
import json
import os

print("The Data is being scrapped please wait!!!!!!!!!!")
start=0
flag = 1
scrap = Scrapper()
p = Processor()
print("Creating your Visualization Please Wait.........")
p.createOrientedReviewsMap()
p.summarize()
p.removeFeaturesWithNoReview()
p.separatePositiveAndNegative()

if os.path.exists("finalOrientation.txt"):
    os.remove("finalOrientation.txt")
f = open("finalOrientation.txt", "a")
f.write(str(p.finalOrientation))
f.close()
if os.path.exists("OrientedReviews.txt"):
    os.remove("OrientedReviews.txt")
f = open("OrientedReviews.txt", "a")
f.write(str(p.orientedReviews))
f.close()

from Visualization.Featuresandvisual import Visualization 
vis = Visualization()




