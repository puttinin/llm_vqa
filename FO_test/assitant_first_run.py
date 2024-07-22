from openai import OpenAI
import urllib.request
import base64 
import time

client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

#助手id
assistant_id = "asst_oHt3P00a52Y7WwuyN0pWGxhw"
 
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

#创建初次对话Thread
thread = client.beta.threads.create(
  messages=[
                {"role": "user",
                "content": [
                    {"type": "text", "text": "使用你的知识库，知识库中json的键值对value为安全规范，key为规范对应的索引，我将上传给你施工现场的图片，你要对比每条规范，如果图片中存在违规行为，你就在最后结果的的数组中添加这条行为对应的索引\
                                            比如这张图片中违反了索引为2、5、8的规范，你就返回[2,5,8],，除此之外不要返回其他的任何东西。等你确认了我就要继续给你传图片"},
                    {"type": "image_url", "image_url": { "url": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.jpg"} }
                ]},
                {"role": "assistant", "content": "[2, 5, 8]"},
                {"role": "user",
                    "content": [{"type": "image_url", "image_url": { "url": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/17/DJI_20240617110623_0019_Z.JPG"} }
                ]},
  ]
)

print("thread id:",thread.id)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant_id,
  model="gpt-4o",
  instructions="New instructions that override the Assistant instructions",
  tools=[{"type": "file_search"}]
)

print("run id:",run.id)

# # 获取run的最新状态。 
# run = client.beta.threads.runs.retrieve(
#   thread_id=thread.id,
#   run_id=run.id
# )

# while True:
#     if run.status == 'completed':
#         messages = client.beta.threads.messages.list(
#         thread_id=thread.id
#         )
#         print(messages)
#         break
#     else:
#         time.sleep(1)
#         print("wait assistant 1 second......")


#thread id: thread_y1SupvqmAiXsyAw7w6JzSsuF
# run id: run_6ifSvngkT7eC5zUO6CTfC1vC