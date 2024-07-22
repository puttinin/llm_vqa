
#转换结果
result_file = open('./source/result.txt', 'r')

results = result_file.readlines()

result_file.close()

#转换结果
violation_file = open('./source/violation_index.txt', 'w')

#三个布尔分别对应索引为43 10 36的规范
for result_list in results:
    result = eval(result_list)
    print(result)
    violation_index = []
    if(result[0]==1):
        violation_index.append(43)
    if(result[1]==1):
        violation_index.append(10)
    if(result[2]==1):
        violation_index.append(36)
    violation_file.write(str(violation_index)+"\r")   
 

violation_file.close()