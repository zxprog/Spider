import easygui as g
import numpy as np
import requests,openpyxl
import datetime
import pandas as pd

def _input():
    msg = "请输入固定值、范围、条件"
    title = "判断"
    fieldNames = ["固定值","范围","条件","比较值"]
    #fieldValues = []
    fixed_nums,range_num,condition,compare = g.multenterbox(msg,title,fieldNames)
    fixed_nums = list(map(int,fixed_nums.strip().split(" ")))
    return fixed_nums,int(range_num.strip()),condition.strip(),int(compare.strip())
	
def data_analyis(filename,fixed_nums,range_num,condition,compare):
	df=pd.read_excel(filename)#这个会直接默认读取到这个Excel的第一个表单
	df["一二列求和"] = df["第1列"] + df["第2列"]
	data = list(df["一二列求和"])
	print(max(data))
	count = 0
	count_fixed = 0
	if condition == '>':
		for value in fixed_nums:
			for i in range(len(data)):
				if data[i] == value and i!=0 and i-range_num>=0:
					count_fixed += 1
					for j in range(1,range_num+1):
						if data[i-j] > compare:
							count +=1
							break
	elif condition == '<':
		for value in fixed_nums:
			for i in range(len(data)):
				if data[i] == value and i!=0 and i-range_num>=0:
					count_fixed += 1
					for j in range(1,range_num+1):
						if data[i-j] < compare:
							count +=1
							break
	return count_fixed,count
	
	
if __name__ == '__main__':
	#print('a')
	msg = "请填写一下文件名"
	title = "数据分析"
	fieldNames = ["文件名"]
	#fieldValues = []
	filename = g.multenterbox(msg,title,fieldNames)[0]
	fixed_nums,range_num,condition,compare = _input()
	count_fixed,count = data_analyis(filename,fixed_nums,range_num,condition,compare)
	print(count_fixed,count)
	title = g.msgbox(msg="固定值有{}个！ 符合条件的总计{}！".format(count_fixed,count),title="结果",ok_button="YES")