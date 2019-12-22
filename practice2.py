import sys
import tweepy
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import csv
import os
from matplotlib import pyplot as plt
import numpy as np

bollywood_vocab = ['3-idiots', 'Slumdog Millionaire', 'popular', 'bollywood', 'indian', 'star', 'movie', 'bombay',
'hindi', 'flim',  'musical', 'concert', 'dance', 'fantasy', 'tragedy', 'love', 'integrated', 'choreography', 'love triangle',
'eternal', 'triangle', 'triangular relation', 'make', 'love triangle',  'fancy' , 'showy',  'formal', 'splendid', 'colorful' ,
'unusual' , 'distinctive', 'unique', 'peculiar', 'desire', 'appetite', 'craving', 'ambition', 'Mumbai', 'overdo', 'exaggerate',
'universal', 'studio', 'vintage', 'blockbuster', 'tradition', 'custom', 'music', 'actor']

consumer_key = 'vg9ULXEzT0AyYLp18vflpTVA1'
consumer_secret = 'FgqssSLMfUKAhVlP3eBuQMEim3LYs4i0yMAIauh6yyQRSyvpDk'

access_token = '1207342041161580544-5IJrX0OF9RGj6jSrXoa98CyjWoRYCy'
access_token_secret = 'Pub6yJTQp07MLjzr5bQ8kprPIGXvRWJrlDDKKwjAyDDkH'

# perform authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create our twitter api to access tweets from it
api = tweepy.API(auth)
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QLabel



d = {}
for v in bollywood_vocab:
    v = v.lower()
    d[v] = True
bollywood_features = [(d, 'bollywood')]

bollywood_features2 = []
for v in bollywood_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    bollywood_features2.append((d, 'bollywood'))


date_vocab = ['sweet', 'pleasure', 'joy', 'happy', 'delighted', 'couple', 'love', 'date', 'boyfriend', 'girlfriend', 'propose',
'kiss', 'emotion', 'devotion', 'sweetheart', 'beau', 'partner', 'go out', 'get along', 'get close', 'associate with', 'go around', 'marriage',
'wedding',  'romnce', 'woo', 'tempt', 'wheedle', 'entice', 'lure']

d = {}
for v in date_vocab:
    v = v.lower()
    d[v] = True
date_features = [(d, 'date')]

date_features2 = []
for v in date_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    date_features2.append((d, 'date'))

animation_vocab = ['childish', 'sophomoric', 'childlike', 'naive', 'youthful', 'adolescent', 'boyish', 'enthusiastic',
'girlish', 'inexperienced', 'underage', 'young', 'youth', 'animation' ]

d = {}
for v in animation_vocab:
    v = v.lower()
    d[v] = True
animation_features = [(d, 'animation')]

animation_features2 = []
for v in animation_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    animation_features2.append((d, 'animation'))

friend_vocab = ['acquaintance', 'companion', 'mate', 'partner', 'associate', 'classmate', 'buddy', 'partner', 'familiar', 'intimate',
'soul matem', 'bosom buddy', 'schoolmate', 'playmate', 'spare', 'trust', 'confidence', 'expectation', 'faith', 'hope',
'assurance', 'certainty', 'certitude', 'conviction',  'positiveness', 'reliance', 'stock', 'store', 'entrustment', 'gospe', 'truth',
'acceptance' ,'assumption' ,'conclusion' ,'confidence' ,'conviction' , 'faith' ,'feeling' ,'hope' ,'idea' ,'judgment',
'knowledge' ,'notion' ,'opinion' ,'position' ,'suspicion' ,'theory' ,'thinking' ,'trust' ,'understanding' ,'view']

d = {}
for v in friend_vocab:
    v = v.lower()
    d[v] = True
friend_features = [(d, 'friend')]

friend_features2 = []
for v in friend_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    friend_features2.append((d, 'friend'))
interesting_vocab = ['scary', 'creepy', 'alarming', 'eerie', 'intimidating', 'chilling', 'hairy', 'shocking',
'creepy', 'horrifying', 'spocky', 'stuffy', 'be chocked', 'stuffy', 'be suffocated', 'be stifled',
'daunt', 'frighten', 'petrify', 'terrify', 'sicken', 'outrage', 'disgust', 'appall', 'dismay', 'stun',
'overwhelm', 'absorbing', 'interesting', 'ascinating']

d = {}
for v in interesting_vocab:
    v = v.lower()
    d[v] = True
interesting_features = [(d, 'interesting')]

interesting_features2 = []
for v in interesting_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    interesting_features2.append((d, 'interesting'))

old_vocab = ['old', 'classic', 'typical', 'usual', 'ancient', 'aged', 'decrepit', 'elderly', 'gray', 'mature', 'tried',
'venerable', 'fossil', 'senior', 'elder', 'common', 'exemplary', 'normal', 'regular', 'smbolic',
'archaic', 'hoary', 'old-fashioned', 'timeworn', 'antique', 'antediluvian', 'oldie', 'relic', 'antiqueated', 'primal']

d = {}
for v in old_vocab:
    v = v.lower()
    d[v] = True
old_features = [(d, 'old')]

old_features2 = []
for v in old_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    old_features2.append((d, 'old'))

rainy_vocab = ['drizzly', 'stormy', 'wet', 'coastal', 'showery', 'rainy outside', 'sad', 'sad ending', 'depressed', 'melachony', 'gloomy', 'low', 'blue',
'despondent', 'morose', 'pessimistic', 'sad', 'unhappy', 'down', 'weeping', 'dragged', 'bitter', 'dismal', 'heartbroken', 'mournful'
'sorrowful', 'sorry', 'wistful', 'doleful', 'cloudy', 'dim', 'dejection', 'depression', 'miserable']

d = {}
for v in rainy_vocab:
    v = v.lower()
    d[v] = True
rainy_features = [(d, 'rainy')]

rainy_features2 = []
for v in rainy_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    rainy_features2.append((d, 'rainy'))

alone_vocab = ['only', 'unattended', 'solo', 'unaccompanied', 'abandoned', 'by itself', 'by oneself', 'companionless', 'deserted', 'desolate', 'detached',
'forlorn', 'forsaken', 'friendless', 'hermit', 'in solitary', 'individual', 'isolated', 'lone', 'lonely', 'lonesome', 'onliest', 'shag', 'single', 'sole', 'solitary', 'stag',
'traveling light', 'unaided', 'unassisted', 'unattached', 'unescorted', 'unmarried', 'widowed', 'solitude',  'part', 'lonesomeness', 'alone']

d = {}
for v in alone_vocab:
    v = v.lower()
    d[v] = True
alone_features = [(d, 'alone')]

alone_features2 = []
for v in alone_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    alone_features2.append((d, 'alone'))

didactic_vocab = ['didactic', 'academic', 'advisory', 'donnish', 'edifying', 'enlightening', 'moral',
'homiletic', 'expository', 'exhortative', 'hortative', 'instructive', 'collegiate', 'scholastic',
'scholarly', 'intellectual', 'cerebral highbrow', 'thoughtful', 'studious', 'inventive', 'bookish',
'phrenic', 'learned', 'educational', 'cultural', 'informational', 'instructive', 'helpful', 'illuminating']

d = {}
for v in didactic_vocab:
    v = v.lower()
    d[v] = True
didactic_features = [(d, 'didactic')]

didactic_features2 = []
for v in didactic_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    didactic_features2.append((d, 'didactic'))

ost_vocab = ['ost', 'music', 'B-side', 'track', 'drama', 'movie music', 'movie album', 'sound stripe']

d = {}
for v in ost_vocab:
    v = v.lower()
    d[v] = True
ost_features = [(d, 'ost')]

ost_features2 = []
for v in ost_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    ost_features2.append((d, 'ost'))

villain_vocab = ['villain', 'antihero', 'criminal', 'devil', 'scoundrel', 'sinner', 'blackguard', 'creep', 'evildoer',
'offender', 'sinner', 'scoundrel', 'miscreant', 'crime', 'calamity', 'catastrophe', 'corruption',
'harm', 'hatred', 'pain', 'sin', 'suffering', 'sorrow', 'injury', 'breach', 'atrocity', 'evil', 'violation',
'midsdeed', 'felony']

d = {}
for v in villain_vocab:
    v = v.lower()
    d[v] = True
villain_features = [(d, 'villain')]

villain_features2 = []
for v in villain_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    villain_features2.append((d, 'villain'))

heroes_vocab = ['iron man', 'captain america', 'captain marve', 'hulk', 'black widow', 'thor', 'Gtoot rocket', 'war machine',
'Dr. strange', 'nubula', 'roki', 'valkyrie', 'ant man', 'black panther',
'Bucky Barnes', 'wasp', 'Drax', 'star lord', 'ancient one', 'mantis',
'Falcon', 'spider man', 'scarlet', 'witch', 'Hawkeye']

d = {}
for v in heroes_vocab:
    v = v.lower()
    d[v] = True
heroes_features = [(d, 'heroes')]

heroes_features2 = []
for v in heroes_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    heroes_features2.append((d, 'heroes'))

family_vocab = ['family', 'love', 'lovely', 'clan', 'folk', 'group', 'house', 'household', 'people', 'tribe', 'ancestors', 'ancestry', 'birth', 'blood', 'brood',
'children', 'class', 'descendants', 'descent', 'dynasty', 'extraction', 'forebears', 'kind', 'kindred', 'band']

d = {}
for v in family_vocab:
    v = v.lower()
    d[v] = True
family_features = [(d, 'family')]

family_features2 = []
for v in family_vocab:
    v = v.lower()
    d = {}
    for a in v:
        d[a] = True
    family_features2.append((d, 'family'))

# 단어단위로 -> 없는단어 판단못함 죄다 빌런행;
trainset = family_features + heroes_features + villain_features + ost_features + didactic_features + alone_features + \
           friend_features + interesting_features + old_features + rainy_features + bollywood_features + \
           date_features + animation_features

# 교수님의방법 알파벳단위로 -> 정확하지않음
trainset2 = family_features2 + heroes_features2 + villain_features2 + ost_features2 + didactic_features2 + alone_features2 + \
            friend_features2 + interesting_features2 + old_features2 + rainy_features2 + bollywood_features2 + \
            date_features2 + animation_features2

features = ['family', 'heroes', 'villain', 'ost', 'didactic', 'alone', 'friend', 'interesting', 'old',
            'rainy', 'bollywood', 'date', 'animation']

classifier = NaiveBayesClassifier.train(trainset2)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('search', self)
        self.btn.move(10, 10)
        self.btn.resize(400,30)
        self.btn.clicked.connect(self.showDialog) # 이걸 합쳤네 잘했네 *^^*


        self.la = QLabel('', self)
        self.la.move(10, 60)
        self.la.resize(900,100)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'search your movie', 'Enter movie title:')

        def f(keyword, cnt):
            tweets = tweepy.Cursor(api.search,
                                   q=keyword,
                                   lang='en').items(cnt)
            arr = []
            for t in tweets: # 세뇌교육 완료.
                arr.append(t.text)
            return arr

        tweets = f(text, 30)

        dd = {}
        for a in features:
            dd[a] = 0


        for t in tweets:
            for w in t:
                dd[classifier.classify({w: True})] += 1


        print(dd)
        if ok:
            plt.figure(figsize=(12, 3))
            plt.bar(features, dd.values())
            # self.la.setText(str(plt))
            plt.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

