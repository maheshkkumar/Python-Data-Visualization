from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

'''
Change the values of the next four variables, by your access and consumer values from twitter
'''
access_token = "XXXXXXXXXX"
access_token_secret = "XXXXXXXXXX"
consumer_key = "XXXXXXXXXX"
consumer_secret = "XXXXXXXXXX"

class StdOutListener(StreamListener):

	def on_data(self, data):
		print(data)
		return True

	def on_error(self, status):
		print status


if __name__ == '__main__':
	listener = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, listener)

	stream.filter(track=['python', 'javascript', 'ruby'])