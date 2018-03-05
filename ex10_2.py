fname = input("Enter a file: ")
if len(fname)<1: fname = 'mbox-short.txt'
fh = open(fname)
di = dict()

for line in fh:
    if line.startswith('From '):
        wds = line.split()
        time = wds[5]
        hr = time.split(':')[0]
        di[hr] = di.get(hr,0)+1

lst = di.items()
lst = sorted(ls)
for k,v in lst:
    print(k, v)
