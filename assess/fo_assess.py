

#真实标注数据
violation_file = open('./source/violation_index.txt', 'r')    
violations = violation_file.readlines()
violation_file.close()

#大模型检测结果
foresult_file = open('./assistant_learn/fo_result.txt', 'r')    
fo_result = foresult_file.readlines()
foresult_file.close()

count = 500

#命中率：判定存在违规的图片个数/总数
violate_count = 0

#准确率：真实违规个数/违规判定个数
violate_true = 0
violate_judge = 0

for index in range(count):

    #遍历寻找真实命中
    
    #标注违规
    violates_mark = eval(violations[index])
    
    violates = eval(fo_result[index])

    for vio in violates:
        if vio in violates_mark:
            violate_true = violate_true + 1

    #当前图片判定违规个数
    violation_num = len(violates)
    violate_judge = violate_judge + violation_num

    #命中率
    if violation_num > 0:
        violate_count = violate_count + 1

print(violate_count/count,violate_true/violate_judge)


    








