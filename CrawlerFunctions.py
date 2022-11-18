from bs4 import BeautifulSoup
import requests

def createAttributeForCrawler():
    #創造一個http request，encoding = utf8，再轉成BeautifulSoup object，才能使用的method
    r = requests.get("http://www.csim.scu.edu.tw/news_list.aspx?c=NEWS&cid=1")
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text,"lxml")
    return soup

def getTitle(soup):
    title_a = soup.findAll('a',attrs = {'class':'clearfix'})
    title = []
    for val in title_a:
      title.append(val.h2.text)
    return title

def getDate(soup):
    date_td = soup.findAll('td',attrs = {'class':'date'})
    date = []
    for val in date_td:
      date.append(val.text)
    return date

def getTitleLink(soup):
    title_a = soup.findAll('a',attrs = {'class':'clearfix'})
    title_href = []
    for tag in title_a:
        soup = BeautifulSoup(str(tag),"lxml").a
        title_href.append("http://www.csim.scu.edu.tw/" + soup['href'])
    return title_href

def sortCategory(title):
    category = []

    for val in title:
      if "程式能力檢定"in val or "程式檢定"in val or "程式設計能力檢定"in val or "程式設計檢定" in val:
        category.append("程式檢定")
      elif "程式競賽"in val or"資管程式競賽"in val or"資管系程式競賽" in val or "程式設計競賽" in val or"資管程式設計競賽" in val :
        category.append("程式競賽")
      elif "獎助學金申請" in val or"獎學金" in val or"獎助學金" in val:
        category.append("獎助學金")
      elif "實習" in val or"工讀" in val or"校外實習" in val or"工讀生" in val:
        category.append("實習")
      elif "講座"in val or "演講" in val or "講師" in val or "外師" in val:
        category.append("講座")
      elif "課程" in val or"選課"in val or"課堂"in val or"開課" in val or"學程" in val:
        category.append("課程")
      else:
        category.append("其他")
        
    return category

def getText(innards):
    r = requests.get(innards)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text,"lxml")
    content = ""
    for val in soup.findAll('section', attrs = {'class','html-content'}):
        content = content + val.text.replace('\r','').replace('\t','').replace('\xa0','')
    content = content.replace("\n\n","\n") #因為爬下來的內容常常同時換行兩次，很站空間
    return content

def getImage(innards):
    r = requests.get(innards)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text,"lxml")
    image = ""
    for val in soup.findAll('section', attrs = {'class','html-content'}):
        if val.img != None:
            image = "http://www.csim.scu.edu.tw" + val.img['src']
            
    return image

def getData():
    soup = createAttributeForCrawler()
    title = getTitle(soup)
    date = getDate(soup)
    title_href = getTitleLink(soup)
    category = sortCategory(title)
    
    data = [(category[i], date[i],title[i], title_href[i]) for i in range(len(title))]
    return data
