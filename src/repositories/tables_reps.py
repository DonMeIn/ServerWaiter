import schemas.tablesTypes as types
import secrets 
async def get_all_tables_reps():
    try:
        tables=await types.tablesSchema.find_all().project(types.tableType).to_list()
        return tables
    except: 
        return False
async def get_all_halls_reps():
    try:
        halls=await types.hallSchema.find_all().project(types.hallType).to_list()
        return halls
    except :
        return False
async def get_tables_by_hall_reps(id:int):
    try:
        tables=await types.tablesSchema.find_many(types.tablesSchema.hall_id==id).project(types.tableType).to_list()
        return tables
    except:
        return False
async def add_new_table_reps(hall):
    try:
        newhall=hall.model_dump()
        if await types.hallSchema.find(types.hallSchema.hall_id==newhall["hall_id"]).exists():
            newTable=types.tablesSchema.model_validate({"hall_id":newhall["hall_id"]})
            await newTable.insert()
            return True
        else: return None
        
    except:
        return False
async def delete_table_reps(hallId):
    try:
        tableForDel=await types.tablesSchema.find(types.tablesSchema.hall_id==hallId).sort("-name").first_or_none()
        if tableForDel:
            await tableForDel.delete()
            return True
        else:return None
    except:return False
async def delete_tables_reps(hallId):
    try:
        result=await types.tablesSchema.find(types.tablesSchema.hall_id==hallId).delete()
        if not result or not result.acknowledged:
            return None
        else:return True
    except:return False
async def add_new_hall_reps(hall):
    try:
        newTable=types.hallSchema.model_validate(hall.model_dump())
        await newTable.insert()
        return True
    except:
        return False
    
async def delete_hall_reps(hallId):
    try:
        hallForDel=await types.hallSchema.find(types.hallSchema.hall_id==hallId).first_or_none()
        if hallForDel:
            await hallForDel.delete()
            return True
        return None
    except:
        return False