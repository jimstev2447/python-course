import re

fhand = open('regex.txt')

for line in fhand:
    print line
#checks for 'q'
    if re.search('q', line):
        print "this line has a 'q' in it"

#checks starts with 'q'
    if re.search('^q',line):
        print "this line starts with a 'q'"

#checks has 'q' or 'Q'
    if re.search('[qQ]',line):
        print "this line has a 'q' or 'Q' in it"

#checks has '*'
    if re.search('[*]',line):
        print "this line has a '*' in it"

#checks starts with 'Q' or 'q'
    if re.search('^[Qq]',line):
        print "this line st/w a Q or q"

#checks has both 'a' and 'e'
    if re.search('[a].*[e]|[e].*[a]',line):
        print "this line has an a and e in it"

#checks for an a then later an e
    if re.search('[a].*[e]', line):
        print "this line has a followed by e"
#checks not a
    if re.search('^[^aA]*$',line):
        print "this line does not have an a in"

#checks if has no a or e
    if re.search('^[^aA|eE]*$',line):
        print "this line has no a or e in"
    
#checks has an a but not an e
    if re.search('^[^e]*a[^e]*$',line):
        print "this line has an a but no e in it"

#checks for consec vowels
    if re.search('[aeiou][aeiou]',line):
        print "this line has consec vowels in"

#checks for 3 vowles
    if re.search('[aeiou]+.*[aeiou]+.*[aeiou]+',line):
        print "this line has 3vowels in"

#checks for at least 6 characters
    if re.search('.{6,}', line):
        print "this line has at least 6 characters"
#checks for exactly 6 characters
    if re.search('^.{6}$',line):
        print "this line has exactly 6 characters"

    print ""

