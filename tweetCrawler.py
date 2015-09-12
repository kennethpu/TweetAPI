import tweepy


class TweetCrawler:
	"""
	Dedicated class for making network fetch requests to Twitter
	"""
	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
		"""Initializes an instance of TweetCrawler"""
		self.api = self.getAPI(consumer_key, consumer_secret, access_token, access_token_secret)

	def getAPI(self, consumer_key, consumer_secret, access_token, access_token_secret):
		"""Gets an authenticated wrapper class that will provide access to Twitter RESTful API"""
		# Authenticate
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	def getFollowerIDs(self, screen_name):
		"""Fetches a list of follower ids for a specified twitter user

	    Arguments:
	      screen_name -- the screen name of the specified twitter user
	    
	    Returns:
	      follower_ids -- list of ids for all users following the specified twitter screen name
	    """
		follower_ids = []
		for follower_id in tweepy.Cursor(self.api.followers_ids,id=screen_name).items():
			print follower_id
			follower_ids.append(follower_id)
		return follower_ids

	def getFollowersData(self, follower_ids):    
		"""Fetches user JSON data for a list of follower ids and returns the data as a dictionary

	    Arguments:
	      follower_ids -- list of ids for all users following the specified twitter screen name
	    
	    Returns:
	      followers_data -- dictionary mapping follower ids to JSON data for the specified follower ids
	    """
	    # Split follower ids into batches of 100 so that we can make batched calls
		fid_batches = [follower_ids[x:x+100] for x in xrange(0,len(follower_ids),100)]

		followers_data = {}
		tot_batch = len(fid_batches)
		cur_batch = 0
		for batch in fid_batches:
			cur_batch += 1
			print "Processing batch...%d/%d" % (cur_batch,tot_batch)
			followers = self.getBatchedUsersJSON(batch)
			for follower in followers:
				follower_id = follower['id_str']
				followers_data[follower_id] = follower
		return followers_data

	def getUserJSON(self, u_id):
		"""Fetches JSON data for a single specified user

	    Arguments:
	      u_id -- the user id of the specified twitter user
	    
	    Returns:
	      user_json -- JSON data for the specified user
	    """
		return self.api.get_user(user_id=u_id)._json

	def getBatchedUsersJSON(self, u_ids):
		"""Fetches JSON data for a batch of specified users

	    Arguments:
	      u_ids -- list of user ids of specified twitter users
	    
	    Returns:
	      users_json -- JSON data for the specified users
	    """
		users = self.api.lookup_users(user_ids=[','.join([str(x) for x in u_ids])])
		return [user._json for user in users]
