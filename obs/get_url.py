import json
import requests


#添加训练集
with open('./source/train.txt', 'r') as f:
    img_str = f.read()

img_json = json.loads(img_str)

# print(len(img_json['data_set']))    #500


# for unit in img_json['data_set']:
#     print(unit['img_url'])

date_t = "2024/01/01"
path_header = "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/"
filePath = "cms/2024/06/20/"
for index in range(1):
    #切片获取文件索引,id
    dst = img_json['data_set'][index]['img_url'][len(path_header):]
    id = dst[len(filePath):]
    path = dst[:len(filePath)]
    print(path,id)




