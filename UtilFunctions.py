from tkinter import *
import webbrowser
from PIL import Image, ImageTk
from io import BytesIO
from pathlib import Path
from CrawlerFunctions import *

#【method for:】displayDetails
#【switch參考資料】https://www.geeksforgeeks.org/switch-case-in-python-replacement/
def getCategoryColor(cat):
    switch = {
        "程式檢定":"#ffcccc",
        "程式競賽":"#ffe0b3",
        "獎助學金":"#cce6ff",
        "實習":"#b3cbe6",
        "講座":"#b3ffb3",
        "課程":"#eeccff",
        "其他":"white"
    }
    return switch.get(cat,"white")

#【method for:】displayDetails
def download(article,content, imgLink):
    outFile = open( str(Path.home() / "Downloads") + "/" +article[2] + ".txt",'w')
    outFile.write(article[2] + "\n\n")
    outFile.write("日期：" + article[1] + "\n")
    outFile.write("公告連結： " + article[3]  + "\n")
    
    if imgLink != "":
        outFile.write("圖片連結： " + imgLink + "\n")
        
    if content.strip() != "":
        outFile.write("==========================以下公告內文===========================\n")
        outFile.write(content)
    outFile.close()

#【method for:】displayDetails
def getPicture(img, window2):
    Label(window2,image=img).grid(row = 2, column = 0)

def displayDetails(article,window):
    #爬取文字內容
    content = getText(article[3])
    
    #爬取圖片內容
    image = getImage(article[3])
            
    #排版視窗和顯示物件
    window2 = Toplevel(window)
    window2.title(article[2])
    Label(window2,text = article[2],font=('Arial',18,'bold')).grid(row = 0, column = 0) #標題
    Label(window2,text = article[1],font=('Arial',12,'bold')).grid(row = 1, column = 0) #日期
    href = Label(window2,text = "網頁連結", width=12, fg='blue',font=('Arial',12,'bold','underline'), cursor="hand2") #細網連結
    href.grid(row=1, column=0, padx = (0,60),sticky = "E")
    href.bind("<Button-1>",lambda e: webbrowser.open_new(article[3]))
     
    #顯示公告文字
    Label(window2,text = "",width = 100,height = 20).grid(row = 2,column = 0,sticky = "W") #調整排版的空label
    Label(window2,text = "~~~~~沒有文字信息喔~~~~" if content.strip() == "" else content,font=('Arial',10)).grid(row = 2, column = 0)
    
    #顯示圖片按鈕
    if image != "":
        response = requests.get(image)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        Button(window2,text = "有圖片喔~~ 按這裡顯示圖片",bg = "white",font=('Arial',12,'bold'),command = lambda val=img, window = window2: getPicture(img,window2)).grid(row = 3, column = 0,sticky = "W",padx = (50,0))
        
    
    #下載內容
    Button(window2,text = "下載文字檔和圖片連結" if image != "" else "下載文字檔",bg = "white",font=('Arial',12,'bold'),command =  lambda stuff = article,text = content, picLink = image: download(stuff,text,picLink)).grid(row = 3, column = 0,sticky = "E",padx = (0,50))
    
    window2.mainloop()


def initTable(data,indexCount,window):
    rowCount = 5
    for el in data[indexCount.getStartIndex():indexCount.getEndIndex() + 1]:
        category = Label(window,text = el[0],width=11,bg = getCategoryColor(el[0]), borderwidth=0.5, relief="groove",font=('Arial',11))
        category.grid(row=rowCount, column=0,sticky = "NES")

        date = Label(window,text = el[1],width=11,bg = getCategoryColor(el[0]), borderwidth=0.5, relief="groove", font=('Arial',11))
        date.grid(row=rowCount, column=1,sticky = "NS")

        title = Label(window,text = el[2], width=69,bg = getCategoryColor(el[0]), borderwidth=0.5, relief="groove", font=('Arial',10),anchor='w')
        title.grid(row=rowCount, column=2,sticky = "NS")

        seeDetail = Button(window,text = "查看內容",width= 9,font=('Arial',10),bg = getCategoryColor(el[0]),command = lambda val=el,win = window : displayDetails(val,window))
        seeDetail.grid(row = rowCount, column = 3, padx = 5,sticky = "NWS")
        rowCount += 1
        
    #補上白塊
    if rowCount < 20:
        for i in range(20 - rowCount):
            category = Label(window,width=11,bg = "white", borderwidth=0.5, relief="groove", font=('Arial',11))
            category.grid(row=rowCount, column=0,sticky = "NES")

            date = Label(window,width=11,bg = "white", borderwidth=0.5, relief="groove", font=('Arial',11))
            date.grid(row=rowCount, column=1,sticky = "NS")

            title = Label(window, width=69,bg = "white", borderwidth=0.5, relief="groove",font=('Arial',10),anchor='w')
            title.grid(row=rowCount, column=2,sticky = "NS")

            seeDetail = Button(window,text = "無",width= 9,font=('Arial',10),bg = "white")
            seeDetail.grid(row = rowCount, column = 3, padx = 5,sticky = "NWS")
            rowCount += 1
