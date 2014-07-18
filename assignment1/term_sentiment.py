import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_tweet_scores(tweet_file, sentscores):
    tweetscores = {}
    for line in tweet_file:
        tweetdict = {}
        tweetdict = json.loads(line);
        tweettext = tweetdict.get('text')
        if(tweettext != None and tweettext != ''):
            tweetscore = get_tweet_score(tweettext, sentscores)
            tweetscores[tweettext] = tweetscore
    
    return tweetscores

def get_tweet_score(tweettext, sentscores):
    tweetscore = 0
    terms = tweettext.split()
    for term in terms:
        termscore = 0
        termscore = sentscores.get(term, 0)
        tweetscore += termscore
        
    return tweetscore

def get_counts(tweetscores, sentscores):
    poscounts = {}
    negcounts = {}
    for tweet, score in tweetscores.iteritems():
        terms = tweet.split()
        for term in terms:
            termscore = sentscores.get(term)
            if(termscore == None): #Term not present in sentiment dictionary
                termposcount = poscounts.get(term, 0)
                termnegcount = negcounts.get(term, 0)
                if(score >= 0):
                    poscounts[term] = termposcount + 1
                    negcounts[term] = termnegcount
                elif(score < 0):
                    poscounts[term] = termposcount
                    negcounts[term] = termnegcount + 1
    
    return poscounts, negcounts

def print_new_term_scores(poscounts, negcounts):
    for term, count in poscounts.iteritems():
        score = (poscounts[term] - negcounts[term]) * 5/(poscounts[term] + negcounts[term])
        print term + ' ' + str(score)
    
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
        tweetscores = get_tweet_scores(tweet_file, sentscores)
        poscounts, negcounts = get_counts(tweetscores, sentscores)
        print_new_term_scores(poscounts, negcounts) 

if __name__ == '__main__':
    main()
