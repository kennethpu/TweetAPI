from tweetStorage import *
from tweetCrawler import TweetCrawler

# AUTHENTICATION CONSTANTS (SHOULD USE YOUR OWN, DO NOT EXPOSE PUBLICLY)
CONSUMER_KEY = "XXXX"
CONSUMER_SECRET = "XXXX"
ACCESS_TOKEN = "XXXX"
ACCESS_SECRET = "XXXX"

# TWITTER SCREEN NAMES
WWF_SN = "wordswfriends"
TRC_SN = "triviacrack"
CCS_SN = "candycrushsaga"


class TweetAPI:
    """
    Simple API for fetching information about Twitter followers
    """
    def __init__(self):
        """Initializes an instance of TweetAPI"""
        self.crawler = TweetCrawler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    def getFollowerIDs(self, screen_name, should_save=True):
        """Fetches a list of follower ids for a specified twitter user, from file if cached locally, otherwise from network

        Arguments:
          screen_name -- the screen name of the specified twitter user
          should_save -- True if data loaded from network should be written to a file

        Returns:
          follower_ids -- list of ids for all users following the specified twitter screen name
        """
        file_name = screen_name + '_ids.txt'
        try:
            print "Trying to load follower ids for %s from file..." % screen_name
            return loadFollowerIDsFromFile(file_name)
        except IOError:
            print "Unable to load from file (%s), trying to load follower ids for from network..." % file_name
            follower_ids = self.crawler.getFollowerIDs(screen_name)
            if should_save:
                print "Saving follower ids to file (%s)..." % file_name
                saveFollowerIDsToFile(follower_ids, file_name)
            return follower_ids

    def getFollowersData(self, screen_name, should_save=True):
        """Fetches a dictionary of follower ids mapped to JSON data, from file if cached locally, otherwise from network

        Arguments:
          screen_name -- the screen name of the specified twitter user
          should_save -- True if data loaded from network should be written to a file

        Returns:
          followers_data -- dictionary mapping follower ids to JSON data
        """
        file_name = screen_name + '_data.txt'
        try:
            print "Trying to load followers data for %s from file..." % screen_name
            return loadFollowersDataFromFile(file_name)
        except IOError:
            print "Unable to load from file (%s), trying to load followers data for from network..." % file_name
            follower_ids = self.getFollowerIDs(screen_name)
            followers_data = self.crawler.getFollowersData(follower_ids)
            if should_save:
                print "Saving followers data to file (%s)..." % file_name
                saveFollowersDataToFile(followers_data, file_name)
            return followers_data


def main():
    api = TweetAPI()
    api.getFollowerIDs('angrybirds')
    # wwf_followers = set(api.getFollowerIDs(WWF_SN))
    # ccs_followers = set(api.getFollowerIDs(CCS_SN))
    # trc_followers = set(api.getFollowerIDs(TRC_SN))

    # WWF_CCS_followers = wwf_followers & ccs_followers
    # WWF_TRC_followers = wwf_followers & trc_followers
    # CCS_TRC_followers = ccs_followers & trc_followers
    # shared_followers = WWF_CCS_followers & trc_followers

    # print "WWF:%d, CCS:%d, TRC:%d, WWF+CCS:%d, WWF+TRC:%d, CCS+TRC:%d ALL:%d" % \
    # 	(len(wwf_followers), len(ccs_followers), len(trc_followers), len(WWF_CCS_followers), len(WWF_TRC_followers), len(CCS_TRC_followers), len(shared_followers))

if __name__ == '__main__':
    main()
