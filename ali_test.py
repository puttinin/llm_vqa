# -*- coding: utf-8 -*-
# ����������
# pip install alibabacloud_imagerecog20190930

import os
import io
from urllib.request import urlopen
from alibabacloud_imagerecog20190930.client import Client
from alibabacloud_imagerecog20190930.models import RecognizeSceneAdvanceRequest
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util.models import RuntimeOptions

import requests
import json
from Guangyuan import Building

from viapi.fileutils import FileUtils

config = Config(
  # ����AccessKey ID��AccessKey Secret����ο�https://help.aliyun.com/document_detail/175144.html��
  # ������õ���RAM�û���AccessKey������ҪΪRAM�û�����Ȩ��AliyunVIAPIFullAccess����ο�https://help.aliyun.com/document_detail/145025.html��
  # �ӻ���������ȡ���õ�AccessKey ID��AccessKey Secret�����д���ʾ��ǰ���������û���������
  access_key_id=os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
  access_key_secret=os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
  # ���ʵ�����
  endpoint='imagerecog.cn-shanghai.aliyuncs.com',
  # ���ʵ�������Ӧ��region
  region_id='cn-shanghai'
)
#����һ���ļ��ڱ���
#img = open(r'/tmp/RecognizeScene1.jpg', 'rb')
#��������ʹ������ɷ��ʵ�url
tower = Building(ip = "119.3.184.126",port = 4337,headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE4NjE0MzYzLCJleHAiOjE3MjEyMDYzNjN9.deBfJfbIQe2g5RYLVU742vAZJ43003uAxXtVIKPAnlo'})
url = 'https://viapi-test-bj.oss-cn-beijing.aliyuncs.com/viapi-3.0domepic/imagerecog/RecognizeScene/RecognizeScene1.jpg'
# url = tower.get_photo_url(682)
img = io.BytesIO(urlopen(url).read())
recognize_scene_request = RecognizeSceneAdvanceRequest()
recognize_scene_request.image_urlobject = img
runtime = RuntimeOptions()
try:
  # ��ʼ��Client
  client = Client(config)
  response = client.recognize_scene_advance(recognize_scene_request, runtime)
  # ��ȡ������
  print(response.body)
except Exception as error:
  # ��ȡ���屨����Ϣ
  print(error)
  # ��ȡ�����ֶ�
  print(error.code)