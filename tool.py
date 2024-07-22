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
    ʹ�� OpenAI ��ģ����������ظ���

    ����:
    prompt: �û������룬���������ʾ��
    model: ʹ�õ�ģ�ͣ�Ĭ��Ϊ"gpt-3.5-turbo"��
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"] # ģ�����ɵĻظ�


