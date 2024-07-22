from openai import OpenAI
import time
import json

 # 创建openai客户端
client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

#安全检查的4o
assistant_id = "asst_C9AxTkml9tkSEWYaqDsSBZVq"

#创建一个线程
thread = client.beta.threads.create()
print("thread.id: "+str(thread.id))
thread_id = thread.id

# 引导
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content = [
                {"type": "text", "text": "使用你的知识库，知识库中json的键值对中value为安全规范，key为规范对应的索引，我将上传给你施工现场的图片，你要对比每条规范，如果图片中违反了对应规范，你就在结果的的数组中添加对应的索引\
                                            比如一张图片中违反了索引为2、5、12的规范，你就返回[2,5,12],，除此之外不要返回其他的任何东西。等你确认了我就要继续给你传图片"}
               ]
)

# 假装回复
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role = "assistant",
    content="好的,我已经了解，你开始传图片吧",
)

# # 引导
# message = client.beta.threads.messages.create(
#     thread_id=thread_id,
#     role="user",
#     content =   [
#                     {"type": "image_url", "image_url": { "url": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/dji_20240618150735_0007_z.jpg"} }
#                 ]
# )

# # 假装回复
# message = client.beta.threads.messages.create(
#     thread_id=thread_id,
#     role = "assistant",
#     content="[5,20,104]",
# )


#大模型结果
result_file = open('./assistant_learn/fo_result.txt', 'w')

with open('./source/train.txt', 'r') as f:
    img_str = f.read()

img_json = json.loads(img_str)

count = 10
for index in range(count):

    #获取图片
    image_url = img_json['data_set'][index]['img_url'].lower()  #按顺序获取url

    print(image_url)

    #开始上传图片
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content = [
                    {"type": "image_url", "image_url": { "url": image_url} }
                ]
    )

    # 运行assistant
    run = client.beta.threads.runs.create(
        assistant_id=assistant_id,
        thread_id=thread_id,
        instructions="你是一个有用的助手，与知识库中安全条例逐一判断后只返回list形式的结果"
    )

    #fail计数
    err_count = 0

    while True:

        run = client.beta.threads.runs.retrieve( # 通过thread.id和run.id来查看run的状态
            thread_id=thread_id,
            run_id=run.id
        )
        print(f"{index} run status: "+run.status)

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
            content_str = message.content[0].model_dump_json()
            content_json = json.loads(content_str)
            value = content_json['text']['value']
            print(content_json)
            result_file.write(value+"\r")  
            break

        elif(run.status=='failed'):

            err_count = err_count + 1

            #是否重新创建运行    
            if err_count <= 8:
                print(f"第{err_count}次重试")
                #开始上传图片
                message = client.beta.threads.messages.create(
                    thread_id=thread_id,
                    role="user",
                    content = [
                                {"type": "image_url", "image_url": { "url": image_url} }
                            ]
                )
                # 运行assistant
                run = client.beta.threads.runs.create(
                    assistant_id=assistant_id,
                    thread_id=thread_id,
                    instructions="你是一个有用的助手，与知识库中安全条例逐一判断后只返回list形式的结果"
                )
                time.sleep(1)
            else:
                #清零
                err_count = 0
                
                #跳过
                result_file.write(str([])+"\r")  
                break

        time.sleep(1)

result_file.close()




