# -*- coding: utf-8 -*-

"""

@author: Shashank Sapaliga, Dhwani Shah, Ishpreet Kaur, Shashwat Sagar
"""

import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from tkinter import ttk 
import ast 
from datetime import datetime
from tkinter import scrolledtext 
import numpy as np


class Visualization():
    def __init__(self):
        review_set = []
        with open ('OnePlus8_reviews.csv', 'r', encoding='utf-8') as f:
            for n,i in enumerate(f):
                review_set.append([i])
        # reading the data from the file 
        with open('finalOrientation.txt') as f: 
            FinalOrientedReviews = f.read()
           
        d = ast.literal_eval(FinalOrientedReviews)
        
        with open('OrientedReviews.txt') as f1: 
            Orienteddata = f1.read()
            
        d1 = ast.literal_eval(Orienteddata) 
        
        
        from PIL import ImageTk,Image
        
        
        
        root = tk.Tk() 
        root.title("Visulization And Features") 
        root.geometry('1700x1700')
        
        tabControl = ttk.Notebook(root) 
        
        tab1 = ttk.Frame(tabControl)
        #tab1.pack()
        #tab1 = Canvas(root, width = 700, height = 700)  
        #tab1.pack()
        #tab2 = ttk.Frame(tabControl)
        #tab2 = ttk.Frame(tabControl)
        tab2 = tk.PanedWindow(orient ='horizontal') 
        tabControl.add(tab1, text ='Visulization') 
        tabControl.add(tab2, text ='Features') 
        tabControl.pack(expand = 1, fill ="both")
        
        
        #ttk.Label(tab1, text ="Visulization").grid(column = 0, row = 0, padx = 400, pady = 400) 
        #ttk.Label(tab2, text ="Lets dive into the\ world of computers").grid(column = 0,row = 0, padx = 40, pady = 30) 
        
        text1 = tk.Text(tab2 , height=8, width =10)
        tab2.add(text1) 
        
        text2 = scrolledtext.ScrolledText(tab2, 
        									wrap = "word", 
        									width = 200, 
        									height = 300, 
        									font = ("Times New Roman", 
        											15))
        text2.focus() 
        #text2 = tk.Text(tab2, height=200, width=300)
        tab2.add(text2)
        
        text3 = scrolledtext.ScrolledText(tab2, 
        									wrap = "word", 
        									width = 200, 
        									height = 300, 
        									font = ("Times New Roman", 
        											15))
        text3.focus() 
        
        #text3 = tk.Text(tab2, height=200, width=300)
        tab2.add(text3) 
        
        
        
        l_positive = tk.Label(text2, text = "Positive Reviews") 
        l_positive.config(font =("Courier", 10)) 
        l_positive.pack()
        
        l_negative = tk.Label(text3, text = "Negative Reviews") 
        l_negative.config(font =("Courier", 10)) 
        l_negative.pack()
        
        #lbl = tk.Label(text2)
        #lb2 = tk.Label(text3)
        
        lbl = tk.Text(text2, height=1000, width=80)
        lb2 = tk.Text(text3, height=1000, width=80)
        lbl.pack()
        lb2.pack()
        def memory():
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['memory'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['memory'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                 lbl.insert(tk.END,"No Reviews")
            
        def audio():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['audio'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['audio'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1  
            except:
                lbl.insert(tk.END,"No Reviews")
        
        def camera():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['camera'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['camera'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        
        def display():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['display'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['display'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
        
        def weight():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['weight'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['weight'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def wifi():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['wifi'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['wifi'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
            
        def keypad():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['keypad'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['keypad'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def battery():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['battery'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['battery'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def interface():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['interface'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['interface'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def processor():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['processor'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['processor'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def radio():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['radio'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['radio'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def bluetooth():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['bluetooth'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['bluetooth'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
        
        def touch_screen():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['touch_screen'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['touch_screen'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
            
        def m_size():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['m_size'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['m_size'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
        
        def price():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['price'][0])
                n = 1
                for i in li:                
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['price'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
        
        def misc():
        
            lbl.delete('1.0',END)
            lb2.delete('1.0',END)
            try:
                li = list(d['misc'][0])
                n = 1
                for i in li:  
                    if len(review_set[i][0]) > 10: 
                        lbl.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n + 1
                n = 1    
                li = list(d['misc'][1])
                for i in li:                
                    if len(review_set[i][0]) > 10:
                        lb2.insert(tk.END,str(n)+'.'+review_set[i][0]+'\n')
                        n = n +1
            except:
                lbl.insert(tk.END,"No Reviews")
        
        
        Memory = ttk.Button(tab2, text="Memory",width =12, command=memory).place(x=0, y=0)
        Audio = ttk.Button(tab2, text="Audio",width =12, command=audio).place(x=0, y=23)
        Camera = ttk.Button(tab2, text="Camera",width=12, command=camera).place(x=0, y=46)
        Display = ttk.Button(tab2, text="Display",width =12, command=display).place(x=0, y=69)
        Weight = ttk.Button(tab2, text="Weight",width=12, command=weight).place(x=0, y=92)
        Keypad = ttk.Button(tab2, text="Keypad",width =12, command=keypad).place(x=0, y=115)
        Battery = ttk.Button(tab2, text="Battery",width=12, command=battery).place(x=0, y=138)
        Interface = ttk.Button(tab2, text="Interface",width =12, command=interface).place(x=0, y=161)
        Processor = ttk.Button(tab2, text="Processor",width=12, command=processor).place(x=0, y=184)
        Radio = ttk.Button(tab2, text="Radio",width =12, command=radio).place(x=0, y=207)
        Bluetooth = ttk.Button(tab2, text="Bluetooth",width=12, command=bluetooth).place(x=0, y=230)
        touch_screen = ttk.Button(tab2, text="Touch Screen",width=12, command=touch_screen).place(x=0, y=253)
        size = ttk.Button(tab2, text="Size",width=12, command=m_size).place(x=0, y=276)
        wifi = ttk.Button(tab2, text="WiFi",width=12, command=wifi).place(x=0, y=299)
        price = ttk.Button(tab2, text="Price",width=12, command=price).place(x=0, y=322)
        misc = ttk.Button(tab2, text="Misc",width=12, command=misc).place(x=0, y=345)
        
        
        ############################################ CHART #################################################
        
        fpos=[]
        fneg=[]
        f1=()
        fpost=()
        fnegt=()
        
         
        colors = ('tomato','darkorchid','yellowgreen','firebrick','lightskyblue','chocolate','navy','lightcoral'
                ,'aquamarine','indigo','teal' ,'crimson','gold','springgreen','royalblue','indianred','slategrey')
        
        
        title1='Positive Reviews Distribution'
        title2='Negative Reviews Distribution'
        
         
        #split the input data into lists
        
        def splitLabels(FinalReviews):
            f1 = tuple(d.keys())
            for f in f1:
                fpos.append(len(d.get(f)[0]))
                fneg.append(len(d.get(f)[1]))
            fpost=tuple(fpos)
            fnegt=tuple(fneg)
            return f1,fpost, fnegt
        
         
        
        #to create pie chart
        
        def showCharts(f1,flab,title,prefix):
            fig1,ax1=plt.subplots(figsize=(8,4))
            _,_ = ax1.pie(flab, startangle=90, radius=1000,colors=colors, wedgeprops={'edgecolor' :'white', 'linewidth':3})
            ax1.axis('equal')
            totalp= sum(flab)
            plt.legend(
                loc='upper left',
                labels=['%s, %1.1f%%' % (
                    l, (float(s) / totalp) * 100)
                        for l, s in zip(f1, flab)],
                prop={'size': 11},
                bbox_to_anchor=(0.05, 1),
                bbox_transform=fig1.transFigure
            )
        
            plt.title(title)
        
            plt.tight_layout(pad=3)
            now = datetime.now()
            name = prefix+now.strftime("%d%m%Y%H%M%S")+'.png'
            plt.savefig(name)
            
            plt.show()
            return name
        
        def barChart(f1,fpost, fnegt):
            #print(len(f1))
            X = np.arange(0,(len(f1)),1.0)
            fig = plt.figure(figsize=(8,5))
            ax = fig.add_axes([0,0,1,1])
            plt.xticks(X)
            ax.set_xticklabels(list(f1),rotation= 90)
            ax.bar(X +0.0, fpost, color = 'tomato', width = 0.5,label="Positive Comments")
            ax.bar(X + 0.40, fnegt, color = 'blueviolet', width = 0.4 ,label ="Negative Comments")
            ax.legend()
            plt.title("Overall Positive/Negative Reviews Distribution")
            plt.savefig("Overall.png", bbox_inches = 'tight')
                    
        
        
        features, postiveLabels, NegativeLabels= splitLabels(d)
        
        #to Show overall bar chart
        barChart(features, postiveLabels, NegativeLabels)
        
        #to show positive review Pie chart
        
        name1 = showCharts(features,postiveLabels, title1,'Positive')
        
        #to show positive review Pie chart
        
        name2 = showCharts(features,NegativeLabels, title2,'Negative')
        
        
        canvas1 = tk.Canvas(tab1, width = 460, height = 650)
        #canvas1.pack(side="left", expand=True)
        canvas1.place(x = 100,y = 0)
        img1 = ImageTk.PhotoImage(Image.open(name1))
        canvas1.create_image(0, 0, anchor=NW, image=img1)
        
        canvas2 = tk.Canvas(tab1, width = 460, height = 650)  
        canvas2.place(x = 100,y = 350)
        #canvas2.pack(side="left", expand=True)
        img2 = ImageTk.PhotoImage(Image.open(name2))
        canvas2.create_image(0, 0, anchor=NW, image=img2) 
        
        canvas3 = tk.Canvas(tab1, width = 700, height = 650) 
        canvas3.place(x = 700,y = 100) 
        #.pack(side="right", expand=True)
        img3 = ImageTk.PhotoImage(Image.open("Overall.png"))
        canvas3.create_image(0, 0, anchor=NW, image=img3)
 
     
        
        
        
        root.mainloop()
    
