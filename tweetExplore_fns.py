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

def extract_tweets_interest_field(data, interest_field):
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


def extract_sentiment(tweet_list,person):
    """ Returns the sentiment rating of each tweet, and indices for the tweets """
    from textblob import TextBlob
    import numpy as np
    person_sentiment_polarity = []
    person_tweetInd = []
    person_sentiment_subjectivity = []
    # for each tweet
    for tweet,val in enumerate(tweet_list):
        curText = tweet_list[tweet]['text']
        cur_blob = TextBlob(curText)
        # check that the tweet contains mention of candidate
        if cur_blob.words.count(person):
            cur_sentiment = cur_blob.sentiment
            # save sentiment polarity and subjectivity
            person_sentiment_polarity.append(cur_sentiment[0])
            person_sentiment_subjectivity.append(cur_sentiment[1])
            # save tweet index
            person_tweetInd.append(tweet)
        else:
            x = 1
    print(person, '  # tweets:',len(person_tweetInd))
    return person_sentiment_polarity, person_sentiment_subjectivity, person_tweetInd

def sort_tweets_pos_neg(iperson, polarity_store, tweet_index_store, tweet_list):
    """sorts tweets for given candidate by positive or negative sentiment, and creates/returns
        lists of indices, sentiment values, and texts for tweets in the two categories. Scores of 0 are ignored """
    pos_polarity = []
    ind_pos_polarity = []
    tweet_pos_polarity = []
    neg_polarity = []
    ind_neg_polarity = []
    tweet_neg_polarity = []
    # get sentiment scores for this candidate
    current_polarity = polarity_store[iperson]
    # get the indices for the tweets about this candidate
    current_indices = tweet_index_store[iperson]
    # for each sentiment value
    for iscore,sentiment in enumerate(current_polarity):
        curindex = current_indices[iscore]
        # select positive sentiments
        if sentiment > 0: 
            # store sentiment and index
            pos_polarity.append(sentiment)
            ind_pos_polarity.append(curindex)
            #get tweet text for current sentiment
            tweet_pos_polarity.append(tweet_list[curindex]['text'])
        # or negative sentiments
        elif sentiment < 0:
            #store sentiment and index
            neg_polarity.append(sentiment)
            ind_neg_polarity.append(curindex)
            #get tweet text for current sentiment
            tweet_neg_polarity.append(tweet_list[curindex]['text'])
    
    return pos_polarity, neg_polarity, ind_pos_polarity, ind_neg_polarity, tweet_pos_polarity, tweet_neg_polarity



def autolabel_int(rects,ax,axNum,vals):
    """attach labels to bars, integers"""
    i = 0
    for rect in rects:
        height = rect.get_height()
        if vals[i] > 0:
            ax[axNum].text(rect.get_x() + rect.get_width()/2., height+.03,
                '%d' % int(height),
                ha='center', va='bottom')
        else:
            ax[axNum].text(rect.get_x() + rect.get_width()/2., -1*(height+.1),
                '%d' % int(height),
                ha='center', va='bottom')
        i = i + 1

def autolabel_dec(rects,ax,axNum,vals):
    """attach labels to bars, 3 decimals"""
    i = 0
    for rect in rects:
        height = rect.get_height()
        if vals[i] > 0:
            ax[axNum].text(rect.get_x() + rect.get_width()/2., height+.03,
                '%0.3f' % height,
                ha='center', va='bottom')
        else:
            ax[axNum].text(rect.get_x() + rect.get_width()/2., -1*(height+.1),
                '%0.3f' % height,
                ha='center', va='bottom')
        i = i + 1


def rival_count(rival_list,current_inds, candidates, tweet_list):
    """extract counts and indices of tweets that mention more than one candidate"""
    from textblob import TextBlob
    count = [0]*len(candidates)
    rival_index_temp = []
    # for each potential rival 
    for irival, rival in enumerate(rival_list):
        cur_rival_index = []
        cur_rival = candidates[rival]
        # for each tweet about the candidate
        for iind,textval in enumerate(current_inds):
            curidx = current_inds[iind]
            curtweet = tweet_list[curidx]["text"]
            curblob = TextBlob(curtweet)
            if curblob.words.count(cur_rival):
                count[rival] = count[rival] + 1
                cur_rival_index.append(current_inds[iind])
        rival_index_temp.append(cur_rival_index)
    return rival_index_temp, count



