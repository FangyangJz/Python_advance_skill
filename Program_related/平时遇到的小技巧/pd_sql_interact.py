# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/10/18
'''
import traceback

__author__ = 'Fangyang'

import pandas as pd
from sqlalchemy import create_engine
import time
import os


db_info = {
    'user': 'root',
    'password': '123',
    'host': '192.168.3.155',
    'database': 'yldsj'  # 这里我们事先指定了数据库，后续操作只需要表即可
    }


kf_db = {
    'kf_daa01': ['JH', 'CYJH', 'YT', 'QKDY', 'XQKDM', 'QCDS1', 'QCDS2', 'YCDBS1',
                'YCDBS2', 'SCDS', 'CW', 'SKJDDS1', 'SKJDDS2', 'CS', 'SKYXHD', 'SKSYHD', 
                'YLSYHD', 'ELSYHD', 'MQJB', 'SJJB', 'TCJB', 'TCRQ', 'CM', 'KM', 'DM', 
                'DH', 'JLZH', 'YPFL', 'ZSRQ', 'JSRQ1', 'CQRQ', 'ZQRQ', 'YCZBSD', 'YSDCYL', 
                'YSBHYL', 'YSDCWD', 'PLYL', 'BGRQ', 'SCBZ', 'SCLX', 'SCZRRQ', 'SCJXRQ', 
                'HXSQRQ', 'FZRQ', 'ZCRQ', 'BFRQ', 'BFYY', 'BFFS', 'JWBZ', 'CXDM', 'BZ', 
                'QKDYDM', 'SKYCDS1', 'SKYCDS2', 'JSHD', 'CYRQ', 'HSRQ'],
    'kf_daa05': ['XCXH', 'JH', 'YCZMC', 'XCH', 'XFCH', 'CJX', 'SYDS', 'SYHD', 'YLSYDS', 
                'YLSYHD', 'YXHDDS', 'YXHD', 'YXHDLB', 'JCS', 'KXD', 'STLTZ', 'STL', 
                'SYJSJG', 'HYBHD', 'HQBHD', 'HSBHD', 'SFSBHD', 'SKQK', 'DCJSJG', 'BZ'],
    'kf_daa07': ['JH', 'YCFZMC', 'YCFZDS', 'HD', 'BSMS'],
    'kf_daa071': ['JH', 'XCXH', 'XCFZMC', 'XCFZDS', 'HD', 'BSMS'],
    'kf_daa091': ['JH', 'RQ', 'SKMD', 'JDDS1', 'JDDS2', 'XH', 'YCZMC', 'XCH', 'XFCH', 'FSL', 'JSXH', 'SKHD'],
    'kf_dba04': ['JH', 'NY', 'SCTS', 'CYFS', 'BJ', 'BS', 'PL', 'YZ', 'CC', 'CC1', 'YY', 
                'TY', 'LY', 'JY', 'DYM', 'JYM', 'RCYL', 'RCSL', 'RCQL', 'HS', 'SXDL', 'XXDL', 
                'DBDLC', 'YCYL', 'YCSL', 'YCQL', 'HSYCYL', 'HSYCSL', 'HSYCQL', 'NCYL', 'NCSL', 
                'NCQL', 'HSNCYL', 'HSNCSL', 'HSNCQL', 'LJCYL', 'LJCSL', 'LJCQL', 'HSLJCYL', 
                'HSLJCSL', 'HSLJCQL', 'CCJHWND', 'CCJND', 'CCBHJND', 'HSL1', 'BX', 'BZDM1', 
                'BZDM2', 'BZDM3', 'BZDM4', 'BZDM5', 'BZ', 'CW', 'SCJDDS', 'SCJDDS1', 'RCBZ', 'CCJHWND1'],
    'kf_dba08': ['JH', 'NY', 'XLJBZ', 'CSLB', 'CYCS1', 'CYCS2', 'CYCS3', 'WGRQ', 'CSQRCYL1', 'CSQRCYL', 'CZRCYL1', 
                'CZRCYL', 'MQZYSP1', 'MQZYSP', 'YZYL', 'YZYL1', 'YXTS', 'NLJZYL1', 'NLJZYL', 'SXRQ', 'KNBZ'],
    'kf_ddc10': ['JH', 'KGRQ', 'SGCW', 'SGJDDS1', 'SGJDDS2', 'XCS', 'YQJSMC', 'JSL', 'YLRQ', 'YLLX', 'YLYLX',
                 'YLYMC', 'JLJMC', 'JLJYL', 'JLB', 'TJJMC', 'TJJYL', 'ZCJMC', 'ZCJLD', 'ZCJYL', 'JSSJ', 'TQS',
                 'TQXZ', 'TQGG', 'PLYL', 'YQTBYL', 'YLSJ', 'PYFS', 'PCYL', 'LQZL', 'BZ', 'YLCX', 'CH', 'SKHD',
                 'YXHD', 'SGSJ', 'YLDW', 'YLYYL', 'JLJMC1', 'JLJYL1', 'SFJMC', 'SFJYL', 'XCJMC', 'XCJYL', 'QZYYL',
                 'QZYCO2YL', 'XSYYL', 'XSYCO2YL', 'TJYYL', 'TJCO2YL', 'LQYL', 'ZDJMC', 'ZDJYL', 'YHTBYL', 'PJSB', 'ZGSB']
}

kf_db_combine_primary_key = {
    'kf_daa01': ['JH'],
    'kf_daa05': ['XCXH', 'JH', 'YCZMC', 'XFCH'],
    'kf_daa07': ['JH', 'YCFZMC'],
    'kf_daa071': ['JH', 'XCXH', 'XCFZMC'],
    'kf_daa091': ['JH', 'RQ', 'JDDS1'],
    'kf_dba04': ['JH', 'NY'],
    'kf_dba08': ['JH', 'NY', 'CSLB', 'WGRQ'],
    'kf_ddc10': ['JH', 'KGRQ', 'SGJDDS1', 'YLRQ', 'YLCX']
}


def get_data_from_database(table_name, db_info):
    db_info = db_info
    engine = create_engine(
        'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**db_info), encoding='utf-8')
    # return pd.read_sql('SELECT * FROM `work-1`.work1_dep2', con=engine)
    print("Start to read [table:{0}] in [DB:{database}]".format(table_name, **db_info))
    return pd.read_sql(table_name, con=engine)


def save_df_to_database(df, table_name, db_info):
    ''' 传入dataframe, 给出数据库中的表名string, 存入数据库 '''
    db_info = db_info
    engine = create_engine(
        'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**db_info), encoding='utf-8')

    print("Start to save df into database...")
    start_time = time.time()
    df.set_index('JH', inplace=True)    # 设置井号为index, 作为数据库的主键
    try:
        df.to_sql(table_name, con=engine, if_exists='append')  # 如果表存在, 就append数据到表中
        print("Save dataframe data to database successfully. Cost {:.2f}s".format(time.time() - start_time))
    except Exception:
        traceback.print_exc()
    finally:
        engine.dispose()

def trans_xlsx_df_to_sql(file_name, table_name, db_info):
    '''将xlsx用pandas读取存入sql数据库'''
    df = get_data_from_file(file_name)
    df_columns_base_db = kf_db[table_name]
    # 数据columns 和 数据库中的表 取交集
    df = df[list(set(df_columns_base_db) & set(df.columns))]
    # 联合主键去重
    df.drop_duplicates(kf_db_combine_primary_key[table_name], keep='last', inplace=True)
    print('Total {} rows data wait to insert into DB'.format(len(df)))
    save_df_to_database(df, table_name, db_info)


def get_file_abs_path(file_name=''):
    ''' 文件和脚本在同目录下, 返回文件的原始字符串'''
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


def get_data_from_file(file_name):
    print('Start read {} file into pandas...'.format(file_name))
    start_time = time.time()
    df = pd.read_excel(get_file_abs_path(file_name))
    print('Read df successful.Cost {:.2f}s'.format(time.time() - start_time))
    return df


if __name__ == '__main__':

    # # 从数据库中读取数据并打印
    # start_time = time.time()
    # table_name = 'well_source'
    # data = get_data_from_database(table_name, db_info)
    # end_time = time.time()
    # print(data.info(verbose=False))
    # print(data)
    # print('Cost time is {:.2f}s'.format(end_time - start_time))

    files_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    for i in files_list:
        if os.path.splitext(i)[1] == '.xlsx':
            table_name = 'kf_' + os.path.splitext(i)[0].lower()
            trans_xlsx_df_to_sql(i, table_name, db_info)
            print('-'*50)

