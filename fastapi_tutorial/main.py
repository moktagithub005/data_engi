from fastapi import FastAPI
#create the fastapi app
app=FastAPI()

#route 1: home endpoint

@app.get("/")
def home():
    return{"mesage":"welcome to my  forst api"}


@app.get("/students")
def get_students():
    students =[
      {"id":1, "name": "nikita", "city":"sundernagar"},
      {"id":2, "name": "saurabh", "city":"solan"},
      {"id":3, "name": "palak", "city":"Hamirpur"},
    ]

    return {"total": len(students), "students":students}

#route:  client sends data to us : POST
@app.post("/students")
def create_students():
    return {"message": "A new student was created"}

# route PUT: client want to update something 
@app.put("/students")
def update_students():
    return{"message": "A student was updated "}

# route DELETE - client wants to  delete data
@app.delete("/students")
def delete_students():
    return{"message": "a student was deleted"}
