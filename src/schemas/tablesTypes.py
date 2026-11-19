from beanie import Document,before_event,Insert
from pydantic import Field,BaseModel
import secrets


class tablesSchema(Document):
    table_id:int|None=None
    name:int|None=None
    hall_id:int
    isFree:bool|None=None
    order_id:int|None=None
    @before_event(Insert)
    async def create_id(self):
        for _ in range(20):
                new_id=secrets.randbelow(900)+100
                if not await tablesSchema.find_one(tablesSchema.table_id==new_id).exists():
                        self.table_id=new_id
                        self.name=await tablesSchema.find(tablesSchema.hall_id==self.hall_id).count()+1
                        self.isFree=False
                        return
        raise(RuntimeError("Не удалось сгенерировать уникальный ID...")) 
          
    class Settings:
            name="tables"

class hallSchema(Document):
    hall_id:int|None=None
    name:str=Field(min_length=3,max_length=10)
    @before_event(Insert)
    async def create_id(self):
            for _ in range(20):
                    new_id=secrets.randbelow(900)+100
                    if not await hallSchema.find_one(hallSchema.hall_id==new_id).exists():
                            self.hall_id=new_id
                            return
            raise(RuntimeError("Не удалось сгенерировать уникальный ID..."))       
    class Settings:
                name="hall"

class tableType(BaseModel):
       name:int
       table_id:int
       hall_id:int
class hallType(BaseModel):
        hall_id:int
        name:str=Field(min_length=3,max_length=10)
class newTableType(BaseModel):
        hall_id:int
class newHallType(BaseModel):
        name:str=Field(min_length=3,max_length=10)
class deleteByIdType(BaseModel):
       id:int