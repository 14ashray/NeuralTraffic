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


class CustomStreamListener(tweepy.StreamListener):
    global tweets
    def on_status(self, status):
        ### info that you want to capture
        info = status.id, status.text, status.created_at, status.place, status.user, status.in_reply_to_screen_name, status.in_reply_to_status_id 
        
        if keyword in status.text.lower():
            a =  status.text
            b =  status.place.bounding_box.coordinates
            data = {}
            data['tweets'] = []
            data['tweets'].append({
                    'tweet': a,
                    'location': b
            })

            r = requests.post({url = "https://api.myjson.com/bins",data:data})

            print(r)
            break


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

