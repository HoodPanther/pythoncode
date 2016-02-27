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