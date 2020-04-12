import bs4 as bs
import urllib.request as req
import datetime


today=str(datetime.date.today())
filename="News"+today+".txt"

#Base page Link
url="https://www.indiatoday.in/"

url_link=req.urlopen(url)
page_html=url_link.read()
url_link.close()

#Parsing the base page in Html format
soup=bs.BeautifulSoup(page_html,"html.parser")
container = soup.find_all('ul',{'class':'itg-listing'})[0]

#Creating a file to save the Data
f=open(filename,"w")


for i in container.find_all('li'):
    f.write("Top News:\n")
    f.write("     " + i.text + "\n")

    #Again Parsing the link extracted from base page
    link=i.a.get('href')
    url_link=req.urlopen(url+link)
    page_html=url_link.read()
    url_link.close()
    
    soup_stories=bs.BeautifulSoup(page_html,"html.parser")
    
    f.write("Headlines:\n")
    f.write("     " + soup_stories.h1.text + "\n")
    
    f.write("Description:\n")
    f.write("     " + soup_stories.h2.text + "\n")
    
    container1=soup_stories.find('dl',{'class':'profile-byline'})
    for add in container1.find_all("dt"):
        f.write(add.text+"\n")
    
    
    f.write("\n\n\n")    

f.close()
