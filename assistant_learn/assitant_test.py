from openai import OpenAI
import time
import json

 # 创建openai客户端
client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

#安全检查的4o
assistant_id = "asst_C9AxTkml9tkSEWYaqDsSBZVq"

thread_id = "thread_d3FBP2teBYhcLFJIRmYgQ6Lr"

vector_store_ids=['vs_styozoeUobKZkCbNnE12dey3']


# #创建矢量存储
# vector_store = client.beta.vector_stores.create(name="safety regulations")
 
# # 准备上传文件
# file_paths = ["./source/regulationsInformat.json"]
# file_streams = [open(path, "rb") for path in file_paths]
 
# # 使用上传和轮询sdk上传文件，添加到vector base
# # 并且轮询知道上传完成
# file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
#   vector_store_id=vector_store.id, files=file_streams
# )
 
# #打印上传结果.
# print(file_batch.status)
# print(file_batch.file_counts)

# #更新助手
# assistant = client.beta.assistants.update(
#   assistant_id=assistant_id,
#   tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
# )

# print(assistant)
# print("update complete")

# #创建assistant对象, 定义创建assistant的身份为安全检察员
# assistant = client.beta.assistants.create(
#   name="Safety Assistant",
#   instructions="你是一个能干的助手 使用你的知识库来发现图片中存在的安全违规问题",
#   model="gpt-4o",
#   tools=[{"type": "file_search"}],
# )

# print("assistant.id:"+str(assistant.id))

# #上传图片文件
# image_file = client.files.create(
#   file=open("violate.jpg", "rb"), purpose="assistants"
# )
# print(image_file)

# #违规图片id
# imageFile_id ='file-FxidMdlwFAApBkIp4w0ZcQNY'

#创建一个线程
thread = client.beta.threads.create()
print("thread.id: "+str(thread.id))
thread_id = thread.id

# 
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content = [
                {"type": "text", "text": "你是个非常有用的助手，你要使用你的知识库，告诉我知识库中安全规范总共有几条，分别是什么"}
               ]
)

# 
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content = [
                {"type": "text", "text": "你是个非常有用的助手，你要使用你的知识库，帮我看看这张图中违反了哪些安全规范并以python的list作为结果返回"},

                {"type": "image_url", "image_url": { "url": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/dji_20240618150735_0007_z.jpg"} }
               ]
)



# 运行assistant
run = client.beta.threads.runs.create(
    assistant_id=assistant_id,
    thread_id=thread_id,
    instructions="使用知识库"
)


while True:

    run = client.beta.threads.runs.retrieve( # 通过thread.id和run.id来查看run的状态
        thread_id=thread_id,
        run_id=run.id
    )
    print(run.status)

    if(run.status=='completed'):
        print("success!")
        #查看对话消息
        messages = client.beta.threads.messages.list( # 查看thread.id中的message
            thread_id=thread_id
        )
        message_id = messages.data[0].id
        message = client.beta.threads.messages.retrieve(
            thread_id=thread_id,
            message_id=message_id
        )

        print(message)  #usage=Usage(completion_tokens=295, prompt_tokens=11967, total_tokens=12262) prompt_tokens*5/1M + completion_tokens*15/1M
        break

    elif(run.status=='failed'):
        break

    time.sleep(1)


    





