from fastapi import FastAPI
app=FastAPI()
#@app.get("/")
# def home():
#     return {"Hii Seema"}
# @app.get("/products")
# def home():
#     return {"hii seema"}
# @app.get("/product") 
# def cus(id:int,name:str):
#     return {f"you entered id: {id}, name: {name}"}   

# @app.get("/products")
# def products(
#     category: str,
#     brand: str,
#     price: int
# ):
#     return {
#         "category": category,
#         "brand": brand,
#         "price": price
#     }    
#/products?category=mobile&brand=Samsung&price=50000
from pydantic import BaseModel
class loan(BaseModel):
    name:str
    age:int
    income:int
    loan_amount:int

@app.get("/")
def home():
    return {"In url type docs and fill data correctly to check loan "}

@app.post("/loan")
def loan_status(data: loan):
    if data.age>=21 and data.income>=(data.loan_amount*0.2):
        return {"name=":data.name,
        "age=":data.age,
        "loan approved successfully and here is the amount":data.loan_amount
        }
    else:
        return {"loan_status":"not approved"}