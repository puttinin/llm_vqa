import urllib.request
import base64 

res = urllib.request.urlopen("https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/cms/2024/06/18/DJI_20240618150735_0007_Z.JPG")
imgdata = res.read()
# 将图片数据转换为 base64 编码
base64_image = base64.b64encode(imgdata).decode('utf-8')

