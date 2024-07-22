import json
import requests

api = "http://119.3.184.126:4338/service/api/annotations"

#过滤器项目选择
filter_project = "filters[project]=1"

#查询索引开始
index_start = 1
pagination_start = "pagination[start]="+str(index_start)

#查询索引数目
index_count = 523   #project = 1   
# index_count = 403 #project = 2
pagination_limit = "pagination[limit]="+str(index_count)

#photo
photo_shootingTime = "populate[photo][fields][0]=shootingTime"
photo_id = "populate[photo][populate][image][fields][0]=id"
photo_url = "populate[photo][populate][image][fields][1]=url"

#请求头 校验
headers =  {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NiwiaWF0IjoxNzE5MTkyMTcyLCJleHAiOjE3MjE3ODQxNzJ9.-r0kWG3Eus6A1vBUE81dp46vC-_H47aknBW22G0NiFM'}

#获取批量返回的违规数据
url = api+"?"+filter_project+"&"+pagination_start+"&"+pagination_limit+"&"+photo_shootingTime+"&"+photo_id+"&"+photo_url
response = requests.get(url,headers=headers)
#data包含了index_count条数据
data = json.loads(response.content)

#构造训练集
'''
{
    "data_set": [
        {
            "img_id": "1",
            "img_url": "url",
            "violations": [
                "rule_id1",
                "rule_id2"
            ]
        }
    ]
}
'''

img_dict = {}
data_set_array = []

#遍历
for unit in data['data']:
    data_set_unit = {}

    #单元构造
    data_set_unit['img_id'] = unit['id']
    data_set_unit['img_url'] = unit['attributes']['photo']['data']['attributes']['image']['data']['attributes']['url']
    data_set_unit['violation'] = unit['attributes']['description']

    #json数组添加
    data_set_array.append(data_set_unit)
    print(unit['attributes']['description'])

#嵌套
img_dict["data_set"] = data_set_array

img_json = json.dumps(img_dict,ensure_ascii=False)


#添加训练集
with open('./source/train.txt', 'w') as f:
    f.write(str(img_json)+"\r\n")

