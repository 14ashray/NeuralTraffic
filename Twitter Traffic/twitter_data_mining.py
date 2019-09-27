# import json
# import tweepy
# from elasticsearch import Elasticsearch
# import requests
# import re

# ACCESS_TOKEN = '884807193416970240-iipYmqXRTLWeINirrO2ztFujWvO7J34'
# ACCESS_SECRET = 'HEnMWGtzVWDektEoCM0GFuPNFufp2pwFYt62EYRrtsTPG'
# CONSUMER_KEY = 'qkc83TiYHX5HRsnFi7zlrIEuq'
# CONSUMER_SECRET = 'o4mtJ2LsaXpbLkV8gPRxhAXHdGDqjFcOAG9L22FW04KJXmppO2'


# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search,
#                            q=["traffic infosys"],
#                            rpp=10,
#                            result_type="recent",
#                            include_entities=True,
#                            lang="en").items():
#     # print(tweet.text)
    

#     if tweet.place != None:
#     	print (tweet.place.bounding_box.coordinates)
#     	print (tweet.text)
#     	break


    # processed_String = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\ART )", "", tweet.text).split())
    # processed_String = ' '.join(processed_String.split('\n'))
    # doc = {
    #     'text': processed_String,
    #     'timestamp': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    #     'location' : tweet.coordinates
    # }
    # print(doc)
    # print ()



# import sys
# import tweepy

# consumer_key="qkc83TiYHX5HRsnFi7zlrIEuq"
# consumer_secret="o4mtJ2LsaXpbLkV8gPRxhAXHdGDqjFcOAG9L22FW04KJXmppO2"
# access_key="884807193416970240-iipYmqXRTLWeINirrO2ztFujWvO7J34"
# access_secret="HEnMWGtzVWDektEoCM0GFuPNFufp2pwFYt62EYRrtsTPG"

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)



# class CustomStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         # if 'traffic' in status.text.lower():
#         #     print (status.text)
#         # elif  'jam' in status.text.lower():
#         # 	print (status.text)
#         # elif 'accident' in status.text.lower():
#         # 	print (status.text)
#         # elif 'roadblock' in status.text.lower():
#         # 	print (status.text)
#        	print (status)
       	


#     def on_error(self, status_code):
#         print >> sys.stderr, 'Encountered error with status code:', status_code
#         return True # Don't kill the stream

#     def on_timeout(self):
#         print >> sys.stderr, 'Timeout...'
#         return True # Don't kill the stream

# sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
# sapi.filter(locations=[77.050125,28.477282,77.393105,28.758771])


# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import tweepy




# class TwitterStreamListener(tweepy.StreamListener):
#     """ A listener handles tweets are the received from the stream.
#     This is a basic listener that just prints received tweets to stdout.
#     """

#     def on_status(self, status):
#         self.get_tweet(status)

#     def on_error(self, status_code):
#         if status_code == 403:
#             print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
#             return False

#     @staticmethod
#     def get_tweet(tweet):

#         if tweet.coordinates is not None:
#             x, y = map(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
#             map.plot(x, y, 'ro', markersize=2)
#             plt.draw()


# if __name__ == '__main__':

#     # Size of the map
#     fig = plt.figure(figsize=(18, 4), dpi=250)

#     # Set a title
#     plt.title("Tweet's around the world")

#     # Declare map projection, size and resolution
#     map = Basemap(projection='merc',
#                   llcrnrlat=-80,
#                   urcrnrlat=80,
#                   llcrnrlon=-180,
#                   urcrnrlon=180,
#                   lat_ts=20,
#                   resolution='l')

#     map.bluemarble(scale=0.3)

#     # Set interactive mode ON
#     plt.ion()

#     # Display map
#     plt.show()

#     # Get access and key from another class
    
#     consumer_key = "qkc83TiYHX5HRsnFi7zlrIEuq"
#     consumer_secret = "o4mtJ2LsaXpbLkV8gPRxhAXHdGDqjFcOAG9L22FW04KJXmppO2"

#     access_token = "884807193416970240-iipYmqXRTLWeINirrO2ztFujWvO7J34"
#     access_token_secret = "HEnMWGtzVWDektEoCM0GFuPNFufp2pwFYt62EYRrtsTPG"

#     # Authentication
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.secure = True
#     auth.set_access_token(access_token, access_token_secret)

#     api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
#                      retry_errors=5)

#     streamListener = TwitterStreamListener()
#     myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

#     myStream.filter(locations=[-180, -90, 180, 90])



import sys
import tweepy
import json

consumer_key="qkc83TiYHX5HRsnFi7zlrIEuq"
consumer_secret="o4mtJ2LsaXpbLkV8gPRxhAXHdGDqjFcOAG9L22FW04KJXmppO2"
access_key = "884807193416970240-iipYmqXRTLWeINirrO2ztFujWvO7J34"
access_secret = "HEnMWGtzVWDektEoCM0GFuPNFufp2pwFYt62EYRrtsTPG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
### keywords for the public stream
keyword = "traffic infosys"
### initialize blank list to contain tweets
tweets = []
### file name that you want to open is the second argument
# f = open('today.txt', 'a')

class CustomStreamListener(tweepy.StreamListener):
    global tweets
    def on_status(self, status):
        ### info that you want to capture
        info = status.id, status.text, status.created_at, status.place, status.user, status.in_reply_to_screen_name, status.in_reply_to_status_id 
        
        if keyword in status.text.lower():
            print status.text
            print status.place.bounding_box.coordinates
                # # this is for writing the tweets into the txt file
                # f.write(str(info))
                # try:
                #     tweets.append(info)
                # except:
                #     pass


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

### filter for location
# locations should be a pair of longtitude and latitude pairs, with the southwest corner
# of the bounding box coming first
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[75.9252,30.3852,77.7902,31.1222])