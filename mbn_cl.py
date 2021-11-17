import pandas as pd 
import numpy as np
#import xlwings as xw
import openpyxl 
import xlrd
#E:/down/打字练习/蓝宝石/后五百.xlsx
#E:/down/python2/study/datasanalys/test2.xlsx
#E:/down/打字练习/蓝宝石/匠心雨码表/匠士雨词库1.6.xlsx
file_path='E:/down/python2/study/datasanalys/test2.xlsx'
df = pd.read_excel('E:/down/打字练习/蓝宝石/匠心雨码表/匠士雨词库1.6.xlsx') 
# 现在查询成绩就可以写成如下风格,如查询李四语文成绩
df=pd.DataFrame(df)
bmcd=df[df.编码.str.len() ==1]

#print (bmcd)
''' 
writer = pd.ExcelWriter('test.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
''' 
#writer = pd.ExcelWriter('test.xlsx')
#writer = pd.ExcelWriter('test.xlsx','Sheet1')
#bmcd.to_excel('test.xlsx','Sheet1')
#writer.save()
 
book = openpyxl.load_workbook(file_path) #读取你要写入的文件路径
#和pd.read_excel() 用于将Dataframe写入excel xls用xlwt。xlsx用openpyxl
writer = pd.ExcelWriter(file_path, engine='openpyxl')
##此时的writer里还只是读写器. 然后将上面读取的book复制给writer
writer.book = book
#转化为字典的形式
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
#将data写入writer
bmcd.to_excel(writer,sheet_name="一码字词",index=False)
writer.save()

''' 
def excelAddSheet():
	DataFrame=bmcd
	sheet_name='3'
	writer = pd.ExcelWriter(file_path, engine='openpyxl')
	writer.book=book
	writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
	DataFrame.to_excel(writer,sheet_name ="sheet_name",index=False)
	writer.save()
print(excelAddSheet)
'''
