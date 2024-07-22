import json
from http import HTTPStatus
import dashscope

def qwen_test():

    #规范
    regulation_text = ""
    with open('./source/regulationsInformat.json', 'r',encoding='utf-8') as f:
        regulation_text = f.read()
    
    #上下文提示
    messages = [

        {
            "role": "user",
            "content": [
                {
                    "text": "这些是安全规范 "+regulation_text+" 我需要你找出图片中所有被违反的安全条例,按照python 的list格式返回这些条例对应的序号"
                },
                {
                    "image": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG"
                }
        ]},

        {
            "role": "assistant", 
            "content": [
                {"text": "[1,39,36,30,10,71]"}
            ]
        },

        {
            "role": "user",
            "content": [
                {
                    "text": "继续按照相同的格式，找出图片中所有被违反的安全条例,按照python 的list格式返回这些条例对应的序号"
                },
                {"image": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150814_0011_Z.JPG"}
            ]
        }
    ]

    response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                    messages=messages,
                                                    api_key="sk-a1201b345d764687a3f8246944ea62fa",
                                                    max_tokens=1500)
    
    #content = response['output']['choices'][0]['message']['content'][0]['text']
    print(response)
    # '''
    # 检查输出是否符合要求：数组格式要求;长度要求
    # '''
    # # try:
    # #     content_list = eval(content)
    # # except Exception as e:
    # #     print(e)
    # #     return
    # # else:
    # #     if type(content_list)!=type([]) or len(content_list)!=3:
    # #         print("response format error")
    # #         return
    
    # # print(content_list)

    # #开始批量查询
    # query_num = 10

    # with open('./source/train.txt', 'r') as f:
    #     img_str = f.read()

    # img_json = json.loads(img_str)

    # #测试集结果
    # result_file = open('./Qwen_test/Qwenvl_result.txt', 'w')

    # for index in range(query_num):
    #     #获取图片url
    #     image_url = img_json['data_set'][index]['img_url']  #按顺序获取url  
    #     #上下文提示
    #     messages = [

    #         {
    #             "role": "user",
    #             "content": [
    #                 {
    #                     "text": "这些是安全规范 "+regulation_text+" 我需要你找出图片中所有被违反的安全条例,按照python 的list格式返回这些条例对应的序号"
    #                 },
    #                 {
    #                     "image": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG"
    #                 }
    #         ]},

    #         {
    #             "role": "assistant", 
    #             "content": [
    #                 {"text": "[1,39,36,30,10,71]"}
    #             ]
    #         },

    #         {
    #             "role": "user",
    #             "content": [
    #                 {"image": image_url}
    #             ]
    #         }
    #     ]
    #     response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
    #                                                 messages=messages,
    #                                                 api_key="sk-a1201b345d764687a3f8246944ea62fa") 
    #     print(response)   
    #     #content = response['output']['choices'][0]['message']['content'][0]['text']

    #     #对于格式进行检查
    #     #correct = True
    #     # try:
    #     #     content_list = eval(content)
    #     # except Exception as e:
    #     #     print(e,content)
    #     #     #选择继续还是终止
    #     #     correct = False
    #     #     pass
    #     #     #break
    #     # else:
    #     #     if type(content_list)!=type([]):
    #     #         print("response format error")
    #     #         #选择继续还是终止
    #     #         correct = False
    #     #         pass
    #     #         #break
    #     #     else:
    #     #         for num in content_list:
    #     #             if num != 1 and num!= 0:
    #     #                 correct = False
    #     #                 pass   
    #     # if correct:
    #     #     result_file.write(content+"\r")   
    #     # else:
    #     #     result_file.write("error"+"\r")  
    #     # print(index,content)
            

        

    # result_file.close()


if __name__ == '__main__':
    qwen_test()

