from fastapi import APIRouter   

router = APIRouter()

@router.get('/')
async def get_users():
    return {'message': 'Get Users!'}

@router.get('/new')
async def create_users():
    return {'message': 'Create Users'}