from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"Enter customer id to get customer details"}
@app.get("/customer")
def get_customer(customer_id:int):
    return {"customer_id":customer_id,
    "name":"seema"}