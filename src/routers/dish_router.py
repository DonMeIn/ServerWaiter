from fastapi import APIRouter,HTTPException
import schemas.dishTypes as dish_types
import services.dish_services as services
from starlette.responses import JSONResponse
router=APIRouter(prefix="/dish",tags=["dishes"])


@router.get("", response_model=list[dish_types.DishOutForMenu])
async def get_dishes(search:str|None=None)->list[dish_types.DishOutForMenu]|JSONResponse:
    if isinstance(search,str):
        dishes=await services.find_dish_by_name_srv(search)
        return dishes if dishes else JSONResponse(status_code=200, content={"detail": "Nothing is founded"})
    dishes = await services.get_dishes_srv()
    return dishes if dishes else JSONResponse(status_code=400, content={"detail": "some trouble"})


@router.get("/edit")
async def get_dish(id:int):
    dishes=await services.find_dish_by_id_srv(id)
    return dishes if dishes else JSONResponse(status_code=400, content={"detail": "some trouble"})

@router.post("")
async def add_dish(dish:dish_types.newDishType):
    result= await services.add_new_dish_srv(dish)
    return result if result else JSONResponse(status_code=400, content={"detail": "some trouble"})

@router.post("/categories")
async def add_category(category:dish_types.newCategoryType)->bool:
    result=await services.add_new_category_srv(category)
    if result:
        return result 
    else:raise HTTPException(status_code=400, detail={"detail": "some trouble"})

@router.get("/categories")
async def get_categories()->list[dish_types.categoryType]:
    result=await services.get_category_srv()
    if result==None or result:
        return result
    else :raise HTTPException(status_code=400, detail={"detail": "some trouble"})

@router.post("/elements")
async def add_element(element:dish_types.newElementType)->bool:
    result=await services.add_new_elements_srv(element)
    if result:
        return True
    else:raise HTTPException(status_code=400, detail={"detail": "some trouble"})

@router.delete("/elements")
async def delete_element(element_id:int)->bool:
    result=await services.delete_elements_srv(element_id)
    if result:
        return True
    else:raise HTTPException(status_code=400, detail={"detail": "some trouble"})

@router.get("/elements")
async def get_elements()->list[dish_types.elementType]:
    result=await services.get_elements_srv()
    if result is not None:
        return result or []
    else:
        raise HTTPException(status_code=400, detail={"detail": "some trouble"})