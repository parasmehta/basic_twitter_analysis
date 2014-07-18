import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def print_tweet_scores(tweet_file, sentscores):
    for line in tweet_file:
        tweetdict = {}
        tweetdict = json.loads(line);
        tweettext = tweetdict.get('text')
        tweetscore = get_tweet_score(tweettext, sentscores)
        print tweetscore
            
def get_tweet_score(tweettext, sentscores):
    tweetscore = 0
    if(tweettext != None):
        terms = tweettext.split()
        for term in terms:
            termscore = 0
            termscore = sentscores.get(term, 0)
            tweetscore += termscore
    else:
        tweetscore = 0
        
    return tweetscore
    
def sent_scores(afinnfile):    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores # Print every (term, score) pair in the dictionary
    
def main():
    sentscores = {}
    with open(sys.argv[1]) as sent_file:
        sentscores = sent_scores(sent_file)
    with open(sys.argv[2]) as tweet_file:
        #lines(tweet_file)
        print_tweet_scores(tweet_file, sentscores)
    
    
if __name__ == '__main__':
    main()
