import requests 
from bs4 import BeautifulSoup 
import csv 
from selenium import webdriver
import time

# driver = webdriver.Firefox()
# driver.get('https://www.ebooks777.net/')
# print (driver.title)
# driver.find_element_by_xpath(r"/html/body/header/section/div/div/form/input").send_keys("node js")
# driver.find_element_by_xpath(r"/html/body/header/section/div/div/form").submit()
# time.sleep(5)

# alinks = driver.find_elements_by_class_name("title")

# ax2 = []
# for x in alinks:
#     ax2.append(x["href"])

    # alinks2 = driver.find_elements_by_class_name("title")
    # print(alinks2[x2], alinks2[x2].get_attribute('innerHTML'))
    # alinks2[x2].click()
    # x2 +=1
    # driver.back()


    

# driver.quit()


links=[]  # a lfinist to store quotes 
linksText=[]

URLa = "https://www.ebooks777.net/web-development/"
URLb = "https://www.ebooks777.net/web-development/page/"
URLc = ""

#URLa = "https://www.ebooks777.net/"
#URLb = "https://www.ebooks777.net/page/"
#URLc = "?s=android"


URL = ""
#https://www.ebooks777.net/it-ebooks/page/13/
#https://www.ebooks777.net/it-ebooks/

for x in range(1, 23):
    if x == 1:
        URL = URLa + URLc
    else:
        URL = URLb + str(x) + '/' + URLc
        #https://www.ebooks777.net/page/2/?s=.net

    try:
        r = requests.get(URL)
    except:
        continue
    
    soup = BeautifulSoup(r.content, 'html5lib') 
    
    for row in soup.findAll('a', attrs = {'class':'title'}):
        links.append(row.attrs["href"])
        linksText.append(row.text)


for x in range(0, len(links)):
    URL = links[x]
    try:
        r = requests.get(URL)
    except:
        continue
    soup = BeautifulSoup(r.content, 'html5lib')
    for row in soup.findAll('a', attrs = {'target':'_blank'}):
        URL = row.attrs["href"]
        if "Download (" in row.text:
            varnum = URL.split('/')
            varnum2 = varnum[4].split('.')
            print(URL)
            r = requests.get(URL)
            try:
                open(varnum2[0] + " - " + linksText[x] + '.pdf', 'wb').write(r.content)
            except:
                print("unable to save")



# #table = soup.find('div', attrs = {'id':'all_quotes'})  
   
# for row in soup.findAll('div', attrs = {'class':'col-md-6 col-xs-6'}): 
#     row2 = row.findAll('dt')
#     heading = row.findAll('h2')
#     print(heading[0].text, row2[1].text)
#     #url2 = 'https://pdf.yspark.vip/078/1617290572.pdf'
#     for x in range(30, 100):
#         url2 = 'https://pdf.yspark.vip/' + str(x).zfill(3) + '/' + str(row2[1].text) + '.pdf'
#         r2 = requests.get(url2, allow_redirects=True)
#         if r2.status_code == 200:
#             open(row2[1].text + " - " + heading[0].text + '.pdf', 'wb').write(r2.content)
#             print ('Pass ', url2, r2.status_code)
#             break
#         else:
#             print ('Fail ', url2, r2.status_code)


   
    