import requests as requests
import time as time
from textblob import TextBlob
import pandas as pd
import numpy as np

url  = "http://theyfightcrime.org"
male= list()
female = list()

def webscrape(url):
        request = requests.get(url)
        text = request.text
        text = text.split('<P>')
        text = (text[1])
        text = text.split('.')

        male.append(text[0])
        female.append(text[1])
        
male = list()
female = list()
male1 = [line.strip() for line in open('male/male.txt', 'r')]
male2 = [line.strip() for line in open('male/male2.txt', 'r')]
male3 = [line.strip() for line in open('male/male3.txt', 'r')]
male4 = [line.strip() for line in open('male/male4.txt', 'r')]
male5 = [line.strip() for line in open('male/male5.txt', 'r')]
male6 = [line.strip() for line in open('male/male6.txt', 'r')]
male7 = [line.strip() for line in open('male/male7.txt', 'r')]
male8 = [line.strip() for line in open('male/male8.txt', 'r')]
male9 = [line.strip() for line in open('male/male9.txt', 'r')]
male10 = [line.strip() for line in open('male/male10.txt', 'r')]
male11 = [line.strip() for line in open('male/male11.txt', 'r')]
male12 = [line.strip() for line in open('male/male12.txt', 'r')]

female1 = [line.strip() for line in open('female/female.txt', 'r')]
female2 = [line.strip() for line in open('female/female2.txt', 'r')]
female3 = [line.strip() for line in open('female/female3.txt', 'r')]
female4 = [line.strip() for line in open('female/female4.txt', 'r')]
female5 = [line.strip() for line in open('female/female5.txt', 'r')]
female6 = [line.strip() for line in open('female/female6.txt', 'r')]
female7 = [line.strip() for line in open('female/female7.txt', 'r')]
female8 = [line.strip() for line in open('female/female8.txt', 'r')]
female9 = [line.strip() for line in open('female/female9.txt', 'r')]
female10 = [line.strip() for line in open('female/female10.txt', 'r')]
female11 = [line.strip() for line in open('female/female11.txt', 'r')]
female12 = [line.strip() for line in open('female/female12.txt', 'r')]

# Adding elements to male and female list
male = male1 + male2 + male3 + male4 + male5 + male6 + male7 + male8 + male9 + male10 + male11 + male12
female = female1 + female2 + female3 + female4 + female5 + female6 + female7 + female8 + female9 + female10 + female11 + female12
blobm = list()
sentiment_resultsm = list()
blobf = list()
sentiment_resultsf = list()

if __name__ == '__main__':
    count = 0
    while count < 50:
        webscrape(url)
        time.sleep(2)
        count += 1

    with open('male.txt', 'w') as m:
        for item in male:
            m.write("%s\n" % item)

    with open('female.txt', 'w') as f:
        for item in female:
            f.write("%s\n" % item)
            
            
            
    for i in (range(0, len(male))):  # Convert each element of the male list into a textblob
        blobm.append(TextBlob(male[i]))

    for i in range(0, len(blobm)):  # Sentiment analysis for each text blob
        sentiment_resultsm.append(blobm[i].sentiment.polarity)


    for i in (range(0, len(female))):  # Convert each element of the female list into a textblob
        blobf.append(TextBlob(female[i]))

    for i in range(0, len(blobf)):  # Sentiment analysis for each text blob
        sentiment_resultsf.append(blobf[i].sentiment.polarity)

    datam = pd.DataFrame()
    pd.set_option('display.max_colwidth',-1)
    datam['Hero'] = male
    datam['Sentiment Analysis'] = sentiment_resultsm
    sorted_datam = datam.sort_values('Sentiment Analysis')
    bottom_ten_male = sorted_datam.head(10)
    top_ten_male = sorted_datam.tail(10)

    dataf = pd.DataFrame()
    dataf['Hero'] = female
    dataf['Sentiment Analysis'] = sentiment_resultsf
    sorted_dataf = dataf.sort_values('Sentiment Analysis')
    bottom_ten_female = sorted_dataf.head(10)
    top_ten_female = sorted_dataf.tail(10)

    with open('top_ten_male.txt', 'w') as maletop:
        maletop.write(top_ten_male.to_string(header=False, index=False))

    with open('bottom_ten_male.txt', 'w') as malebottom:
        malebottom.write(bottom_ten_male.to_string(header=False, index=False))

    with open('top_ten_female.txt', 'w') as femaletop:
        femaletop.write(top_ten_female.to_string(header=False, index=False))

    with open('bottom_ten_female.txt', 'w') as femalebottom:
        femalebottom.write(bottom_ten_female.to_string(header=False, index=False))



#Finding 10 most common  descriptors

    blob = blobm + blobf     #Combine male and female characters
    adjectives = list()
    count = list()

    for i in range(0,len(blob)):
        for word,tag in blob[i].tags:
            if tag == 'JJ':
                adjectives.append(word.lemmatize())

    for i in range(0,len(adjectives)):
        count.append(adjectives.count(adjectives[i]))

    count_df = pd.DataFrame()
    count_df['Descriptor'] = adjectives
    count_df['Count'] = count

    sorted_count = count_df.sort_values('Count')
    top_ten_descriptors = (sorted_count.drop_duplicates().tail(10))

    with open('Top_ten_descriptors.txt', 'w') as descriptors:
        descriptors.write(top_ten_descriptors.to_string(header=False, index=False))
