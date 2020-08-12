def clean_freq(text):
    '''A pre-processing function that cleans text of stopwords, punctuation and capitalization, tokenizes, lemmatizes
    then finds the most frequently used 100 words
    
    text - the text to be cleaned in string format'''

    # Get all the stop words in the English language
    import nltk
    from nltk.corpus import stopwords
    #importing additional functions to execute
    import string
    from nltk import FreqDist
    #importing and enstantiating lemmatizer 
    from nltk.stem import WordNetLemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()
    
    stopwords_list = stopwords.words('english')

    #remove punctuation
    stopwords_list += list(string.punctuation)
    ##adding adhoc all strings that don't appear to contribute, added 'article, page and wikipedia' iteratively as 
    ##these are parts of most comment strings
    stopwords_list += ("''","``", "'s", "\\n\\n" , '...', 'i\\','\\n',
                       '•', "i", 'the', "'m", 'i\\', "'ve", "don\\'t", "'ll",
                      "'re", "\\n\\ni", "it\\", "'ll", 'you\\', "'d", "n't",
                      '’', 'app', 'wa', 'ha', 'wo', 'u',"'s", "ve","'m","wo","doe") 
    
    from nltk import word_tokenize
    tokens = word_tokenize(text)
    lemma_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stopped_tokens = [w.lower() for w in lemma_tokens if w.lower() not in stopwords_list]
    freqdist = FreqDist(stopped_tokens)
    most_common_stopped = freqdist.most_common(100)
    return most_common_stopped



def clean_tokens(text):
    '''A pre-processing function that cleans text of stopwords, punctuation and capitalization, tokenizes, lemmatizes
    then finds the most frequently used 100 words
    
    text - the text to be cleaned in string format'''

    # Get all the stop words in the English language
    import nltk
    from nltk.corpus import stopwords
    #importing additional function to execute
    import string
    #importing and enstantiating lemmatizer 
    from nltk.stem import WordNetLemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()
    
    stopwords_list = stopwords.words('english')

    #remove punctuation
    stopwords_list += list(string.punctuation)
    ##adding adhoc all strings that don't appear to contribute, added 'article, page and wikipedia' iteratively as 
    ##these are parts of most comment strings
    stopwords_list += ("''","``", "n't", 'app', "...", "n't",
                       "wa","ve", "ha","'", 'wa', 'ha', 'ca', "'ll",
                       'doe' 'wo','u',"'s","'ve", "ve","'m","wo","doe",
                       "'ve", "'d") 
  
    
    from nltk import word_tokenize
    tokens = word_tokenize(text)
    lemma_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stopped_tokens = [w.lower() for w in lemma_tokens if w.lower() not in stopwords_list]
    return stopped_tokens

def cleaner_tokens(text):
    '''A pre-processing function that cleans text of stopwords, punctuation and capitalization, tokenizes, lemmatizes
    then finds the most frequently used 100 words
    
    text - the text to be cleaned in string format'''

    # Get all the stop words in the English language
    import nltk
    from nltk.corpus import stopwords
    #importing additional function to execute
    import string
    #importing and enstantiating lemmatizer 
    from nltk.stem import WordNetLemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()
    
    stopwords_list = stopwords.words('english')

    #remove punctuation
    stopwords_list += list(string.punctuation)
    ##adding adhoc all strings that don't appear to contribute, added 'article, page and wikipedia' iteratively as 
    ##these are parts of most comment strings
    stopwords_list += ("''","``", "n't", 'app', "...", "n't", "'d"
                       "wa","ve", "ha","'", 'wa', 'ha', 'ca', "'re"
                       'doe' 'wo','u',"'s","'ve", "ve","'m","wo","doe",
                       'love', 'great', 'excellent', 'awesome', 'really', 'good', 'brilliant',
                       'fantastic', 'amazing', 'wonderful', 
                       'rubbish', 'terrible', 'worst', 'insane', 'useless', 'horrible',
                       'awful', 'stupid', 'suck', 'sucks'
                       ) 
  
    
    from nltk import word_tokenize
    tokens = word_tokenize(text)
    lemma_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stopped_tokens = [w.lower() for w in lemma_tokens if w.lower() not in stopwords_list]
    return stopped_tokens



def clean_comment(comment):
    '''Lemmatizes, removes capitalization, punctuation and 'stopwords' from the lemmatized tokens,
    returns data in the dataframe for modeling in a "clean" state
    
    comment - a text string'''
    from nltk.corpus import stopwords
    import string
    #splitting sentences into tokens
    tokens = comment.split()
    
    #instantiating Lemmatizer and lemmatizing words
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemma_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    stopwords_list = stopwords.words('english')
    stopwords_list += ("''","``", ".", 'app', 'apps', 'ca',"--", 'wa', 'ha', 'doe', 'wo', 'u') 

    #remove punctuation, capitalization, and stopwords
    stopwords_list += list(string.punctuation)
    stopped_tokens = [w.lower() for w in lemma_tokens if w.lower() not in stopwords_list]
    
    return ' '.join(stopped_tokens)

def good_clean_tokens(text):
    '''A pre-processing function that cleans text of stopwords, punctuation and capitalization, 
    tokenizes, lemmatizes 

    text - the text to be cleaned in string format'''

    import nltk
    from nltk.corpus import stopwords
    #importing and enstantiating lemmatizer 
    from nltk.stem import WordNetLemmatizer   
    lemmatizer = nltk.stem.WordNetLemmatizer()
     # Get all the stop words in the English language  
    stopwords_list = stopwords.words('english')
   
    #importing additional function to execute
    import string   
    #remove punctuation
    stopwords_list += list(string.punctuation)
    ##adding adhoc all strings that don't appear to contribute, added 'love, great, good, really, amazing' iteratively as 
    ##these are parts of most comment strings
    stopwords_list += ("''","``", "n't", 'app', 'love', 'apps', 'great', 'good', 'really', 'wa', 'ha',"I", "l",
                     '...', "--","'s", 'amazing', 've', 'excellent', 'awesome', 'wonderful', 'fantastic', "ve") 
  
    
    from nltk import word_tokenize
    tokens = word_tokenize(text)
    lemma_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stopped_tokens = [w.lower() for w in lemma_tokens if w.lower() not in stopwords_list]
    return stopped_tokens

def five_cluster_wrdcld(xtrain):
    '''Takes a dataframe to return wordcloud renderings for each cluster in a KMEANS 
    model for a 5 cluster model

    xtrain - a dataframe '''

    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    cloud = {}
    for cluster in list(xtrain['5cluster'].unique()):
        clust_df = xtrain[xtrain['5cluster']==cluster]
            
        wrdcld5 = WordCloud(width=400, height=200, background_color="white", 
                            max_words=5000, contour_width=3, collocations=False, 
                            contour_color='steelblue')
        wrdcld5.generate(clust_df['content'].to_string())
        clustwrdcld = wrdcld5.to_image()
        fig = plt.imshow(clustwrdcld, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Cluster {cluster} WordCloud:')
        cloud[cluster]=fig
        plt.show()
    return cloud

def six_cluster_wrdcld(xtrain):

    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    cloud = {}
    for cluster in list(xtrain['6cluster'].unique()):
        clust_df = xtrain[xtrain['6cluster']==cluster]
            
        wrdcld6 = WordCloud(width=400, height=200, background_color="white", 
                            max_words=5000, contour_width=3, collocations=False, 
                            contour_color='steelblue')
        wrdcld6.generate(clust_df['content'].to_string())
        clustwrdcld = wrdcld6.to_image()
        fig = plt.imshow(clustwrdcld, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Cluster {cluster} WordCloud:')
        cloud[cluster]=fig
        plt.show()
    return cloud

def plot_coefs(classifier, scaler, col):
    '''Plotting function that takes a dataframe and classifier model
    and plots the top ten most negative coefficients
    
    df - dataframe that is being analysed
    classifier - multinomial classifier
    '''
    #importing libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    feats = scaler.get_feature_names()

    #creating a dictionary for each of the classes and enumerating them in 
    #order to track the coefficients for each:
    class_dict = {}
    for i, cat in enumerate(classifier.classes_):
        class_dict[cat] = classifier.coef_[i]
    
    
    #creatging a dataframe of the output
    class_coefs = pd.DataFrame(class_dict)
    
    #creating a column that tracks the features for each
    class_coefs['feats'] = feats
    
    #setting the index to each of the features:
    class_coefs.set_index('feats', inplace=True)
    
    #slicing the most meaningful negative words:
    class_coefs[col].sort_values(ascending=False).head(15).plot(kind='barh')
    plt.title('Most important terms used to classify a review:', fontsize=14)
    plt.ylabel('Term')
    plt.xlabel('Mathmetical Coefficient')



def generate_wordcloud(words, mask):
    '''This function takes in text and a mask as a .png and generates a wordcloud in the 
    shape of the mask..

    words - a string of text
    mask - .png file eg: nmask = np.array(Image.open('mask.png')) you'll need the file
    path if the file isn't local'''

    import matplotlib.pyplot as plt
    from wordcloud import WordCloud


    word_cloud = WordCloud(width  = 500, height = 300, background_color='white', 
                           contour_color = 'purple', contour_width = 1, mask=mask).generate(words)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    