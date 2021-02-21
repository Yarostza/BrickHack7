import twint
import os
import re
import preprocessor as p
import textblob as tb

fileName = "tweets.json"

while True:
    print("--------------------------------")
    print("Who would you like to examine? Type q to quit")
    username = input()
    if username == "q":
        break
    else:
        print("Calculating...")

    try:
        if os.path.exists(fileName):
            os.remove(fileName)

        tweets = []
        config = twint.Config()
        config.Username = username
        config.Limit = 10
        config.Hide_output = True
        config.Store_object = True
        config.Store_object_tweets_list = tweets

        twint.run.Search(config)

        tweetsCleaned = []

        for tweet in tweets:
            tweetsCleaned.append(p.clean(tweet.tweet))

        def getSubjectivity(text):
            return tb.TextBlob(text).sentiment.subjectivity

        def getPolarity(text):
            return tb.TextBlob(text).sentiment.polarity

        if len(tweetsCleaned) > 0:
            totalPolarity = 0.0
            totalSubjectivity = 0.0
            for tweet in tweetsCleaned:
                totalPolarity += getPolarity(tweet)
                totalSubjectivity += getSubjectivity(tweet)
            totalPolarity /= len(tweetsCleaned)
            totalSubjectivity /= len(tweetsCleaned)
            print("Polarity (-1, 1): ", totalPolarity)
            if totalPolarity <= -0.90:
                print("    Extremely negative")
            print("Subjective (0, 1): ", totalSubjectivity)
    except:
        print("User could not be found")