fname = raw_input('Enter file name: ')

names = dict()

try:
    fhand = open(fname)
except:
    fname = 'mbox-short.txt'    
    fhand = open(fname)

for lines in fhand:
    if lines.startswith('From '):
        name = lines.split()[1]
        names[name] = names.get(name,0) + 1

highname = None
highval = None

for name,value in names.items():

    if highname is None:
        highname = name
        highval = value
    elif value > highval:
        highname = name
        highval = value

print highname,highval

