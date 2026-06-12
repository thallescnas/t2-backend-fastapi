from fastapi import FastAPI
from routes.routes import router


app = FastAPI()

app.include_router(router)

@app.get("/health")
def health_cheack():
    return {"message": "API rodando!"}