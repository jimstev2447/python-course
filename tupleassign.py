#Assignment with tuples

fname = raw_input("Enter file name: ")
hrscount = dict()

try:
    fhandle = open(fname)
except:
    fhandle = open("mbox-short.txt")

for line in fhandle:
    if not line.startswith("From "): continue
    hrsent = (line.split()[5]).split(':')[0]
    hrscount[hrsent] = hrscount.get(hrsent,0) + 1

for time,count in sorted(hrscount.items()):
    print time, count



