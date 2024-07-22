from http import HTTPStatus
import dashscope


messages = [
    {
        "role": "user",
        "content": [
            {"text": "你帮我进行工人安全检查，你需要检查的安全条例就三条：1.施工现场未穿带反光背心。2.人员未佩戴安全帽。3.高出作业、攀登或转移作业时失去保护。\
待会我每给你一张图片，你就对上述三条进行判断，并以python数组的形式返回你认为有没有违规，比如一张图中违反了第一条，没有违反第二条和第三条，你就返回【1,0,0】，现在我要准备给你传图片了"}
        ]
    }
]

# messages = [
#         {
#             "role": "user",
#             "content": [
#                 {"image": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG"}
#             ]
#         }
#     ]

response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                    messages=messages,
                                                    api_key="sk-a1201b345d764687a3f8246944ea62fa")
# The response status_code is HTTPStatus.OK indicate success,
# otherwise indicate request is failed, you can get error code
# and message from code and message.
if response.status_code == HTTPStatus.OK:
    print(response)
else:
    print(response.code)  # The error code.
    print(response.message)  # The error message.


#    export DASHSCOPE_API_KEY=sk-a1201b345d764687a3f8246944ea62fa

