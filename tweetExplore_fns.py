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
	print(person, '  # tweets:',len(person_tweetInd), 'avg polarity:', np.average(person_sentiment_polarity))
	return person_sentiment_polarity, person_sentiment_subjectivity, person_tweetInd




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
    # display wordcloud
#     plt.imshow(wordcloud)
#     plt.axis('off')
#     plt.show();



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


def autolabelInt(rects,axNum,ax):
    """attach labels to bars, integers"""
    for rect in rects:
        height = rect.get_height()
        ax[axNum].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def autolabelDec(rects,axNum,ax):
    """attach labels to bars, 3 decimals"""
    for rect in rects:
        height = rect.get_height()
        ax[axNum].text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%0.3f' % height,
                ha='center', va='bottom')
