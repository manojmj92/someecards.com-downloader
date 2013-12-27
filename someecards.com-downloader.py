#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:
# Copyright:   (c) hp
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import urllib
import os
import sys
import thread
import threading
import time


dir = os.path.dirname(os.path.abspath(__file__))
someecardsdir = dir +"\\Someecards"

if not os.path.exists(someecardsdir):
        os.makedirs(someecardsdir)
class DonwloadThread(threading.Thread):
     def __init__(self,category,low,high):
         threading.Thread.__init__(self)
         self.category = category
         self.low=low
         self.high=high

     def run(self):
         print "Downloading Category: "+ self.category
         category_dir = someecardsdir+"\\"+self.category
         try:

                if not os.path.exists(category_dir):
                        print "Making New Directory for Category "+self.category+"\n"
                        os.makedirs(category_dir)
         except:
            pass

         for pageno in range(self.low,self.high):
            time.sleep(2)
            print "Entered page number"+str(pageno)
            main_url = "http://www.someecards.com/"+self.category+"/newest/"+str(pageno)+"/40"
            url_parts = main_url.split("/")
            category_name = url_parts[3]


            main_url_response = urllib.urlopen(main_url).read()
            main_url_soup = BeautifulSoup(main_url_response)


            if not main_url_soup.find_all('a',{'class':'cardthumb'}):
                print " Page no " + str(pageno) +" of " + category_name + "is blank \n"
                break

            duplicate_counter = 0
            breaker=False
            mainbreaker=False

            for comiclink in main_url_soup.find_all('a',{'class':'cardthumb'}):
                time.sleep(2)
                full_url ="http://www.someecards.com/" +comiclink['href']
                full_url_response = urllib.urlopen(full_url).read()
                full_url_soup = BeautifulSoup(full_url_response)

                for imagelink in full_url_soup.find_all('link',{'rel':'image_src'}):

                    imageurl =  imagelink['href']
                    filename = imageurl.split('/')[5]
                    filename = filename.replace('?','')
                    filename = filename.replace(':','')
                    filename = filename.replace('*','')
                    filename = filename.replace('"','')
                    path = os.path.join(category_dir,filename)
                    if not os.path.exists(path):
                        image_response = urllib.urlopen(imageurl).read()
                        duplicate_counter=0
                        with open (path,"wb") as data:
                            time.sleep(2)
                            data.write(image_response)
                            print "Downloaded file "+ filename
                    else:
                        duplicate_counter +=1
                        print " Duplicate found: "+ filename
                        if duplicate_counter == 40:
                            print "40 Duplicate Files Found One after the other. Looks like you have all files downloaded in this page. Exiting."
                            breaker = True
                            print " Break 1"
                            break
                if breaker == True:
                    mainbreaker=True
                    print "Break 2"
                    break
            if mainbreaker==True:
                print "Break 3"
                break

def thread_initialize(choice):
        thread1=DonwloadThread(category_list[int(choice)],1,2)
        thread2=DonwloadThread(category_list[int(choice)],2,3)
        thread3=DonwloadThread(category_list[int(choice)],3,4)
        thread4=DonwloadThread(category_list[int(choice)],4,5)
        thread5=DonwloadThread(category_list[int(choice)],5,6)
        thread6=DonwloadThread(category_list[int(choice)],6,7)
        thread7=DonwloadThread(category_list[int(choice)],7,8)
        thread8=DonwloadThread(category_list[int(choice)],8,9)
        thread9=DonwloadThread(category_list[int(choice)],9,10)
        thread10=DonwloadThread(category_list[int(choice)],10,11)
        thread11=DonwloadThread(category_list[int(choice)],11,12)
        thread12=DonwloadThread(category_list[int(choice)],12,13)
        thread13=DonwloadThread(category_list[int(choice)],13,14)
        thread14=DonwloadThread(category_list[int(choice)],14,15)
        thread15=DonwloadThread(category_list[int(choice)],15,16)
        thread16=DonwloadThread(category_list[int(choice)],16,17)
        thread17=DonwloadThread(category_list[int(choice)],17,18)
        thread18=DonwloadThread(category_list[int(choice)],18,19)
        thread19=DonwloadThread(category_list[int(choice)],19,20)
        thread20=DonwloadThread(category_list[int(choice)],20,21)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()
        thread10.start()
        thread11.start()
        thread12.start()
        thread13.start()
        thread14.start()
        thread15.start()
        thread16.start()
        thread17.start()
        thread18.start()
        thread19.start()
        thread20.start()


        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
        thread9.join()
        thread10.join()
        thread11.join()
        thread12.join()
        thread13.join()
        thread14.join()
        thread15.join()
        thread16.join()
        thread17.join()
        thread18.join()
        thread19.join()
        thread20.join()


category_list = ['All','anniversary-cards','apology-collection-cards','baby-cards',
                'better-like-buttons-cards','birthday-cards','breakup-cards','censored-cards',
                'college-cards','confession-cards','congratulations-cards','courtesy-hello-cards',
                'cry-for-help-cards','divorce-cards','drinking-cards','ecard-museum-cards','encouragement-cards',
                'family-cards','fantasy-sports-cards','farewell-cards','flirting-cards','friendship-cards','get-well-cards',
                'graduation-cards','honest-autocorrects-cards','honest-popups-cards','lgbt-cards','miss-you-cards','movies-cards',
                'pets-cards','pregnancy-cards','psas-cards','ransom-cards-cards','reminders-cards','seasonal-cards','sports-cards',
                'sympathy-cards','thanks-cards','thinking-of-you-cards','tv-cards','wedding-cards','weekend-cards','workplace-cards',
                'christmas-cards','kwanzaa-cards','new-years-cards','mlk-day-cards','chinese-new-year-cards','black-history-month-cards',
                'rake-cards','cougar-town-cards','dance-moms-cards','clorox-bleach-it-away-cards']

for i in range(0,53):
    print str(i)+"."+category_list[i]

choice = raw_input("Enter a choice")
if choice=="0":
    for x in range(5,53):
        thread_initialize(x)
elif int(choice)>=1 and int(choice)<=52:
        thread_initialize(choice)

else:
    print "Invalid choice"