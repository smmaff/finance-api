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

@app.get("/transactions")
def transaction_see():
    return{"message": "Cписок всех транзакций: ", "data": transactions}

@app.get("/balance")
def balance_see():
    balance = 0
    for transaction in transactions:
        if transaction.type == "Доход":
            balance += transaction.amount
        else:
            balance -= transaction.amount
    return{"message": "Ваш баланс:", "data": balance}

class Scoring(BaseModel):
    amount: float
    term: int

@app.post("/scoring")
def scoring(data: Scoring):
    mouthly_payment = data.amount / data.term
    balance = 0
    for transaction in transactions:
            if transaction.type == "Доход":
                balance += transaction.amount
            else:
                balance -= transaction.amount
    remain_balance = balance - mouthly_payment
    if remain_balance >= mouthly_payment * 2:
        return{"message": "Кредит одобрен!"}
    else:
        return{"message": "В кредите отказано!"}