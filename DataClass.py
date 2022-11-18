from CrawlerFunctions import *

class Data:
    def __init__(self):
        self._data = getData() #會因為搜尋而更動的資料
        self._backupData = getData() #init出來以後就不再更動的資料 (以防每次搜尋都要再爬一次資料比較耗時)
    
    def filterData(self,query,indexCount):
        if query == "ALL":
            self._data = self.getBackupData() 
            indexCount.initIndexAfterFilter(self.getLength())
        else:
            temp = self.getBackupData() #如果直接從A filter跳到 B filter，A裡面不包含B，所以B無法顯示，必須加這行重整一遍
            self._data = [el for el in temp if el[0] == query] 
            indexCount.initIndexAfterFilter(self.getLength())
        return self._data
    
    def searchData(self,searchstr,indexCount):
        temp = self.getBackupData() #如果直接從A filter跳到 B filter，A裡面不包含B，所以B無法顯示，必須加這行重整一遍
        self._data = [el for el in temp if searchstr in el[2]] 
        indexCount.initIndexAfterFilter(self.getLength())
        return self._data
    
    def getData(self):
        return self._data
    
    def getLength(self):
        return len(self._data)
    
    def getBackupData(self):
        return self._backupData
