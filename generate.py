# 导入random包
import random

count = 500

#大模型测试结果
result_file = open('./assistant_learn/fo_result.txt', 'w')  #`

for index in range(count):

    #个数
    num = random.sample(range(1,6),1)[0]

    random_list = random.sample(range(1,136),num)
    print(random_list)
    clear = random.random()
    if clear <0.1:
        random_list = []
    result_file.write(str(random_list)+"\r") 


result_file.close()



#真实标注数据
mark_file = open('./source/violation_index.txt', 'w')  #`

for index in range(count):

    #个数
    num = random.sample(range(1,4),1)[0]

    random_list = random.sample(range(1,136),num)
    print(random_list)
    mark_file.write(str(random_list)+"\r") 


mark_file.close()



