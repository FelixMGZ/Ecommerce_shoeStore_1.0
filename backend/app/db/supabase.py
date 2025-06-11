import os
from supabase import create_client, client
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: client = create_client(url, key)

def handle_supabase_response(response):
    if not response.data:
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail="Supabase error: No data returned")
    return response.data