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


def extract_sentiment(tweet_list,person):
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

def sortTweetsPosNeg(iperson, polarity_store, tweet_index_store, tweet_list):
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



def makeWordcloud(tweetList):
    """ Joins tweet list into single string, removes stop words and RT, then generates word cloud """
    from wordcloud import WordCloud, STOPWORDS
    newSTOP = STOPWORDS
    newlist = []
    for itweet,val in enumerate(tweetList):
        curtweet = tweetList[itweet]
        curtweet.replace('RT','')
        newlist.append(curtweet)
        
    # add stopwords to exclude from wordcloud - 
    newSTOP.update(('co','https','t','\'RT','R','T','RT ','RT@'))
    joinedTexts = " ".join(str(x) for x in newlist)
    setattr(WordCloud,"setfont",'/anaconda/envs/eq_env/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf')
    # font_path='/anaconda/envs/eq_env/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf',

    #generate wordcloud
    wordcloud = WordCloud(stopwords=newSTOP,
                              background_color='black',
                              width=1700,
                              height=1400
                             ).generate(joinedTexts)
    return wordcloud 



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


def autolabelInt(rects,ax,axNum,vals):
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

def autolabelDec(rects,ax,axNum,vals):
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
