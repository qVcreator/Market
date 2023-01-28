from sqlalchemy.ext.asyncio import async_session

from Market.dal.product import ProductDal
from Market.database import Session


async def get_product_dal():
    async with async_session(Session) as session:
        async with session.begin():
            yield ProductDal(session)
