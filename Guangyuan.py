import json
import requests

class Building:
    
    def __init__(self,ip = "119.3.184.126",port = 4337,headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE4NjE0MzYzLCJleHAiOjE3MjEyMDYzNjN9.deBfJfbIQe2g5RYLVU742vAZJ43003uAxXtVIKPAnlo'}):
        
        self.ip = ip
        self.port = port
        
        self.headers = headers
        
    def get_photo_url(self,id):
        # url = "http://119.3.184.126:4337/content-manager/collection-types/api::photo.photo/682"
        url = "http://"+self.ip+":"+str(self.port)+"/content-manager/collection-types/api::photo.photo/"+str(id)
        #print(url)
        response = requests.get(url,headers=self.headers)
        data = json.loads(response.content)
        
        return data['image']['url']
        
    
        
        
        