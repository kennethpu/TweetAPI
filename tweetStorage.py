import json


def loadFollowerIDsFromFile(in_file_name):
	"""Loads a list of follower ids from a specified text file

    Arguments:
      in_file_name -- file name (including txt extension) that follower_ids is contained in

    Returns:
      follower_ids -- list of ids for all users following the specified twitter screen name
    """
	follower_ids = []
	for line in open(in_file_name):
		follower_ids.append(int(line.strip()))
	return follower_ids

def saveFollowerIDsToFile(follower_ids, out_file_name):    
	"""Saves a list of follower ids to a specified text file

    Arguments:
       follower_ids -- list of ids for all users following the specified twitter screen name
      out_file_name -- file name (including txt extension) that follower_ids should be written to (PRE-EXISTING FILES WILL BE OVERWRITTEN)
    """
	out_file = open(out_file_name,'w')
	for follower_id in follower_ids:
		out_file.write('%d\n' % follower_id)
	out_file.close()

def loadFollowersDataFromFile(in_file_name):
	"""Loads dictionary of follower ids mapped to follower JSON data from a specified text file

    Arguments:
      in_file_name -- file name (including txt extension) that follower JSON data is contained in

    Returns:
	  followers_data -- dictionary mapping follower ids to JSON data for the specified follower ids
    """
	with open(in_file_name,'r') as in_file:
		return json.load(in_file)

def saveFollowersDataToFile(followers_data, out_file_name):    
	"""Saves dictionary of follower ids mapped to follower JSON data to a specified text file

    Arguments:
	  followers_data -- dictionary mapping follower ids to JSON data for the specified follower ids
       out_file_name -- file name (including txt extension) that follower JSON data should be written to (PRE-EXISTING FILES WILL BE OVERWRITTEN)
    """
	with open(out_file_name,'w') as out_file:
		json.dump(followers_data, out_file)
