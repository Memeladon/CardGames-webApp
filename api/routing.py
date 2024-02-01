from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = APIRouter(
    # prefix='/Games',
    tags=['CardGames'],
    responses={404: {"description": "Not found"}}
)

templates = Jinja2Templates(directory='../frontend/templates')


@router.get('/')
def get_main_page(request: Request):
    return templates.TemplateResponse("main.html", {'request': request})


@router.get('/blackjack')
def get_main_page(request: Request):
    return templates.TemplateResponse("blackjack.html", {'request': request})
