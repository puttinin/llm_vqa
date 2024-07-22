from obs import ObsClient
from obs import ACL
from obs import Owner
from obs import Grant, HeadPermission
from obs import Grantee
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

#添加训练集
with open('./source/train.txt', 'r') as f:
    img_str = f.read()

img_json = json.loads(img_str)

#网址头
path_header = "https://construction-management-system.obs.cn-north-4.myhuaweicloud.com/"

#路径模板
filePath_t = "cms/2024/06/20/"

#源bucket
sourceBucketName = "construction-management-system"

#目标bucket
destBucketName = "construction-management-system"

#复制图片个数
count = 100
for index in range(count):

    #源文件索引
    sourceObjectKey = img_json['data_set'][index]['img_url'][len(path_header):]

    #源文件名
    sourceFile = sourceObjectKey[len(filePath_t):]

    #源文件路径
    sourceFile_path = sourceObjectKey[:len(filePath_t)]

    #复制对象
    try:
        #目标文件名
        dstFile = sourceFile.lower()

        #目标文件存储路径       等同于相同路径下改个小写名字
        dstPath = sourceFile_path

        #目标文件索引
        destObjectKey = dstPath + dstFile

        # print(dstPath,destObjectKey_t)

        #复制文件
        resp = obsClient.copyObject(sourceBucketName=sourceBucketName, sourceObjectKey=sourceObjectKey, destBucketName=destBucketName, destObjectKey=destObjectKey, metadata=None, headers=None, versionId=None)
        
        # 设置文件权限
        resp = obsClient.setObjectAcl(sourceBucketName, destObjectKey,aclControl=HeadPermission.PUBLIC_READ)

        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            print('Put Content Succeeded')
            print(resp)
            print(destObjectKey)
            # print('requestId:', resp.requestId)
            # print('etag:', resp.body.etag)
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
