from fastapi import APIRouter, HTTPException
from models.product import Product, ProductCreate
from db.supabase import supabase, handle_supabase_response

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[Product])
def get_products():
    response = supabase.table("products").select("*").execute()
    return handle_supabase_response(response)

@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    response = supabase.table("products").insert(product.model_dump()).execute()
    data = handle_supabase_response(response)
    return data[0]

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: str, product: ProductCreate):
    response = supabase.table("products").update(product.model_dump(exclude_unset=True)).eq("id", product_id).execute()
    data = handle_supabase_response(response)
    if not data:
        raise HTTPException(status_code=404, detail="Product not found")
    return data[0]

@router.delete("/{product_id}")
def delete_product(product_id: str):
    response = supabase.table("products").delete().eq("id", product_id).execute()
    data = handle_supabase_response(response)
    if not data:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}