# pip install RoboBrowser
# http://robobrowser.readthedocs.io/en/latest/

from robobrowser import RoboBrowser
from requests import Session

session = Session()

browser = RoboBrowser(session=session, user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1')
browser.open('http://google.fr')

forms = browser.get_forms()

#print(browser.parsed)
for form in forms:
 print("****************************************************")
 print(form.parsed)

