import json
import urllib.request
import base64 
from openai import OpenAI



def fo_test():
    client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

    #上下文样例图片
    res = urllib.request.urlopen("https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG")
    imgdata = res.read()
    #base64
    example_image = base64.b64encode(imgdata).decode('utf-8')


    #测试样例
    res1 = urllib.request.urlopen("https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/17/DJI_20240617110623_0019_Z.JPG")
    imgdata1 = res1.read()
    #base64
    test_image = base64.b64encode(imgdata1).decode('utf-8')

    #上下文提示
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
                {"role": "system", "content": "你是一个能干的助手."},
                {"role": "user",
                "content": [
                    {"type": "text", "text": "你帮我进行工人安全检查，你需要检查的安全条例就三条：1.施工现场未穿戴反光背心。2.人员未佩戴安全帽。3.高处作业、攀登或转移作业时失去保护。\
                    待会我每给你一张图片，你就对上述三条进行判断，并以python数组的形式返回你认为有没有违规，比如一张图中违反了第一条，没有违反第二条和第三条，你就返回【1,0,0】，除此之外不要返回其他的任何东西。等你确认了我就要准备给你传图片了"},
                    {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{example_image}"} }
                ]},
                {"role": "assistant", "content": "[0, 1, 0]"},
                {"role": "user",
                "content": [
                    {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{test_image}"} }
                ]},
        ],
        max_tokens=1500,
    )

    content = response.choices[0].message.content
    
    '''
    检查输出是否符合要求：数组格式要求;长度要求
    '''
    try:
        content_list = eval(content)
    except Exception as e:
        print(e)
        return
    else:
        if type(content_list)!=type([]) or len(content_list)!=3:
            print("response format error")
            return
    
    print(content_list)

    #开始批量查询
    query_num = 50

    with open('./source/train.txt', 'r') as f:
        img_str = f.read()

    img_json = json.loads(img_str)

    #测试集结果
    result_file = open('./FO_test/chatgpt4o_result.txt', 'w')

    for index in range(query_num):

        #获取图片
        image_url = img_json['data_set'][index]['img_url']  #按顺序获取url
        query_response = urllib.request.urlopen(image_url)
        query_response_image_data = query_response.read()
        #base64
        query_response_image = base64.b64encode(query_response_image_data).decode('utf-8')

        #使用上下文查询，获取结果并写入
        #上下文提示
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                    {"role": "system", "content": "你是一个能干的助手."},
                    {"role": "user",
                    "content": [
                        {"type": "text", "text": "你帮我进行工人安全检查，你需要检查的安全条例就三条：1.施工现场未穿戴反光背心。2.人员未佩戴安全帽。3.高处作业、攀登或转移作业时失去保护。\
                        待会我每给你一张图片，你就对上述三条进行判断，并以python数组的形式返回你认为有没有违规，比如一张图中违反了第一条，没有违反第二条和第三条，你就返回【1,0,0】，除此之外不要返回其他的任何东西。等你确认了我就要准备给你传图片了"},
                        {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{example_image}"} }
                    ]},
                    {"role": "assistant", "content": "[0, 1, 0]"},
                    {"role": "user",
                    "content": [
                        {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{query_response_image}"} }
                    ]},
            ],
            max_tokens=1500,
        )

        content = response.choices[0].message.content
        
        #对于格式进行检查
        correct = True
        try:
            content_list = eval(content)
        except Exception as e:
            print(e,content)
            #选择继续还是终止
            correct = False
            pass
            #break
        else:
            if type(content_list)!=type([]):
                print("response format error")
                #选择继续还是终止
                correct = False
                pass
                #break
            else:
                for num in content_list:
                    if num != 1 and num!= 0:
                        correct = False
                        pass   
        if correct:
            result_file.write(content+"\r")   
        else:
            result_file.write("error"+"\r")  
        print(index,content)

    result_file.close()

        
    

if __name__ == '__main__':
    fo_test()
