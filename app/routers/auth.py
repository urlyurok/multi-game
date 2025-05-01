from fastapi import APIRouter

router = APIRouter()


@router.get("/login")
def login():
    return {"message": "Login endpoint"}


@router.get("/register")
def register():
    return {"message": "Register endpoint"}
