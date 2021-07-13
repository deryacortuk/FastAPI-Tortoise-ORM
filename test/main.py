from fastapi import FastAPI,Form

app =FastAPI()

@app.post("/test/")
async def testFast(name:str= Form(...),type:str=Form(...)):
    return {"python":name,"fastapi":type}
    