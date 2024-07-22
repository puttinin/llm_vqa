import json
import urllib.request
import base64 
from openai import OpenAI

#客户端
client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

with open('./source/regulationsInformat.json', 'r',encoding='utf-8') as f:
        img_str = f.read()

img_json = json.loads(img_str)

#上下文样例图片
res = urllib.request.urlopen("https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG")
imgdata = res.read()
#base64
example_image = base64.b64encode(imgdata).decode('utf-8')

#开始批量查询
query_num = 50
for index in range(query_num):
      
    #获取图片
    image_url = img_json['data_set'][index]['img_url']  #按顺序获取url
    query_response = urllib.request.urlopen(image_url)
    query_response_image_data = query_response.read()
    #base64
    query_image = base64.b64encode(query_response_image_data).decode('utf-8')

    for key,value in img_json.items():
        #上下文提示
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                    {"role": "system", "content": "你是一个能干的助手."},
                    {"role": "user",
                    "content": [
                        {"type": "text", "text": f"这是安全规范 {value},你判断图片中是否存在违反这项规范的行为，有的话你返回True，否的话返回False"},
                        {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{query_image}"} }
                    ]},
                    # {"role": "assistant", "content": "[0, 1, 0]"},
                    # {"role": "user",
                    # "content": [
                    #     {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{test_image}"} }
                    # ]},
            ],
            max_tokens=1500,
        )

        content = response.choices[0].message.content

        print(content)

        break





