from fastapi import FastAPI
import uvicorn
from src.routers import router
from fastapi.responses import RedirectResponse

app = FastAPI()

app.include_router(router)

@app.get("/")
def redirect():
    return RedirectResponse("http://127.0.0.1:8000/status")

@app.get("/status")
def status():
    return {"message": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port= 8000, reload= True)