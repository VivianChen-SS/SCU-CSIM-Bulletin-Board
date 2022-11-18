#【參考課本P299頁】
from UtilFunctions import *

class IndexCount:
    def __init__(self):
        self._startIndex = 0
        self._endIndex = 14
    
    def addIndex(self,data,indexCount,window):
        length = data.getLength()
        self._startIndex  = self._endIndex + 1 if length > self._endIndex + 1 else self._startIndex #使用length > self._endIndex + 1是因為length和index差一，在右邊+1補回來才好比對，跟左邊的+1意思不同
        self._endIndex = self._endIndex + 15 if length > self._endIndex + 15 else length - 1
        initTable(data.getData(),indexCount,window)
        
    def decreaseIndex(self,data,indexCount,window):
        self._endIndex  = self._startIndex -1 if self._startIndex - 15 >= 0 else self._endIndex
        self._startIndex = self._startIndex - 15 if self._startIndex - 1 >= 0 else self._startIndex
        initTable(data.getData(),indexCount,window)
        
    def getStartIndex(self):
        return self._startIndex
    
    def getEndIndex(self):
        return self._endIndex
    
    def initIndexAfterFilter(self,len):
        self._startIndex = 0
        self._endIndex = len if len < 15 else 14
