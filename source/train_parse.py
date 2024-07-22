import json
import requests


#添加训练集
with open('./source/train.txt', 'r') as f:
    img_str = f.read()

img_json = json.loads(img_str)

print(len(img_json['data_set']))    #500

#对应序号为 10 36 43
violation_list = ['人员未佩戴安全帽','失去保护','未穿戴反光背心']

# for unit in img_json['data_set']:
#     print(unit['img_url'])

for index in range(10):
    print(img_json['data_set'][index]['img_url'])

def violation_fullfill(violation_list,violations:str,Blist):
    violation_num = len(violation_list)    
    for i in range(violation_num):
        if violation_list[i] in violations:
            Blist[i] = 1


#训练集结果
with open('./source/result.txt', 'w') as f:
    for unit in img_json['data_set']:

        violations_bit = []
        for i in range(3):
            violations_bit.append(0)

        violations = unit['violation']

        violation_fullfill(violation_list=violation_list,violations=violations,Blist=violations_bit)
        
        print(violations,violations_bit)

        f.write(str(violations_bit)+"\r")

