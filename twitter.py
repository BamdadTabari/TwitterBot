# yes you need api key here, too
import tweepy

# Keys
consumer_key = "consumer key"
consumer_secret = "consumer secret"
access_token = "your access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

tweepy.API
tweepy.API.add_list_member()
tweepy.API.available_trends()
tweepy.API.chunked_upload_append()
tweepy.API # + more and more

tweepy.AppAuthHandler
tweepy.AppAuthHandler.apply_auth()

tweepy.BadRequest
tweepy.BadRequest.with_traceback()

tweepy.Client
tweepy.Client.block()
tweepy.Client.add_list_member
tweepy.Client.create_tweet()
tweepy.Client.delete_tweet()
tweepy.Client # +++++++++ co

tweepy.Cursor
tweepy.Cursor.pages()

tweepy.DIRECT_MESSAGE_EVENT_FIELDS
tweepy.DM_EVENT_FIELDS
tweepy.Forbidden.add_note()


tweepy.OAuth1UserHandler.get_access_token()
tweepy.OAuth2UserHandler.authorization_url()
tweepy.OAuth2BearerHandler
tweepy.OAuth2AppHandler

#wtf 
# this library not gonna end at all
# wanna see?  just look at the docs

# 
# Uncle Bamdad