from zhipuai import ZhipuAI

#客户端
client = ZhipuAI(api_key="4e1dd11c6ec19175ef73507f4624508a.EUFE2Fp23vRYCMgC") # 填写您自己的APIKey



def glm_test():

    #上下文提示
    messages=[
        {
            "role": "system", "content": "你擅长从文本中提取关键信息，精确、数据驱动，重点突出关键信息，根据用户提供的文本片段提取关键数据和事实，将提取的信息以清晰的list格式呈现。"
        },
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "你帮我进行工人安全检查，你需要检查的安全条例就三条：1.施工现场未穿戴反光背心。2.人员未佩戴安全帽。3.高处作业、攀登或转移作业时失去保护。\
                        待会我每给你一张图片，你就对上述三条进行判断，并以python的list数组的形式返回你认为有没有违规，比如一张图中违反了第一条，没有违反第二条和第三条，你就返回'''[1,0,0]'''，除此之外不要返回其他的任何文字。我给你传图片了"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url" : "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG"
                }
            }
            ]
        },
        #pretend reply
        {
            "role": "assistant",
            "content": [
            {
                "type": "text",
                "text": "[0,1,0]"
            }
            ]
        },
        #test
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "按照与上面回答相同的格式继续判断接下来的图片"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url" : "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/17/DJI_20240617110623_0019_Z.JPG"
                    }
                }
            ]
        },
    ]


    #调用
    response = client.chat.completions.create(
        model="glm-4v",  # 填写需要调用的模型名称
        messages=messages,
        temperature=0.9,
    )

    print(response.choices[0].message)

if __name__ == '__main__':
    glm_test()

