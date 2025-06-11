from fastapi import APIRouter
from models.order import OrderCreate
from db.supabase import supabase, handle_supabase_response

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/")
def get_orders():
    response = supabase.table("orders").select("*").execute()
    if not hasattr(response, "data") or response.data is None:
        return []
    return response.data

@router.post("/")
def create_order(order: OrderCreate):
    response = supabase.table("orders").insert(order.model_dump()).execute()
    data = handle_supabase_response(response)
    return {"message": "Orden guardada", "order": data[0] if data else order}