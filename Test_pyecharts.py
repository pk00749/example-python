# from pyecharts import Map
#
# value = [155,10,66,78,33,80,190,53,49.6]
# attr = ['福建','山东','北京','甘肃','新疆','河南','广西','西藏']
# map = Map("Test", width=1200, height=600)
# map.add("",attr,value,maptype='china',is_visualmap=True,visual_text_color='#000')
# map.show_config()
# map.render()


# from pyecharts import Map
#
# value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
# attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
# map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
# map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
# map.show_config()
# map.render()


# from pyecharts import Map
#
# value = [155, 10, 66, 78]
# attr = ["福建", "山东", "北京", "上海"]
# map = Map("全国地图示例", width=1200, height=600)
# map.add("", attr, value, maptype='china')
# map.show_config()
# map.render()


# from pyecharts import Map
#
# value = [20, 190, 253, 77, 65]
# attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
# map = Map("广东地图示例", width=1200, height=600)
# map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
# map.show_config()
# # map.render()
# map.render_notebook()

import pandas as pd
from pyecharts import Map
# import collections
# value = collections.OrderedDict()
# loc = pd.DataFrame(pd.read_csv(r'G:/Program/Projects/Apolo/data/stock_basics/20170601.csv', encoding='gbk'))
# loc = loc[['area']]
# value = pd.Series.value_counts(loc.iloc[:,0])
# value = value.to_dict()
# attr = dict.keys(value)
# value = list(value.values())
#
# print(type(attr))
value = [375, 351, 294, 519, 263, 182, 125, 111, 98, 95, 93, 76, 75, 54, 50, 47, 47, 46, 42, 38, 37, 36, 35, 32, 31, 30, 25, 24, 14, 12, 11]
attr = ['浙江', '江苏', '北京', '广东', '上海', '山东', '福建', '四川', '安徽', '湖北', '湖南', '河南', '辽宁', '河北', '新疆', '天津', '重庆', '陕西', '吉林', '山西', '江西', '广西', '黑龙江', '云南', '甘肃', '海南', '内蒙古', '贵州', '西藏', '宁夏', '青海']
# 269 250
map = Map("全国地图示例", width=1000, height=600)
map.add("", attr, value, maptype='china',is_visualmap=True, visual_range=[0, 550], visual_text_color='#000')
map.show_config()
map.render_notebook()


