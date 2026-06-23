from fastapi import FastAPI
from models import product

app = FastAPI()

# CRUD operations: GET - To Read, PUT - To Update, POST - To Create, DELETE - To Delete
@app.get("/")

def main():
    return "Hello, World!"

prod = [
    product(item_no=1,name="soap",price=46.99,quantity=8,Description="beautiful soap and good frangrence"),
    product(item_no=2,name="cottom",price=20.99,quantity=36,Description="smooth cotton"),
    product(item_no=3,name="conditioner",price=246.99,quantity=25,Description="beautiful conditioner and good frangrence"),
    product(item_no=4,name="shampoo",price=61.99,quantity=81,Description="beautiful shampoo and good frangrence"),
    product(item_no=5,name="towel",price=89.99,quantity=18,Description="smooth cotton towel")
]

@app.get("/products")
def products():
    return prod

#Get -- retrieve
@app.get("/products/{item_no}")
def get_product_by_item(item_no: int):
    for product in prod:
        if product.item_no == item_no:
            return product        
    return "product not found"

#Post -- create
@app.post("/products")
def add_product(product:"product"):
    prod.append(product)
    return product

#Put -- update
@app.put("/products")
def update_product(item_no:int,product:product):
    for i in range(len(prod)):
        if prod[i].item_no == item_no:
            prod[i] = product
            return "Product added sucessfully"
    return "Product not found"

#Delete -- delete
@app.delete("/products")
def delete_a_product(item_no:int):
    for i in range(len(prod)):
        if prod[i].item_no == item_no:
            del prod[i]
            return "Product Deleted sucessfully"
    return "Product not found"             