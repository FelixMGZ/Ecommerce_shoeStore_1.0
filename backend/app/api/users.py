from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserOut
from db.supabase import supabase, handle_supabase_response
from core.security import hash_password, verify_password

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
def get_users():
    response = supabase.table("users").select("*").execute()
    return handle_supabase_response(response)

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate):
    hashed_pw = hash_password(user.password)
    user_data = user.model_dump(exclude={"password"})
    user_data["hashed_password"] = hashed_pw
    response = supabase.table("users").insert(user_data).execute()
    data = handle_supabase_response(response)
    return data[0]

@router.post("/login")
def login(user: UserCreate):
    response = supabase.table("users").select("*").eq("email", user.email).execute()
    data = handle_supabase_response(response)
    if not data:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    user_db = data[0]
    if not verify_password(user.password, user_db["hashed_password"]):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    return {
        "message": "Login exitoso",
        "user": {
            "id": user_db["id"],
            "email": user_db["email"],
            "full_name": user_db["full_name"],
            "rol": user_db["rol"]
        }
    }