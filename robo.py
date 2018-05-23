# pip install RoboBrowser
# http://robobrowser.readthedocs.io/en/latest/

from robobrowser import RoboBrowser
from requests import Session
import re

session = Session()

open = session.get("http://www.leboncoin.fr/")
print(open.headers)

browser = RoboBrowser(session=session, user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1')

browser.open("https://www.leboncoin.fr/annonces/offres/bretagne/ille_et_vilaine?th=1&q=aspirateur&it=1&f=p")

results = browser.find_all("section", attrs={"class":"item_infos"})

i=0

for result in results:
 print("------------------------")
 if result.find("h2") != None:
  i=i+1
  print(i)
  print("title = " + result.h2.text.strip())
  print("-")
  print("price = " + result.h3.text.strip())
  print("-")
  print("location = " + str(result.findAll("p", attrs={"itemprop":"availableAtOrFrom"})[0].text.strip().replace(" ","").replace("\n","")))
  print("-")
  print("date = " + result.aside.p.text.strip())


