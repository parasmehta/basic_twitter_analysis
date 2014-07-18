import sys
import json
import operator


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def calc_term_freq(tweet_file):
    hashtagfreqs = {}
    for line in tweet_file:
        tweetdict = {}
        tweetdict = json.loads(line);
        tweetentities = tweetdict.get('entities')
        hashtags = get_hashtags(tweetentities)
        if (hashtags != None and hashtags):
            hashtagtexts = get_hashtag_text(hashtags)
            for hashtagtext in hashtagtexts:
                hashtagfreq = 0
                hashtagfreq = hashtagfreqs.get(hashtagtext, 0) 
                hashtagfreq += 1
                hashtagfreqs[hashtagtext] = hashtagfreq

    print_freq(hashtagfreqs)
            
def print_freq(hashtagfreqs):
    sorted_freqs = sorted(hashtagfreqs.iteritems(), key=operator.itemgetter(1), reverse = True)
    #sorted_freqs = sorted_freqs_asc.reverse()
    i = 0
    
    for freqtuple in sorted_freqs:
        if(i < 10):
            i += 1
            print freqtuple[0].encode('utf-8') + " " + str(freqtuple[1])  
        else:
            break
       
        
        #.encode('utf-8') + " " + str(freq)
    #for term, freq in .iteritems():
        #print term.encode('utf-8') + " " + str(freq)

def get_hashtag_text(hashtags):
    hashtagtexts =  []
    for hashtag in hashtags:
        hashtagtext = hashtag.get('text')
        hashtagtexts.append(hashtagtext)
        
    return hashtagtexts
                       
                        
def get_hashtags(tweetentities):
    if(tweetentities != None):
        #print tweetentities
        hashtags = tweetentities.get('hashtags')
        return hashtags
    else:
        return None

def main():
    tweet_file = open(sys.argv[1])
    calc_term_freq(tweet_file)

if __name__ == '__main__':
    main()