from fastapi import APIRouter
import schemas.eventTypes as types
import services.event_services as services
router=APIRouter(prefix="/event",tags=["events"])

@router.post("")
async def AddOrder(order:types.OrderInputType):
    await services.event_check_srv(order)
    return 