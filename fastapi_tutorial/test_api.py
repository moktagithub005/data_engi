import requests

BASE_URL = "http://127.0.0.1:8000"

print("\n--- Test 1: GET / ---")
res = requests.get(BASE_URL + "/")
print("Status:", res.status_code)
print("Response:", res.json())

print("\n--- Test 2: GET /students ---")
res = requests.get(BASE_URL + "/students")
print("Status:", res.status_code)
print("Response:", res.json())

print("\n--- Test 3: POST /students (add new student) ---")
new_student = {"id": 4, "name": "rohan", "city": "manali"}
res = requests.post(BASE_URL + "/students", json=new_student)
print("Status:", res.status_code)
print("Response:", res.json())

print("\n--- Test 4: PUT /students/4 (update student id=4) ---")
updated_student = {"id": 4, "name": "rohan updated", "city": "shimla"}
res = requests.put(BASE_URL + "/students/4", json=updated_student)
print("Status:", res.status_code)
print("Response:", res.json())

print("\n--- Test 5: DELETE /students/4 (delete student id=4) ---")
res = requests.delete(BASE_URL + "/students/4")
print("Status:", res.status_code)
print("Response:", res.json())