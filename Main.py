from tkinter import *
import webbrowser

#以下是自己寫的程式
from UtilFunctions import *
from DataClass import *
from IndexCountClass import *

def main():
    #把會用到的class先創造一個instance
    data = Data()
    indexCount = IndexCount()

    #標題與基本設定
    window = Tk()
    window.title("東吳資管系 公告小助手")
    window.geometry("1000x630")
    Label(window, text = "東吳資管系 公告小助手",font=('Arial',25,'bold')).grid(row = 0, column = 2)
    Label(window, text = "BY  陳韻安 ❤❤❤",font=('Arial',10)).grid(row = 0, column = 3,columnspan = 2, padx = 10,sticky = SE)

    #篩選資料
    Label(window, text = "篩選資料： ",font=('Arial',14,'bold')).grid(row = 1, column = 0, sticky = "E")
    Button(window,text = "程式檢定",width= 8,bg = "#ffcccc",font=('Arial',11,'bold'),command = lambda  : initTable(data.filterData("程式檢定",indexCount), indexCount,window)).grid(row = 1, column = 1, padx = 10)
    Button(window,text = "程式競賽",width= 8,bg = "#ffe0b3",font=('Arial',11,'bold'),command = lambda  : initTable(data.filterData("程式競賽",indexCount), indexCount,window)).grid(row = 1, column = 2, padx = 10,sticky = W)
    Button(window,text = "講座",width= 8,bg = "#b3ffb3",font=('Arial',11,'bold'),command = lambda  : initTable(data.filterData("講座",indexCount), indexCount,window)).grid(row = 1, column = 2, padx = (120,10),sticky = W)
    Button(window,text = "獎助學金",width= 8,bg = "#cce6ff",font=('Arial',11,'bold'),command = lambda  : initTable(data.filterData("獎助學金",indexCount), indexCount,window)).grid(row = 1, column =2, padx = 10)
    Button(window,text = "實習",width= 8,bg = "#b3cbe6",font=('Arial',11,'bold'),command = lambda  : initTable(data.filterData("實習",indexCount), indexCount,window)).grid(row = 1, column = 2, padx = (10,120),sticky = E)
    Button(window,text = "課程",width= 8,bg = "#eeccff",font=('Arial',11,'bold'),command = lambda  : initTable(data.filterData("課程",indexCount), indexCount,window)).grid(row = 1, column = 2, padx = 10,sticky = E)
    Button(window,text = "其他",width= 8,bg = "white",font=('Arial',11,'bold'),command = lambda : initTable(data.filterData("其他",indexCount), indexCount,window)).grid(row = 1, column =  3, padx = 10)
    Button(window,text = "所有資料",width= 8,bg = "white",font=('Arial',11,'bold'),fg = 'blue',command = lambda : initTable(data.filterData("ALL",indexCount), indexCount,window)).grid(row = 1, column = 4, padx = 10)

    #搜尋框
    Label(window, text = "搜尋關鍵字： ",font=('Arial',14,'bold')).grid(row = 2, column = 0,pady = 5, sticky = "E")
    searchString = StringVar()
    Entry(window, textvariable = searchString,font=('Arial',15,'bold')).grid(row = 2, column = 1, padx = (10,150),columnspan = 2, sticky = EW,pady = 5)
    Button(window,text = "搜尋",width= 8,height = 1,font=('Arial',15),command = lambda : initTable(data.searchData(searchString.get(),indexCount), indexCount,window) ).grid(row = 2, column = 2,padx = (0,50), sticky = E,pady = 5)

    #表格標題
    Label(window,text = "類別",width=8,bg ="white", borderwidth=0.5, relief="groove",font=('Arial',14,'bold')).grid(row=3, column=0,sticky = "NES")
    Label(window,text = "日期",width=8,bg = "white", borderwidth=0.5, relief="groove",font=('Arial',14,'bold')).grid(row=3, column=1,sticky = "NS")
    Label(window,text = "標題", width=46,bg = "white", borderwidth=0.5, relief="groove",font=('Arial',15,'bold')).grid(row=3, column=2,sticky = "NS")

    #一開起來時，會需要整理一次資料，作為初始表格顯示
    initTable(data.getData(),indexCount,window)

    #處理分頁
    Button(window,text = "下一頁",width= 8,fg = 'blue',bg = "white",font=('Arial',12,'bold'),command = lambda  : indexCount.addIndex(data,indexCount,window)).grid(row = 21, column = 2, pady = 7, sticky = E)
    Button(window,text = "上一頁",width= 8,fg = 'blue',bg = "white",font=('Arial',12,'bold'),command = lambda : indexCount.decreaseIndex(data,indexCount,window)).grid(row = 21, column = 2, pady = 7, sticky = W)

    window.mainloop()


main()
