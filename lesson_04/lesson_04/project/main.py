# -*- coding: utf-8 -*-

"""
    作者:     Robin
    版本:     1.0
    日期:     2019/01
    文件名:    main.py
    功能：     主程序

    实战：2016美国大选分析

    任务：
        - 分析每个月的民意调查统计趋势

    声明：小象学院拥有完全知识产权的权利；只限于善意学习者在本课程使用，
         不得在课程范围外向任何第三方散播。任何其他人或机构不得盗版、复制、仿造其中的创意，
         我们将保留一切通过法律手段追究违反者的权利
"""

import utils

# 数据文件地址
filename = './presidential_polls.csv'


def main():
    """
        主函数
    """
    # 读取指定列的数据
    use_cols = ['enddate', 'rawpoll_clinton', 'rawpoll_trump']
    data_array = utils.load_data(filename, use_cols)

    # 处理日期格式数据，转换为yyyy-mm字符串
    proc_data_array = utils.process_date(data_array)

    # 统计每月的投票数据
    utils.get_month_stats(proc_data_array)


if __name__ == '__main__':
    main()
