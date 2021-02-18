import easygui as g
import numpy as np
import requests,openpyxl
import datetime
import pandas as pd
#msg = "请输入URL地址"
#title = "数据爬取"
#url = g.enterbox(msg,title)  #设置显示内容、标题、输入下上界
#url = 'https://www.cp550.com/data/bjpk10/lotteryList/2019-01-02.json?KJXTURH3UD9JAVWD2RMH'


def getDatesByTimes(sDateStr, eDateStr):
    list = []
    datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
    list.append(datestart.strftime('%Y-%m-%d'))
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        list.append(datestart.strftime('%Y-%m-%d'))
    return list

def spider(url,sheet):
	res_data = requests.get(url)

	# 调用get方法，下载这个字典
	json_data = res_data.json()
	
	data_len = len(json_data[0]['openNum'])
	#初始化第一行
	for count in range(data_len+1):
		if count < data_len:
			sheet[chr(ord('A')+count)+'1'] = "第{}列".format(count+1)
		else :
			sheet[chr(ord('A')+count)+'1'] = "结果"
	#根据爬取信息填充数据
	for i in json_data:
		#print(i['openNum'])
		data_list = list(np.array(i['openNum'])- np.arange(1,data_len+1))
		result = -data_list.count(0) +1
		data_list.append(result)
		sheet.append(data_list)
	
	#获取文件名并保存
	#filename = url.split('/')[-1].split('.')[0]
	#sheet.append(["_" for i in range(data_len + 1)])
	#wb.save(filename+'.xlsx')
	
def _input():
    msg = "请输入固定值、范围、条件"
    title = "判断"
    fieldNames = ["固定值","范围","条件"]
    #fieldValues = []
    fixed_nums,range_num,condition = g.multenterbox(msg,title,fieldNames)
    fixed_nums = list(map(int,fixed_nums.strip().split(" ")))
    return fixed_nums,int(range_num),condition
	
def data_analyis(filename,fixed_nums,range_num,condition):
	df=pd.read_excel(filename)#这个会直接默认读取到这个Excel的第一个表单
	df["一二列求和"] = df["第1列"] + df["第2列"]
	data = list(df["一二列求和"])
	count = 0
	if condition == '>':
		for value in fixed_nums:
			for i in range(len(data)):
				if data[i] == value and i!=0:
					if data[i-range_num] > value:
						count +=1
	elif condition == '<':
		for value in fixed_nums:
			for i in range(len(data)):
				if data[i] == value and i!=0:
					if data[i-range_num] > value:
						count +=1
	return count
	
	
if __name__ == '__main__':
	#print('a')
	msg = "请填写一下起止日期"
	title = "数据批量爬取"
	fieldNames = ["开始日期","截至日期"]
	#fieldValues = []
	start_date,end_date = g.multenterbox(msg,title,fieldNames)
	data_list =  getDatesByTimes(start_date, end_date)
	##创建excel文件
	wb=openpyxl.Workbook()  
	#创建工作薄
	sheet=wb.active 
	#获取工作薄的活动表
	sheet.title='openNum' 
	for date in data_list:
		print("正在爬取{}的数据".format(date))
		url = 'https://www.cp550.com/data/bjpk10/lotteryList/{}.json?KJXTURH3UD9JAVWD2RMH'.format(date)
		spider(url,sheet)
	filename = start_date+'--'+end_date
	wb.save(filename+'.xlsx')
	fixed_nums,range_num,condition = _input()
	count = data_analyis(filename+'.xlsx',fixed_nums,range_num,condition)
	print(count)
	title = g.msgbox(msg="符合条件的总计{}！".format(count),title="j结果",ok_button="YES")
	