import re

fname = raw_input("Enter file name: ")

try:
    fhand = open("fname")
except:
    fhand = open("RegexSum322424.txt")

total = 0

for line in fhand:
    if re.search('[0-9]', line) is None : continue
       
    nums = re.findall('\S[0-9]+',line)
      
    for i in nums:
        total = total + int(i)

print total
    

