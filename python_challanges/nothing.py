import requests
import re
r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=802")
for i in range(400):
    try:
        mo= re.search(r"(\d{3,5})", r.text)
        print(i, mo.group(1))
        r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+mo.group(1))
    except:
        print("Oops")
        continue
    finally:
        print(r.text)
