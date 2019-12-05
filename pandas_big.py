# 导入必要模块
# import pandas as pd
# from sqlalchemy import create_engine
# import time
# # 初始化数据库连接，使用pymysql模块
# engine = create_engine('mysql+mysqlconnector://root:550053632@localhost:3306/big_data')
#
# # print(engine)
# # 读取本地CSV文件
# df = pd.read_csv("C:/Users/55005/Desktop/train.csv",nrows =100000)
# # print(df)
# df["A"] = ""
# df["B"] = ""
# df["C"] = ""
# df["D"] = ""
# # 将新建的DataFrame储存为MySQL中的数据表，不储存index列
# df.to_sql('mpg', engine, index= False,chunksize=500)
# print('总时间: %s'%(time.time()))




print([a for a in range(8) if a >3])