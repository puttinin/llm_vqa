import numpy as np
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score

#结果个数
result_num = 50

#条例数目
regulation_num = 3


#LLM预测结果
LLM_result = np.zeros((regulation_num,result_num))

fo_file = open('./FO_test/chatgpt4o_result.txt', 'r')

lines = fo_file.readlines()
for i in range(result_num):
    list_str = lines[i]
    result_list = eval(list_str)
    for j in range(regulation_num):
        LLM_result[j][i] = result_list[j]


fo_file.close()
print(LLM_result)


#正确数据
real_result = np.zeros((regulation_num,result_num))

real_file = open('./source/result.txt', 'r')
for i in range(result_num):
    result_str = real_file.readline()
    result_list = eval(result_str)
    for j in range(regulation_num):
        real_result[j][i] = result_list[j]

real_file.close()

print(real_result)



#分别对于每一项条例的性能计算
for j in range(regulation_num):
    
    #正确率
    acc = accuracy_score(y_true=real_result[j], y_pred=LLM_result[j])

    #精确率
    pre = precision_score(y_true=real_result[j], y_pred=LLM_result[j], zero_division=1)

    #召回率
    recall = recall_score(y_true=real_result[j], y_pred=LLM_result[j], zero_division=1)

    #f1_score
    f1 = f1_score(y_true=real_result[j], y_pred=LLM_result[j])

    print(f"关于regulation{j}的正确率：{acc} 精确率：{pre}   召回率：{recall}    F1-score:{f1}")



