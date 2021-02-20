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

        config = twint.Config()
        config.Username = username
        config.Limit = 10
        config.Store_json = True
        config.Output = fileName
        config.Hide_output = True

        twint.run.Search(config)

        tweets = []
        for line in open(fileName, 'r'):
            tweets.append(line)

        tweetsCleaned = []

        for tweet in tweets:
            try:
                temp = p.clean(tweet.split("\"tweet\": \"")[1].split("\", \"language\"")[0])
                temp2 = re.sub(r'[^\w\s]', '', temp)
                tweetsCleaned.append(temp2)
            except:
                continue

        def getSubjectivity(text):
            return tb.TextBlob(text).sentiment.subjectivity

        def getPolarity(text):
            return tb.TextBlob(text).sentiment.polarity

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