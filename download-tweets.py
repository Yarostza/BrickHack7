import twint
import preprocessor as p
import textblob as tb

while True:
    print("--------------------------------")
    print("Who would you like to examine? Type q to quit")
    username = input()
    print("\n")
    if username == "q":
        break
    else:
        print("Calculating...")
        print("\n")

    try:
        tweets = []
        config = twint.Config()
        config.Username = username
        config.Limit = 1000
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
            print("Tweets Analyzed: ", len(tweetsCleaned))
            totalPolarity /= len(tweetsCleaned)
            totalSubjectivity /= len(tweetsCleaned)
            print("Polarity (-1, 1): ", totalPolarity)
            if totalPolarity <= -0.90:
                print("    Extremely negative")
            print("Subjective (0, 1): ", totalSubjectivity)
    except:
        print("User could not be found")