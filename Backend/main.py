import db_model
from data_init import products
from datavalidation import Product
from sqlalchemy.orm import Session
from db_config import session,engine
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_model.Base.metadata.create_all(bind = engine)

# Read operations
@app.get("/home")
def greet():
    return "Welcome to the page"


# func for getting session
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# sql initializing
def init_db():
    db = session()
    count = db.query(db_model.Product).count()
    if count == 0:
        for p in products:
            db.add(db_model.Product(**p.model_dump()))
        db.commit()
init_db()

# Read operations
@app.get("/products")
def product(db: Session = Depends(get_db)):
    db_products = db.query(db_model.Product).all()
    return db_products

# Read operations
@app.get("/products/{id}")
def get_product(id:int, db: Session = Depends(get_db)):
    try:
        db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
        if db_product:
            return db_product
    except:
        return "Product Not Found"
    
# create operations
@app.post("/products")
def add_product(p: Product, db: Session = Depends(get_db)):
    db.add(db_model.Product(**p.model_dump()))
    db.commit()
    return "Product added sucessfully"

# update operations
@app.put("/products/{id}")
def update_product(id:int, product:Product, db: Session = Depends(get_db)):
    try:
        db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
        if db_product:
            db_product.name = product.name
            db_product.price = product.price
            db_product.description = product.description
            db_product.quantity = product.quantity
            db.commit()
            return "Product updated sucessfully"
    except:
        return "Product Not Found"
    
# delete operations
@app.delete("/products/{id}")
def delete_product(id:int, db: Session = Depends(get_db)):
    try:
        db_product = db.query(db_model.Product).filter(db_model.Product.id == id).first()
        if db_product:
            db.delete(db_product)
            db.commit()
            return "Product remove sucessfully"
    except:
        return "Product Not Found"