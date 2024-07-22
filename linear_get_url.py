import json
import requests

# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NiwiaWF0IjoxNzE4NzgyMTc5LCJleHAiOjE3MjEzNzQxNzl9.hOXIyc0tve5RJA5jPxupVYBuhGTc0RfyZitY2RfrY2E'}
# url = "http://"+"119.3.184.126"+":"+str(4338)+"/service/api/annotations?pagination%5Bpage%5"
# response = requests.get(url,headers=headers)
# data = json.loads(response.content)
# print(data['data'][0]['id'],"\r\n\r\n",data['meta'],"\r\n",data['data'][0])


headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE4NzkxNzY0LCJleHAiOjE3MjEzODM3NjR9.DLRvY9Khirbx10obYW8PrUqStNfBkL1wsj97lLzKKw0'}
url = "http://"+"119.3.184.126"+":"+str(4337)+"/content-manager/collection-types/api::photo.photo?page=1"
response = requests.get(url,headers=headers)
data = json.loads(response.content)
print(data)

