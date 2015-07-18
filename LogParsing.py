'''
Created on Jul 17, 2015

@author: Tim
'''

import re

if __name__ == '__main__':
    pass

WHITESPACE, STRING_IN_QUOTE, DATE, EXPRESSION, EMPTY_FIELD = range(5)

RULE = [
        ('\s+', WHITESPACE),
        ('-|"-"', EMPTY_FIELD),
        ('"([^"]+)"', STRING_IN_QUOTE),
        ('\[([^\]]+)\]', DATE),
        ('([^\s]+)', EXPRESSION)
        ]

def TotalLines(fn):
    f = open(fn, 'r')
    i = 0
    for line in f:
        i += 1
    return(i)
        

def Analysis(rules):
    
    compiled_regexp = [(re.compile(regexp), token_type) for regexp, token_type in rules]

#    f = open(fn, 'r')

    #for line in f:
    
    one_line = '64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846'
    
    def lexic(line):    
        ll = len(one_line)
        i = 0
        while i < ll:
            for pattern, token_type in compiled_regexp:
                match = pattern.match(line, i)
                if match is None:
                    continue
                i = match.end()
                yield (match, token_type)
                break
    return lexic
    
analysis = Analysis(RULE)

print(analysis)
     
     
        
    
    
    
    

#analysis = Analysis(RULE, 'access_log')

#print(TotalLines('access_log')) 

