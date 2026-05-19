import requests
BASE_URL = "http://127.0.0.1:8000"

#test case 1
response= requests.get(BASE_URL + "/")
print("status code:", response.status_code)
print("response :", response.json)

# test case 2 : GET all students


response = requests.get(BASE_URL + "/students")
print("status code:", response.status_code)
print("response :", response.json)

# test 3  post...







#test case 4 put ....






#test case 5 delete ...
