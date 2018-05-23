# pip install RoboBrowser
# http://robobrowser.readthedocs.io/en/latest/

from robobrowser import RoboBrowser
from requests import Session
import re

session = Session()

open = session.get("http://www.leboncoin.fr/")
print(open.headers)

browser = RoboBrowser(session=session, user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1')
browser.open('http://www.leboncoin.fr/')

links = browser.get_links()

#for link in links:
# print(link)
 
bretagne_tag = browser.find("a", attrs={'id': re.compile("region_5")})

print("****************************************************")

print("bretagne_tag : " + str(bretagne_tag))

#bretagne = browser.get_link(bretagne_tag)

print("****************************************************")

#print(bretagne)

#browser.follow_link(bretagne_tag)

#print(browser.find("section", attrs={"class":"tabsContent block-white dontSwitch"}))
#print(browser.find("h1", attrs={"class":"grey small no-border"}))

#browser = RoboBrowser(history=False)
#browser.open("https://www.leboncoin.fr/annonces/offres/bretagne/")

#search_input = browser.find("input", attrs={'id': "searchbutton"})
#print("search_input : " + str(search_input))

#form = browser.get_form(action="//www.leboncoin.fr/li")

#form = get_forms()[0]

#print(browser.parsed)
#for form in forms:
#print("****************************************************")

#print("forms keys : " + str(form.keys))

#form["q"].value="aspirateur" 

#print("\n")
#print("form : "+str(form))
#print("\n")

#print("avant submit_form")
#print("first item : " + str(browser.find("h2", attrs={"class":"item_title"})))
#print("rechercher autour de moi : " + str(browser.find("button", attrs={"id":"geolocMain"})))

#browser.submit_form(form)

#print(browser.select("body"))
#print("après submit_form")
#print("first item : " + str(browser.find("h2", attrs={"class":"item_title"})))
#print("rechercher autour de moi : " + str(browser.find("button", attrs={"id":"geolocMain"})))

#print("****************************************************")

browser.open("https://www.leboncoin.fr/annonces/offres/bretagne/?th=1&q=aspirateur&it=1")

#print("first item : " + str(browser.find("h2", attrs={"class":"item_title"})))

results = browser.find_all("section", attrs={"class":"item_infos"})

#print(str(results))

print("------------------------")
print("section = " + str(results[0]))
print("----------")
print("title = " + results[0].findAll("h2")[0].text.strip())
print("----------")
print("price = " + results[0].findAll("h3")[0].text.strip())
print("----------")
print("location = " + str(results[0].findAll("p", attrs={"itemprop":"availableAtOrFrom"})[0].text.strip().replace(" ","").replace("\n","")))

for result in results:
 print("------------------------")
 #print("section = " + str(result))
 #print("----------")
 #print(result)
 #print(result.find("h2"))
 if result.find("h2") != None:
  print("title = " + result.findAll("h2")[0].text.strip())
  print("-")
  print("price = " + result.findAll("h3")[0].text.strip())
  print("-")
  print("location = " + str(result.findAll("p", attrs={"itemprop":"availableAtOrFrom"})[0].text.strip().replace(" ","").replace("\n","")))

#print(item_infos[0])

