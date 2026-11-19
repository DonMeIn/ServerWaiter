import repositories.dish_reps as reps
import schemas.dishTypes as dish_types
async def get_dishes_srv():
    return await reps.get_dishes_for_menu_reps()
async def add_new_dish_srv(dish):
    return await reps.add_dish_reps(dish)
async def find_dish_by_name_srv(dish_id_or_name):
    return await reps.find_dishes_by_name(dish_id_or_name)
async def find_dish_by_id_srv(dish_id_or_name):
    return await reps.find_dish_by_id(dish_id_or_name)
async def get_category_srv():
    return await reps.get_category_reps()
async def add_new_category_srv(category):
    return await reps.add_category_reps(category)
async def get_elements_srv():
    return await reps.get_elements_reps()
async def add_new_elements_srv(element):
    return await reps.add_element_reps(element)
async def delete_elements_srv(id):
    return await reps.delete_element_reps(id)
