import json
import csv

#测试集json格式
# json_file = open('./source/regulationsInformat.json', 'w',encoding='utf-8')

regulation_file = open('regulations.json', 'r',encoding="utf-8")

regulation_str = regulation_file.read()
regulation_file.close()

regulation_json = json.loads(regulation_str)

json_data = {}

regulation_count = 0
for each in regulation_json['safety']:
  for each_name in each['description']:
    
    regulation_count = regulation_count + 1
    json_data[str(regulation_count)] = str(each_name['name'])

    

print(regulation_count)

print(json_data)

with open('my_file.csv', 'w', newline='',encoding='utf-8') as f:
    labels = ["index","regulation"]
    writer = csv.DictWriter(f, fieldnames=labels)
    writer.writeheader()
    for key,value in json_data.items():
       data = {"index":key,"regulation":value}
       writer.writerow(data)


# json.dump(json_data,json_file,ensure_ascii=False)  

# json_file.close()




