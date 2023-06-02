from fastapi import APIRouter, HTTPException, Depends, Security, status
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession


from .db.models import Subscriber
from .db.config import get_session
from .db.utils import create_subscriber
from .db.schemas import SubscriberBase

from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(prefix="/api/v1")

api_key_header = APIKeyHeader(name="X-X-KEY", auto_error=True)


async def get_api_key(
    api_key_header: str = Security(api_key_header),
    session: AsyncSession = Depends(get_session),
):
    """
        Validate API KEY
    """
    if api_key_header == os.getenv("XXAPI"):
        
        return True
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
    )


@router.post("/subscribe", dependencies=[Security(get_api_key)])
async def create_new_user(sub: SubscriberBase, session: AsyncSession = Depends(get_session)):
    
    return await create_subscriber(sub, session=session)
