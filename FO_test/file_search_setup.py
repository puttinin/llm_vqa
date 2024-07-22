from openai import OpenAI
 
client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')
 
assistant = client.beta.assistants.create(
  name="Safety Assistant",
  instructions="你是一个能干的助手 使用你的知识库来发现图片中存在的安全违规问题",
  model="gpt-4o",
  tools=[{"type": "file_search"}],
)

# 创建向量存储  "Financial Statements"
vector_store = client.beta.vector_stores.create(name="safety regulations")
 
# 准备上传文件
file_paths = ["./source/regulationsInformat.json"]
file_streams = [open(path, "rb") for path in file_paths]
 
# 使用上传和轮询sdk上传文件，添加到vector base
# 并且轮询知道上传完成
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)
 
#打印上传结果.
print(file_batch.status)
print(file_batch.file_counts)

#更新助手
assistant = client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

print(assistant)
print("update complete")