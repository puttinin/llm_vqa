# coding=gb2312
import os
import openai
from dotenv import load_dotenv, find_dotenv

def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = get_openai_key()
    """
    使用 OpenAI 的模型生成聊天回复。

    参数:
    prompt: 用户的输入，即聊天的提示。
    model: 使用的模型，默认为"gpt-3.5-turbo"。
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"] # 模型生成的回复


