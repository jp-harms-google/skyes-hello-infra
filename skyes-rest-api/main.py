from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello_world():
    return {"success": True, "message": "Hello Skyes Scheduler"}


@app.get('/schedule')
async def get_schedule(input_data: str):
    return {"success": True, "schedule": ["6:00AM", "Get Starbucks"]}