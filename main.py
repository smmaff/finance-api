from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    type: str
    amount: float
    description: str

transactions = []

@app.get("/")
def read_root():
    return {"message": "Финансовый трекер работает!"}

@app.post("/transaction")
def add_trancaction(transaction: Transaction):
    transactions.append(transaction)
    return{"message": "Транзакция успешно добавлена!", "data": transaction}