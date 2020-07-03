import tweepy


# Authenticate to Twitter
consumer_key = '4Bl3owbajQrQCPETbYCAgdPAh'
consumer_secret = 'FUJgpvCKfVTdPYt2gS2TO5EqmQ7HLZxxtMK4NYGKHGWhmAGCTb'
access_token = '2369703763-diEYZtGytZ0YZcIMD6GXe6ImRg8IMBJHtGa4gz5'
access_token_secret = 'Ugxt5wsnDsRYYizclaTIUXkpN1fZDiWOhPe6L1kIVlpeQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create API object
for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
    except:
        pass
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
api.update_status(":pizza: + :beer: = good vibes")



