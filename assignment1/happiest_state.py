import sys
import json
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
    
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

def printmaxstate(tweet_file, sentscores):
    statescores = {}
    ivstates = {v: k for k, v in states.items()}
    for line in tweet_file:
        tweetdict = {}
        tweetdict = json.loads(line);
        tweetplace = tweetdict.get('place')
        if(tweetplace != None):            
            tweetcountry = tweetplace.get('country')
            if(tweetcountry == 'United States'):
                tweetplacename = tweetplace.get('full_name')
                placenames = tweetplacename.split(',')
                tweettext = tweetdict.get('text')
                tweetscore = get_tweet_score(tweettext, sentscores)
                stateabbrv = placenames[1].strip()
                if(stateabbrv == 'USA'):
                    statename = placenames[0].strip()
                    if(ivstates.get(statename) != None):
                        state = ivstates.get(statename)
                        statescore = statescores.get(state, 0)
                        statescore += tweetscore
                        statescores[state] = statescore
                elif(states.get(stateabbrv) != None):
                    state = stateabbrv
                    statescore = statescores.get(state, 0)
                    statescore += tweetscore
                    statescores[state] = statescore

    print str(max(statescores.iteritems(), key=operator.itemgetter(1))[0])          
                
                        
def main():
    sentscores = {}
    with open(sys.argv[1]) as sent_file:
        sentscores = sent_scores(sent_file)
    with open(sys.argv[2]) as tweet_file:
        printmaxstate(tweet_file, sentscores)
#        #lines(tweet_file)
#        print_tweet_scores(tweet_file, sentscores)

    
    
if __name__ == '__main__':
    main()
