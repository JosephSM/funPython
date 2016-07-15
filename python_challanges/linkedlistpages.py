import requests, re

numreg = re.compile(r'and the next nothing is ([0-9]+)')
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'


tempdic = {'nothing':int(90052)}
numlist = []
print("starting...")
for i in range(401):
    r = requests.get(url, params=tempdic)
    regsearch = numreg.search(r.text)
    print(i, r.text, r.url)
    textnum = regsearch.group(1)
    tempdic['nothing'] = textnum
    
