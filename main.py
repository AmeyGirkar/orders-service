from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Orders Service")

@app.get("/")
def read_root():
    return {"service": "Orders Service", "status": "running"}

@app.get("/orders")
def get_orders():
    return [{"id": 1, "item": "Laptop", "quantity": 1}, {"id": 2, "item": "Mouse", "quantity": 2}]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
