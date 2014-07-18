import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def calc_term_freq(tweet_file):
    totalfreq = 0
    termfreqs = {}
    for line in tweet_file:
        tweetdict = {}
        tweetdict = json.loads(line);
        tweettext = tweetdict.get('text')
        tweetterms = get_tweet_terms(tweettext)
        if (tweetterms != None):        
            for term in tweetterms:
                termfreq = 0
                termfreq = termfreqs.get(term, 0) 
                termfreq += 1
                termfreqs[term] = termfreq
                totalfreq += 1
            
    print_norm_freq(termfreqs, totalfreq)
            
def print_norm_freq(termfreqs, totalfreq):
    for term, freq in termfreqs.iteritems():
        fractionalfreq = freq/totalfreq
        print term.encode('utf-8') + " " + str(fractionalfreq)
                    
def get_tweet_terms(tweettext):
    if(tweettext != None):
        terms = tweettext.split()
        return terms
    else:
        return None

def main():
    tweet_file = open(sys.argv[1])
    calc_term_freq(tweet_file)

if __name__ == '__main__':
    main()