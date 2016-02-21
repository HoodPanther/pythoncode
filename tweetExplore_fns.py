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
#     newSTOP.update(('co','https','t','\'RT','R','T','-RT','RT@'))
    joinedTexts = " ".join(str(x) for x in newlist)
    setattr(WordCloud,"setfont",'/anaconda/envs/eq_env/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf')
    # font_path='/anaconda/envs/eq_env/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf',

    #generate wordcloud
    wordcloud = WordCloud(stopwords=newSTOP,
                              background_color='black',
                              width=1700,
                              height=1400
                             ).generate(joinedTexts)
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
