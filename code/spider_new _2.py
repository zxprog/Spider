import easygui as g
import numpy as np
import requests,openpyxl
import datetime
#msg = "请输入URL地址"
#title = "数据爬取"
#url = g.enterbox(msg,title)  #设置显示内容、标题、输入下上界
#url = 'https://www.cp550.com/data/bjpk10/lotteryList/2019-01-02.json?KJXTURH3UD9JAVWD2RMH'


def getDatesByTimes(sDateStr, eDateStr):
    list = []
    datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
    list.append(datestart.strftime('%Y-%m-%d'))
    while datestart <= dateend:
        datestart += datetime.timedelta(days=1)
        list.append(datestart.strftime('%Y-%m-%d'))
    return list

def spider(url):
	res_data = requests.get(url)

	# 调用get方法，下载这个字典
	json_data = res_data.json()
	##创建excel文件
	wb=openpyxl.Workbook()  
	#创建工作薄
	sheet=wb.active 
	#获取工作薄的活动表
	sheet.title='openNum' 
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
	filename = url.split('/')[-1].split('.')[0]
	wb.save(filename+'.xlsx')
	
if __name__ == '_main_':
	
	msg = "请填写一下起止日期"
	title = "数据批量爬取"
	fieldNames = ["开始日期","截至日期"]
	#fieldValues = []
	start_date,end_date = g.multenterbox(msg,title,fieldNames)
	data_list =  getDatesByTimes(start_date, end_date)
	for date in data_list:
		url = 'https://www.cp550.com/data/bjpk10/lotteryList/{}.json?KJXTURH3UD9JAVWD2RMH'.format(date)
		spider(url)
	



