from openai import OpenAI
import time

client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

#助手id
assistant_id = "asst_oHt3P00a52Y7WwuyN0pWGxhw"

#run id
run_id = "run_6ifSvngkT7eC5zUO6CTfC1vC"

#thread id
thread_id = "thread_y1SupvqmAiXsyAw7w6JzSsuF"

# 添加新消息
message = client.beta.threads.messages.create(
  thread_id=thread_id,
  role="user",
  content=  [{"type": "image_url", "image_url": { "url": "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/17/DJI_20240617110623_0019_Z.jpg"} }]
)
# 创建run
run = client.beta.threads.runs.create(
  thread_id=thread_id,
  assistant_id=assistant_id
)


while True:
    # 获取run的执行结果。 
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
        thread_id=thread_id
        )
        print(messages)
        break
    else:
        print(run.status)
        time.sleep(1)
        messages = list(client.beta.threads.messages.list(thread_id=thread_id, run_id=run.id))
        print("message:"+str(message))

