import GetOldTweets3 as got
import datetime

user = "BarackObama"
currentDate = datetime.date.today()

startDate = str(currentDate - datetime.timedelta(days=365))
endDate = str(currentDate)

userTweets = got.manager.TweetCriteria().setUsername(user).setSince(startDate).\
    setUntil(endDate).setMaxTweets(10).setEmoji("unicode")

tweetList = got.manager.TweetManager.getTweets(userTweets)

print(tweetList)
#since 2015-09-10 --until 2015-09-12