from fastapi import APIRouter

router = APIRouter()


@router.get("/start_game")
def start_game():
    return {"message": "Game started"}


@router.get("/end_game")
def end_game():
    return {"message": "Game ended"}
