from beanie import Document, Insert, before_event
import secrets
from pydantic import BaseModel,EmailStr,Field,model_validator
class newCategoryType(BaseModel):
     name:str=Field(min_length=2,max_length=15)
     isDrink:bool|None=Field(default=False)
class menu_CategoriesSchema(Document):
    name:str=Field(min_length=2,max_length=15)
    category_id:int|None=Field(default=None)
    isDrink:bool=Field(default=False)
    @before_event(Insert)
    async def create_id(self):
         if self.category_id is None:
            for _ in range(20):
                   new_id=secrets.randbelow(800)+100
                   if not await menu_CategoriesSchema.find_one(menu_CategoriesSchema.category_id==new_id).exists():
                        self.category_id=new_id
                        return
            raise RuntimeError("Не удалось сгенерировать уникальный ID...")

    class Settings:
            name = "menu_categories"


class ElementsInDish(BaseModel):
     element_id:int
     count:int=Field(lt=100_000)
class newDishType(BaseModel):
     name: str=Field(min_length=2,max_length=15)
     category_id:int=Field(lt=100_000)
     price:int=Field(lt=100_000_000)
     elements: list[ElementsInDish]|None=Field(default=None)
class DishSchema(Document):
    name: str=Field(min_length=2,max_length=15)
    dish_id:int|None=Field(default=None)
    category_id:int=Field(lt=100_000)
    price:int=Field(lt=100_000_000)
    elements: list[ElementsInDish]|None
    @before_event(Insert)
    async def create_id(self):
         if(self.dish_id is None):
            for _ in range(20):
                   new_id = secrets.randbelow(90000) + 10000
                   if not await DishSchema.find_one(DishSchema.dish_id==new_id).exists():
                        self.dish_id=new_id
                        return
            raise RuntimeError("Не удалось сгенерировать уникальный ID...")
         
    class Settings:
        name = "dishes"
class DishOutForMenu(BaseModel):
     name:str
     dish_id:int
     category_id:int
     price:int

class newElementType(BaseModel):
     name:str
class categoryType(BaseModel):
     name:str
     category_id:int
     isDrink:bool
class dish_ElementSchema(Document):
    name:str=Field(min_length=2,max_length=15)
    element_id:int|None=Field(default=None)
    @before_event(Insert)
    async def create_id(self):
              if(self.element_id is None):
                 for _ in range(20):
                        new_id = secrets.randbelow(9000) + 1000
                        if not await dish_ElementSchema.find_one(dish_ElementSchema.element_id==new_id).exists():
                             self.element_id=new_id
                             return
                 raise RuntimeError("Не удалось сгенерировать уникальный ID...")  
    class Settings:
             name = "elements"
class elementType(BaseModel):
     name:str
     element_id:int
