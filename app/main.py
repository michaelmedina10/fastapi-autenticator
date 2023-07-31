from fastapi import FastAPI
from routes import user_router, test_router
import uvicorn

app = FastAPI()

@app.get('/')
def health_check():
    return "OK, it's working!!"

app.include_router(user_router)
app.include_router(test_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)