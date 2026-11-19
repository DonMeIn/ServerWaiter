import schemas.dishTypes as dish_types
import re
from beanie.operators import RegEx

async def add_dish_reps(dish):
    newDish=dish_types.DishSchema.model_validate(dish.model_dump())
    try:
        await newDish.insert()
        return {"success":True}
    except:
        return {"success":False,"msg":"trouble with DB"}

async def get_dishes_for_menu_reps():
    try:
        dishes=await dish_types.DishSchema.find_all().project(dish_types.DishOutForMenu).to_list()
        return dishes
    except:
        return False
    
async def find_dish_by_id(id:int):
    try:
        dish=await dish_types.DishSchema.find_one(dish_types.DishSchema.dish_id==id)
        return dish
    except:
        return False
    
async def find_dishes_by_name(name:str):
    try:
        safe_query = f"^{re.escape(name)}"
        dish=await dish_types.DishSchema.find(RegEx(dish_types.DishSchema.name,safe_query,options="i")).project(dish_types.DishOutForMenu).to_list()
        return dish
    except:
        return False

async def get_category_reps():
    try:
        category=await dish_types.menu_CategoriesSchema.find_all().project(dish_types.categoryType).to_list()
        return category
    except :
        return False
    
async def add_category_reps(category):
    try:
        newCategory=dish_types.menu_CategoriesSchema.model_validate(category.model_dump())
        await newCategory.insert()
        return True
    except :
        return False

async def get_elements_reps():
    try:
        elements=await dish_types.dish_ElementSchema.find_all().project(dish_types.elementType).to_list()
        return elements
    except :
        return False
    
async def add_element_reps(element):
    try:
        newElement=dish_types.dish_ElementSchema.model_validate(element.model_dump())
        await newElement.insert()
        return True
    except :
        return False

async def delete_element_reps(id:int):
    #try:
        elementForDel=dish_types.dish_ElementSchema.find(dish_types.dish_ElementSchema.element_id==id)
        if elementForDel:
            await elementForDel.delete()
            return True
        else: return None
    #except :
        return False