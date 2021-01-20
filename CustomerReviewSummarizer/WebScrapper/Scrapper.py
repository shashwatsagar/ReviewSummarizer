# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:08:03 2020

@author: Shashank Sapaliga, Shashwat Sagar, Ishpreet Kaur, Dhwani Shah
"""
import requests
from bs4 import BeautifulSoup
import csv

class Scrapper():
    def __init__(self):
        
        with open('OnePlus8_reviews.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for i in range (1,20):    
                url ='https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B085J17VVP/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
                r = requests.get('http://localhost:8050/render.html',params={'url':url, 'wait':2})    
                soup = BeautifulSoup(r.text, 'html.parser')       
                reviews = soup.find_all('div', {'data-hook':'review'})
                for item in reviews:
                        review_comments = item.find('span',{'data-hook':'review-body'}).text.strip()
                        writer.writerow([review_comments]) 
            print("Data has been successfully Scrapped from Amazon Website for OnePlus 8") 
                
                