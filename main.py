from fastapi import FastAPI
from models import product

app = FastAPI()

# CRUD operations: GET - To Read, PUT - To Update, POST - To Create, DELETE - To Delete
@app.get("/")

def main():
    return "Hello, World!"

prod = [
    product(item_no=1,name="soap",price=46.99,quantity=8,Description="beautiful soap and good frangrence")
]

@app.get("/products")
def products():
    return prod


@app.get("/products/{item_no}")
def get_product_by_item(item_no: int):
    for product in prod:
        if product.item_no == item_no:
            return product
        
    return "product not found"
             