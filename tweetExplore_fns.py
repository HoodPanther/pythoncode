def extract_tweets(data):
    """Returns list of tweets that contain text"""
    tweet_list = []
    for index, val in enumerate(data):
        curtweet = data[index]
        if "text" in curtweet:
            if curtweet["text"] == None:
                x = 1
            else:
                tweet_list.append(curtweet)
    return tweet_list

def cool_fn():
    print("hey this is cool")


def extract_tweets_fieldOfInterest(data, interest_field):
	"""Returns tweets that contain a value within the specified field of interest"""
	tweet_list = []	
	for index, val in enumerate(data):
		curtweet = data[index]
		if interest_field in curtweet:
			if curtweet[interest_field] == None:
				x = 1
			else:
				tweet_list.append(curtweet)
	return tweet_list



def extract_indices(data, interest_field):
	"""Returns indices for tweets that contain a value within the specified field of interest"""
	item_index = []	
	for index, val in enumerate(data):
		curtweet = data[index]
		if interest_field in curtweet:
			if curtweet[interest_field] == None:
				x = 1
			else:
				item_index.append(index)
	return item_index
