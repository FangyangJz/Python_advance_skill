db_info = {'user': 'root',
           'password': '123',
           'host': '192.168.3.155',
           'database': 'yldsj'  # 这里我们事先指定了数据库，后续操作只需要表即可
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
    df.to_sql(table_name, con=engine, if_exists='append')  # 如果表存在, 就append数据到表中
    print("Save dataframe data to database successfully. Cost {:.2f}s".format(time.time() - start_time))