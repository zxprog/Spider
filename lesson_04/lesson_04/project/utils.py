# -*- coding: utf-8 -*-

"""
    作者:     Robin
    版本:     1.0
    日期:     2019/01
    文件名:    utils.py
    功能：     工具文件

    声明：小象学院拥有完全知识产权的权利；只限于善意学习者在本课程使用，
         不得在课程范围外向任何第三方散播。任何其他人或机构不得盗版、复制、仿造其中的创意，
         我们将保留一切通过法律手段追究违反者的权利
"""
import numpy as np
import datetime


def load_data(filename, use_cols):
    """
        读取指定列的CSV数据
    """
    # 读取列名，即第一行数据
    with open(filename, 'r') as f:
        col_names_str = f.readline()[:-1]  # [:-1]表示不读取末尾的换行符'\n'

    # 将字符串拆分，并组成列表
    col_name_lst = col_names_str.split(',')

    # 获取相应列名的索引号
    use_col_index_lst = [col_name_lst.index(use_col_name) for use_col_name in use_cols]

    # 读取数据
    data_array = np.loadtxt(filename,       # 文件名
                            delimiter=',',  # 分隔符
                            skiprows=1,     # 跳过第一行，即跳过列名
                            dtype=str,      # 数据类型
                            usecols=use_col_index_lst)  # 指定读取的列索引号
    return data_array


def process_date(data_array):
    """
        处理日期格式数据，转换为yyyy-mm字符串
    """
    enddate_lst = data_array[:, 0].tolist()

    # 将日期字符串格式统一，即'yy/dd/mm'
    enddate_lst = [enddate.replace('-', '/') for enddate in enddate_lst]

    # 将日期字符串转换成日期
    date_lst = [datetime.datetime.strptime(enddate, '%m/%d/%Y') for enddate in enddate_lst]

    # 构造年份-月份列表
    month_lst = ['{}-{:02d}'.format(date_obj.year, date_obj.month) for date_obj in date_lst]

    month_array = np.array(month_lst)

    data_array[:, 0] = month_array

    return data_array


def get_month_stats(data_array):
    """
        统计每月的投票数据
    """
    months = np.unique(data_array[:, 0])
    for month in months:
        # 根据月份过滤数据
        filtered_data = data_array[data_array[:, 0] == month]

        # 获取投票数据，字符串数组转换为数值型数组
        try:
            filtered_poll_data = filtered_data[:, 1:].astype(float)
        except ValueError:
            # 遇到不能转换为数值的字符串，跳过循环
            continue

        result = np.sum(filtered_poll_data, axis=0)

        # 在列方向求和
        print('{}，Clinton票数：{}，Trump票数：{}'.format(month, result[0], result[1]))
