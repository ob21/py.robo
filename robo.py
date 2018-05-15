# pip install RoboBrowser
# http://robobrowser.readthedocs.io/en/latest/

from robobrowser import RoboBrowser
from requests import Session
import re

session = Session()

browser = RoboBrowser(session=session, user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1')
browser.open('http://www.leboncoin.fr/')

links = browser.get_links()

for link in links:
 print(link)
 
bretagne_tag = browser.find("a", attrs={'id': re.compile("region_5")})

print("****************************************************")

print("bretagne_tag : " + str(bretagne_tag))

bretagne = browser.get_link(bretagne_tag)

print("****************************************************")

print(bretagne)

browser.follow_link(bretagne_tag)

form = browser.get_form(action="//www.leboncoin.fr/li")

#print(browser.parsed)
#for form in forms:
#print("****************************************************")

#print(form)

form['q'].value="tablette samsung" 

browser.submit_form(form)

#print(browser.select("body"))

print("****************************************************")

item_infos = browser.select("item_infos")

print("item_infos : " + str(item_infos))
#print(item_infos[0])

