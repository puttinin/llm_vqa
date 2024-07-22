from openai import OpenAI
import time
import json

 # 创建openai客户端
client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

#安全检查的4o
assistant_id = "asst_C9AxTkml9tkSEWYaqDsSBZVq"

#规范
regulation_text = ""
with open('./source/regulationsInformat.json', 'r',encoding='utf-8') as f:
    regulation_text = f.read()

#创建一个线程
thread = client.beta.threads.create()
print("thread.id: "+str(thread.id))
thread_id = thread.id

# 引导
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content = [
                {"type": "text", "text": "这些是安全规范    "+regulation_text+" 我需要你找出图片中所有被违反的安全条例,按照python 的list格式返回这些条例对应的序号"},
                {"type": "image_url", "image_url": { "url": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/dji_20240618150735_0007_z.jpg"} }
               ]
)

# 假装回复
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role = "assistant",
    content="[1,39,36,30,10,71]",
)

#大模型结果
result_file = open('./assistant_learn/promptjson_result.txt', 'w')

#样本
with open('./source/train.txt', 'r') as f:
    img_str = f.read()

img_json = json.loads(img_str)

for index in range(50):

    #获取图片
    image_url = img_json['data_set'][index]['img_url'].lower()  #按顺序获取url

    #
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content = [
                    {"type": "text", "text": "继续按照上面相同数组格式返回数据"},
                    {"type": "image_url", "image_url": { "url": image_url} }
                ]
    )

    # 运行assistant
    run = client.beta.threads.runs.create(
        assistant_id=assistant_id,
        thread_id=thread_id,
        instructions="你是一个有用的助手"
    )

    #fail计数
    err_count = 0

    while True:

        run = client.beta.threads.runs.retrieve( # 通过thread.id和run.id来查看run的状态
            thread_id=thread_id,
            run_id=run.id
        )
        print(f"{index} "+run.status)

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
            print(message)  #usage=Usage(completion_tokens=295, prompt_tokens=11967, total_tokens=12262) prompt_tokens*5/1M + completion_tokens*15/1M
            print(run)
            break

        elif(run.status=='failed'):

            err_count = err_count + 1

            #是否重新创建运行    
            if err_count <= 8:
                print(f"retry time: {err_count}")
                time.sleep(1)
                #重新运行assistant
                run = client.beta.threads.runs.create(
                    assistant_id=assistant_id,
                    thread_id=thread_id,
                    #instructions="你是一个有用的助手,返回的结果形式为python语言的列表"
                )
            else:
                #清零
                err_count = 0
                
                #跳过
                result_file.write(str([])+"\r")  
                break
            continue

        time.sleep(0.1)


result_file.close()
#1.completion_tokens=11, prompt_tokens=11187