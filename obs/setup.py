# 引入模块
from obs import CreateBucketHeader
from obs import ObsClient
import traceback
import json

# 推荐通过环境变量获取AKSK，这里也可以使用其他外部引入方式传入，如果使用硬编码可能会存在泄露风险。
# 您可以登录访问管理控制台获取访问密钥AK/SK，获取方式请参见https://support.huaweicloud.com/usermanual-ca/ca_01_0003.html。
ak = "FJ8LRJDHCFZURCLDSBGA"
sk = "UC2a5nEtFn5JHIN1kHHz2XqmTbLJPZcmQTpaCR7w"

# # 【可选】如果使用临时AKSK和SecurityToken访问OBS，则同样推荐通过环境变量获取
# security_token = os.getenv("SecurityToken")

#server endpoint
server = "obs.cn-north-4.myhuaweicloud.com"

# 创建obsClient实例
obsClient = ObsClient(access_key_id=ak, secret_access_key=sk, server=server)

#先复制几张
count = 10

#添加训练集
with open('./source/train.txt', 'r') as f:
    img_str = f.read()

img_json = json.loads(img_str)

path_header = "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/"

for index in range(count):

    #原文件索引
    img_json['data_set'][index]['img_url'][len(path_header):]

    #复制对象
    try:

        #
        objectKey = "text_test_folder/test_text"

        # 设置带上传的文本内容
        content = 'Hello OBS'

        #源bucket
        sourceBucketName_t = "construction-management-system"

        #源文件路径
        sourcePath = "cms/2024/06/01/"

        #源文件名
        sourceFile = "DJI_20240601140003_0001_W.JPG"

        #源文件索引
        sourceObjectKey_t = sourcePath + sourceFile

        print(sourceObjectKey_t)

        #目标bucket
        destBucketName_t = "construction-management-system"

        #目标文件路径
        dstPath = "cms/2024/06/01/"+"lower/"

        #目标文件名
        dstFile = sourceFile.lower()

        #目标文件索引
        destObjectKey_t = dstPath + dstFile

        resp = obsClient.copyObject(sourceBucketName=sourceBucketName_t, sourceObjectKey=sourceObjectKey_t, destBucketName=destBucketName_t, destObjectKey=destObjectKey_t, metadata=None, headers=None, versionId=None)

        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            print('Put Content Succeeded')
            print('requestId:', resp.requestId)
            print('etag:', resp.body.etag)
        else:
            print('Put Content Failed')
            print('requestId:', resp.requestId)
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
    except:
        print('Put Content Failed')
        print(traceback.format_exc())



# 关闭obsClient
obsClient.close()
