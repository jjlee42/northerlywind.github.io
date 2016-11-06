
# coding: utf-8

# In[ ]:

get_ipython().system('pip install tweepy')


# In[ ]:

get_ipython().system('pip install nltk')


# In[3]:

get_ipython().system('pip install vaderSentiment')


# In[1]:

from nltk import *


# In[13]:

from vaderSentiment.vaderSentiment import sentiment as sentiment


# In[ ]:

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


# In[ ]:

import tweepy


# In[ ]:

ACCESS_TOKEN = '2245810146-os7gvZ3pRNg841BPCp0owl0UoAxNfpKWxmcN2VJ'
ACCESS_SECRET = 'tiuJmQqzjr0SoybM8WihIewkqACxTCX8hXwFpjoYMPGSC'
CONSUMER_KEY = '8pd19OaqgxaF7sjISdWuYoXQi'
CONSUMER_SECRET = 'tYcaTHMYYPtgMaFKCVPWddVUVgakQQvyRYQN4WLXZnCDb8gDsl'


# In[ ]:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


# In[ ]:

tweets = api.search(q="#MakeStuffBetter")

for t in tweets:
    print(t.text)


# In[ ]:

nltk.download()


# In[ ]:

nltk.sentiment.vader.SentiText(t.text[0])


# In[ ]:



