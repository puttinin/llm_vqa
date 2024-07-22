from openai import OpenAI

#解决数学问题的4o
assistant_id="asst_QeJf40PwuZ6nRrPXc8dBQl0y"

thread_id="thread_rajzqnddhRWmDCd2OR1iyJMS"

# 创建openai客户端
client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd') 

# 创建assistant对象, 定义创建assistant的身份为一个数学导师，可以写代码并运行代码来解决数学问题
# assistant = client.beta.assistants.create(
#     name='Math Tutor',
#     instructions="You are a personal math tutor. Write and run code to answer math questions.",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4o",
# )

# print("assistant.id:"+str(assistant.id))

# # 创建一个线程
# thread = client.beta.threads.create()
# print("thread.id"+str(thread.id))

# 创建一条消息
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?" # 提出一个数学问题
)


# # 运行assistant
# run = client.beta.threads.runs.create(
#     assistant_id=assistant_id,
#     thread_id=thread_id,
#     instructions="Please address the user as Jane Doe. The user has a premium account."
# )
# print(run)

# # run = client.beta.threads.runs.retrieve( # 通过thread.id和run.id来查看run的状态
# #   thread_id=thread_id,
# #   run_id=run.id
# # )

#查看对话消息
messages = client.beta.threads.messages.list( # 查看thread.id中的message
  thread_id=thread_id
)
print(messages)

