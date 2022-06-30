import openpyxl

class Write_excel():
    def __init__(self,filepath,filename,sheet,data):
        self.wb=openpyxl.Workbook()  #创建一个空表
        self.ws=self.wb.active       #表格操作
        self.data=data               #数据实例化
        self.filepath=filepath       #存储地址绝对地址实例化
        self.filename=filename       #文件名实例化
        self.ws.title = sheet        #sheet名字
    def write_result(self):
        for i in self.data:
            self.ws.append([i])      #写入excel表格
        self.wb.save(self.filepath+self.filename)   #保存文件