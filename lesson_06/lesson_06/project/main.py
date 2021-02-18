# -*- coding: utf-8 -*-

"""
    作者:     Robin
    版本:     1.0
    文件名:    main.py
    功能：     主程序

    实战：互联网电影资料库分析

    任务：
        - 使用分组统计查看票房收入统计
        - 基于电影类型的数据分析

    声明：小象学院拥有完全知识产权的权利；只限于善意学习者在本课程使用，
         不得在课程范围外向任何第三方散播。任何其他人或机构不得盗版、复制、仿造其中的创意，
         我们将保留一切通过法律手段追究违反者的权利
"""
import pandas as pd
import utils

# 设置显示的最多列数
pd.set_option('display.max_columns', 10)

dataset_path = './dataset/movie_metadata.csv'


def main():
    """
        主函数
    """
    # 加载数据
    df_data = pd.read_csv(dataset_path)
    
    # 查看数据
    utils.inspect_data(df_data)
    
    # 处理缺失数据
    df_data = utils.process_missing_data(df_data)
    
    # 任务1：使用分组统计查看票房收入统计
    # 导演vs票房总收入
    utils.analyse_gross(df_data, ['director_name'], './output/director_gross.csv')
    
    # 主演vs票房总收入
    utils.analyse_gross(df_data, ['actor_1_name'], './output/actor_gross.csv')
    
    # 导演+主演vs票房收入
    utils.analyse_gross(df_data, ['director_name', 'actor_1_name'], './output/director_actor_gross.csv')
     
    # 任务2：基于电影类型的数据分析
    df_genres = utils.get_genres_data(df_data[['movie_title', 'genres']])
    genres_count = df_genres.groupby('genres').size().sort_values(ascending=False)
    genres_count.to_csv('./output/genres_stats.csv')

    
if __name__ == '__main__':
    main()
