from fastapi import APIRouter,HTTPException
import services.table_services as services
import schemas.tablesTypes as types

router=APIRouter(prefix="/tables",tags=["tables"])

@router.get("")
async def get_tables(hall:int|None=None)->list[types.tableType]|None:
    if hall:
        result=await services.get_tables_by_hall_srv(hall)
        if result:
            return result
        elif result==False:
            raise HTTPException(status_code=400, detail={"detail": "hall is not finded"})
        else:return result
    else:
        result=await services.get_all_tables_srv()
        if result:
            return result
        elif result==False:
            raise HTTPException(status_code=400, detail={"detail": "something goes wrong"})
        else:return result

@router.get("/hall")
async def get_halls()->list[types.hallType]|None:
    result=await services.get_all_halls_srv()
    if result==False:
        raise HTTPException(status_code=400, detail={"detail": "something goes wrong"})
    else:return result

@router.post("")
async def add_table(hall_id:types.newTableType)->bool:
    result=await services.add_table_srv(hall_id)
    if result==True:
        return result
    elif result==None:
        raise HTTPException(status_code=400, detail={"detail": "HallId is wrong"})
    else:
        raise HTTPException(status_code=400, detail={"detail": "something goes wrong"})
@router.delete("")
async def delete_table(hall_id:int)->bool:
    result =await services.delete_table_srv(hall_id)
    if result==True:
            return result
    elif result==None:
        raise HTTPException(status_code=400, detail={"detail": "no table"})
    else:
        raise HTTPException(status_code=400, detail={"detail": "something goes wrong"})

@router.post("/hall")
async def add_hall(hall:types.newHallType)->bool:
    result=await services.add_hall_srv(hall)
    if result==True:
        return result
    else:raise HTTPException(status_code=400, detail={"detail": "something goes wrong"})
    
@router.delete("/hall")
async def delete_hall(hall_id:int)->bool:
    result=await services.delete_hall_srv(hall_id)
    if result==True:
        return result
    else:raise HTTPException(status_code=400, detail={"detail": "something goes wrong"})
    
    
