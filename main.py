from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "This Server is running!"


#path parameters
@app.get("/greet/{name}")
def greet (name):
    return {"message: " f"Hallo {name}"}

users = [
    "joan","pep","jordi","hector"
]

#query parameters
# @app.get("/search")
# def search_user(name):
#     if name in users:
#         return {"message": f"Hi {name}"}
#     else:
#         return {"message": "user not found"}

# two query parameters
@app.get("/search")
def search_user(name,message):
    if name in users:
        return {"message": f"Hi {name}, {message}"}
    else:
        return {"message": "user not found"}

#request body
# dicts, lists, objects en general
users2 = [
    {"name":"joan","email":"joan@gmail.cat"},
    {"name":"hector","email":"hector@gmail.cat"},
]

#pydantic



@app.post("/create_user")
def create_user(user:dict):
    print(user)
    new_user = {
        "name": user["name"],
        "email" : user["email"]
    }
    users2.append(new_user)
    return {"message" : "user created successfully"}

