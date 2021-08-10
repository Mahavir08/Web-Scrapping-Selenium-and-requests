import requests
import json


url = "https://wise.com/rates/history+live?source=USD&target=INR&length=30&resolution=hourly"
res = requests.get(url)
data = res.text # unicode
parsed = json.loads(data) # List
value = parsed[-1]
print("Today's USD To INR is : ")
print(value["value"])




    




    


    



