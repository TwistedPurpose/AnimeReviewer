
infile = open('test-anime-titles.dat','r')
outfile = open('test-titles.txt','w')

for line in infile:
    if not line.startswith('#'):
        string = line.split('|')
        if string[2] == "en":
            print string[3].strip()
            outfile.write(string[3]);