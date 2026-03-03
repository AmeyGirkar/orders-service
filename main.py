from fastapi import FastAPI
import uvicorn

import os

app = FastAPI(title="Orders Service")

# Placeholder for PostgreSQL connection
DB_URL = os.getenv("DB_URL", "postgresql://localhost:5432/orders")

@app.get("/")
def read_root():
    return {"service": "Orders Service", "status": "running", "database": "PostgreSQL"}

@app.get("/orders")
def get_orders():
    return [{"id": 1, "item": "Laptop", "quantity": 1}, {"id": 2, "item": "Mouse", "quantity": 2}]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
