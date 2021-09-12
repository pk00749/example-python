#-----------init----------
engine = create_engine()

metadata = MetaData(engine)

tpam_cpai_account_data = Table('tpam_cpai_account_data', metadata,
                            Column('id', Integer, primary_key=True, autoincrement=True),
                            Column('', String(50)),
                            )

metadata.create_all()

tpam_cpai_account_data =  Table('tpam_cpai_account_data', metadata, autoload=True)


#-------------------------
has_table = db.engine.dialect.has_table(db.engine.connect(), 'tpam_cpai_account_data')
if not has_table:
    tpam_cpai_account_data = Table('tpam_cpai_account_data', metadata,
                            Column('', Integer, primary_key=True),
                            Column('', String(50)),
                            )
    metadata.create_all()
else:
    tpam_cpai_account_data =  Table('tpam_cpai_account_data', metadata, autoload=True)

#----------------------
import numpy
import pandas as pd
#
# df = pd.DataFrame({"id":[1,2,3,4,5,6,7], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e','f']})
#
# # 把raw_grade转化成category类型
# df["grade"] = df["raw_grade"].astype("category")
#
# # 相当于给上面的raw_grade的值(a,b,e,f)重命名
# # df["grade"].cat.categories = ["very good", "good", "bad", "very bad"]
#
# # 补齐其他缺漏的种类
# # df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good","The best"])
# df["grade"] = df["grade"].cat.set_categories(["a", "b", "c", "d", "e", "f"])
#
# df = df.sort_values(by="grade")
# print df
#
# print df['grade'].value_counts()
# print df.groupby(by="grade").size()


# data =numpy.arange(0, 16).reshape(4,4)
# data = pd.DataFrame(data, columns=['0','1','2','3'])
# def f(x):
#     return x-1
# print(data)
# print(data.ix[:,['1']].apply(f))
# print(data)

# import pandas as pd
#
# lst = [
#     ['A','x',0],
#     ['B','x',0],
#     ['A','x',0],
#     ['B','y',0],
# ]
#
# def f(x):
#     return x
#
# df = pd.DataFrame(lst)
# # print(df[0])
# # df[2] = df.apply(lambda x: df[0], axis=1)
#
# df[2] = df.apply(f, axis=1)
# print(df)


import pandas as pd
import numpy as np
obj = pd.Series(range(4), index=['d', 'b', 'a', 'c'])
print(obj)
print(obj.reindex(['a', 'b', 'c', 'd', 'e']))

# import pandas as pd
import numpy as np
# print(obj)
# print(obj.reindex(['a', 'b', 'c', 'd', 'e']))

# import pandas as pd
# data = [[1,2,3],[4,5,6]]
# index = ['0','1']
# columns=['a','b','c']
# df = pd.Series(range(4), index=['d', 'b', 'a', 'c'])
# df = pd.DataFrame(data=range(4), index=index, columns=columns)
# print(type(df))

# index_new = ['3','4']
# df = df.reindex(index=index_new)
# test = df.loc[:,['a']]
# test_2 = df.iloc[:,1]
# print(test_2.index)
# test_2 = test_2.reindex(['3','4'])
# print(df)
# print(type(test_2))
# print(test_2)
# print(type(test))
# # print(df.loc[1])
# '''''
# a    4
# b    5
# c    6
# '''
#
#
# dd1=df.reindex(index=index_new)
# print(dd1)

# import pandas as pd
# data = [[1,2,3],[4,5,6]]
# index = ['d','e']
# columns=['a','b','c']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# print df.loc['d',['b','c']]
# '''''
# b    2
# c    3
# '''


# import pandas as pd
# data = [[1,2,3],[4,5,6]]
# index = ['d','e']
# columns=['a','b','c']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# print df.loc[:,['c']]
# '''''
#    c
# d  3
# e  6
# '''

