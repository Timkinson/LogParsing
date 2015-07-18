'''
Created on Jul 17, 2015

@author: Tim
'''

import re
import json

if __name__ == '__main__':
    pass

def TotalLines(fn):
    f = open(fn, 'r')
    i = 0
    for line in f:
        i += 1
    return(i)
        
def ParseOneLine(one_line, line_number):
    
    line_parsed = []
    ll = len(one_line)
    whereWeAre = 0 #Where we are at the string
    
    line_parsed.append((line_number, 'LINE NUMBER'))
        
    #Parsing Address
    for i in range(0, ll): 
        if one_line[i] == ' ':
            line_parsed.append((one_line[0:(i-1)], 'IP_ADDRESS'))
            whereWeAre = i
            break
    #Parsing Date
    for i in range(whereWeAre, ll): 
        if one_line[i] == '[':
            left_one = i
        if one_line[i] == ']':
            right_one = i
            line_parsed.append((one_line[left_one+1:right_one], 'DATE'))
            whereWeAre = i
            break
    
    #Parsing Command in quotation marks
    for i in range(whereWeAre, ll): 
        if one_line[i] == '"':
            left_quote = i
            whereWeAre = i + 1
            break
    for i in range(whereWeAre, ll):
        if one_line[i] == '"':
            right_quote = i
            whereWeAre = i + 2
            break
    line_parsed.append((one_line[left_quote+1:right_quote], 'COMMAND'))
    
    #Parsing first and second number
    for i in range(whereWeAre, ll):
        if one_line[i] == ' ':
            line_parsed.append((one_line[whereWeAre:i], 'FIRST_NUMBER'))
            line_parsed.append((one_line[i+1:ll-1], 'SECOND_NUMBER'))
            break
    
    
    
    return line_parsed
    
def ParseFile(fn):
    
    file_parsed = []
    
    f = open(fn, 'r')
    i = 0
    
    for line in f:
        i += 1
        file_parsed.append(ParseOneLine(line, i))
    return file_parsed


     
     
        
    
    
    
    

print('Total Lines in log file:', TotalLines('access_log'))

#print(ParseOneLine('92-moc-6.acn.waw.pl - - [08/Mar/2004:08:37:14 -0800] "GET /twiki/pub/TWiki/TWikiLogos/twikiRobot46x50.gif HTTP/1.1" 304 -'))

#print(ParseFile('access_log'))

with open('log_parsed', 'w', encoding='utf8') as outfile:
    json.dump(ParseFile('access_log'), outfile, ensure_ascii=False)


