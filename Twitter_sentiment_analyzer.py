


#This function takes the keywords file and strips each line at the comma i.e. separates score from word
#It then stores the key and the number (score) associated with it in a dictionary
def keyWords(file):
    keywords = {}
    for line in file:
        line = line.rstrip()
        entries = line.split(",")
        keywords[entries[0]] = int(entries[1])
    return keywords

#This is the comput_tweets function definition which outputs the final score
def compute_tweets(keywords, tweet):
    score = []
    for x in range(len(tweet)):
        sentiment = 0     #Initializing sentiment and number of tweets
        numOfTweets = 0
        for eachLine in tweet[x]:    # for loops that compairs tweets to keywords file and produced score
            lineScore = 0
            numOfKeywords = 0
            for word in eachLine:
                for key in keywords:
                    if word == key:
                        lineScore = lineScore + keywords[key]
                        numOfKeywords = numOfKeywords + 1
            if numOfKeywords != 0:
                lineScore = lineScore/numOfKeywords
                sentiment = sentiment + lineScore
                numOfTweets = numOfTweets + 1
        if numOfTweets != 0:
            sentiment = sentiment/ numOfTweets
            score.append([sentiment, numOfTweets])
    return score

def timeZone(tweet):           # Function that formats each tweet so text in the tweets is only composed of letters
    LAT_MAX = 49.189787       #initializing the boarders for each timezone
    LAT_MIN = 24.660845

    LONG_MAX_PACIFIC = -115.236428
    LONG_MIN_PACIFIC = -125.242264

    LONG_MAX_MOUNTAIN = -101.998892
    LONG_MIN_MOUNTAIN = -115.236428

    LONG_MAX_CENTRAL = -87.518395
    LONG_MIN_CENTRAL = -101.998892

    LONG_MAX_EASTERN = -67.444574
    LONG_MIN_EASTERN = -87.518395


    tweets = [[],[],[],[]]
    whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")


    for eachLine in tweet:    #for loop that cycles through the tweets and adds to the location
        eachLine = eachLine.split()
        eachLine[0]= float(eachLine[0].strip('[,'))
        eachLine[1] = float(eachLine[1].strip(']'))
        for i in range(5,len(eachLine)):
            eachLine[i] = (''.join(filter(whitelist.__contains__, eachLine[i]))).lower()
        if eachLine[0] >= LAT_MIN and eachLine[0] <= LAT_MAX:
            if eachLine[1] >= LONG_MIN_PACIFIC and eachLine[1] <= LONG_MAX_PACIFIC:
                tweets[3].append(eachLine)
            elif eachLine[1] > LONG_MIN_MOUNTAIN and eachLine[1] < LONG_MAX_MOUNTAIN:
                tweets[2].append(eachLine)
            elif eachLine[1] >= LONG_MIN_CENTRAL and eachLine[1] <= LONG_MAX_CENTRAL:
                tweets[1].append(eachLine)
            elif eachLine[1] > LONG_MIN_EASTERN and eachLine[1] < LONG_MAX_EASTERN:
                tweets[0].append(eachLine)
    return tweets

#defining the function responsible for printing the final score and number of tweets in a timezone
def printTimeZoneScores(score):
    print("\nHappiness Score for the Pacific Timezone is {}".format(score[3][0]))
    print("Number of tweets found in this timezone: {}\n".format(score[3][1]))

    print("Happiness score for the Mountain Timezone is {}".format(score[2][0]))
    print("Number of tweets found in this timezone: {}\n".format(score[2][1]))

    print("Happiness score for the Central Timezone is {}".format(score[1][0]))
    print("Number of tweets found in this timezone: {}\n".format(score[1][1]))

    print("Happiness score for the Eastern Timezone is {}".format(score[0][0]))
    print("Number of tweets found in this timezone: {}".format(score[0][1]))

def main():             # Main function is deffined
    try:
        fileOfKeywords = input("Please enter the name of the file containing the keywords: ")
        k = open(fileOfKeywords,"r",encoding="utf-8")
        fileOfTweets = input("Please enter the name of the file containing the tweets: ")
        t = open(fileOfTweets,"r",encoding="utf-8")
        keywords = keyWords(k)
        tweets = timeZone(t)
        score = compute_tweets(keywords, tweets)
        printTimeZoneScores(score)



    except IOError :                            # Errors that can occur
        print("Error: file not found.")
        exit()
    except ValueError :
        print("Error: file contents invalid.")
        exit()
    except RuntimeError as error :
        print("Error:", str(error))
        exit()

main()  #main function is called

