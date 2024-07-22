import requests
import json
from Guangyuan import Building


# headers = {
#             'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE4NjE0MzYzLCJleHAiOjE3MjEyMDYzNjN9.deBfJfbIQe2g5RYLVU742vAZJ43003uAxXtVIKPAnlo',
#         }
# url = "http://119.3.184.126:4337/content-manager/collection-types/api::photo.photo?page=1&pageSize=10&sort=source:ASC"
# url = "http://119.3.184.126:4337/content-manager/collection-types/api::photo.photo/682"
# response = requests.get(url,headers=headers)
# data = json.loads(response.content)
# print(data['results'][0].keys(),data['results'][0]['image']['url'])
# print(data['image']['url'])

tower = Building(ip = "119.3.184.126",port = 4337,headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE4NjE0MzYzLCJleHAiOjE3MjEyMDYzNjN9.deBfJfbIQe2g5RYLVU742vAZJ43003uAxXtVIKPAnlo'})
        
print(tower.get_photo_url(682))    
