from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Working!"}

@app.get("/users")
async def get_users():
    return {"users": {"user_1": "John", "user_2": "Jane", "user_3": "Doe"}}