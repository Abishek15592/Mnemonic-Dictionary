#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import urllib
import re
import csv

replace_word = "http://www.mnemonicdictionary.com/?word=%REPLACEWORD%"
# output = csv.writer(open("mnemonic.csv", "wb"),delimiter='\t', quoting=csv.QUOTE_NONE, quotechar='"',escapechar=' ')

while True:
    word = raw_input("Enter the word : ")
    global flag
    flag = 0
    url = replace_word
    word = word.strip(" ")
    word = word.strip("\n")
    print ("\n")
    url = url.replace("%REPLACEWORD%", word)
    url = url.replace(" ","+")
    url = url.replace("'","%27")

    #download the URL and extract the content to the variable html
    request = requests.get(url)
    #pass the HTML to Beautifulsoup.
    soup = BeautifulSoup(request.text,'html.parser')

    #Scraps the Definition part of the site
    data = soup.find('div' , {'class' : 'media-body'})

    #Finds the word searched
    word_name = data.find('h1')
    print "------>",word_name.text,"<------"

    #Used to extract the definition,synonyms and example sentence from the site

    if(data.find('div' , {'style' : 'padding-bottom:0px;'})):
        word_def = data.find('div' , {'style' : 'padding-bottom:0px;'}).text.strip().split('\n')
        for i in range(0,len(word_def)):
            if(word_def[i]!=""):
                print(word_def[i])

        #Scraps the mnemonic part of the site
        hello = soup.find('div' , {'class' : 'mnemonics-slides'})
        if (hello):
            mnemonics = hello.find_all('p' , {'class' : ''})
            print "\n\nMnemonics:"
            print mnemonics[0].text.strip() ,"\n"
        else:
            print "\n\nNo Mnemonics\n"
    else:
        print "\n\nWrong word.Please check the spelling or enter the correct word.\n"


        # #Extracts the top 3 mnemonics from the site
        # mnemonics = hello.find_all('p' , {'class' : ''})
        # if (mnemonics):
        #     print "\n\nMnemonics:"
        #     print mnemonics[0].text.strip() ,"\n"
        # else:
        #     print "No Mnemonics"

        # output.writerow([word_name.text,"-----",temp,"",mnemonics[0].text.strip() ,"\n\n",mnemonics[1].text.strip() ,"\n\n" ,mnemonics[2].text.strip()])
