from fastapi import FastAPI
my_awesome_api= FastAPI()
app= FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
    #s