from fastapi import FastAPI

app = FastAPI()

# CRUD operations: GET - To Read, PUT - To Update, POST - To Create, DELETE - To Delete
@app.get("/")

def main():
    return "Hello, World!"

@app.get("/home")

def home():
    return "Welcome to home page"

@app.get("/products")

def products():
    return "Please select any product you like"



             