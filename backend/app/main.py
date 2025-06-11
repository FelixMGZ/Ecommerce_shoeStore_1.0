from fastapi import FastAPI
from core.config import setup_cors
from api import products, users, orders


app = FastAPI()
setup_cors(app)

app.include_router(products.router)
app.include_router(users.router)
app.include_router(orders.router)