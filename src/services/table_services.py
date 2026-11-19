import repositories.tables_reps as reps
async def get_all_tables_srv():
    return await reps.get_all_tables_reps()
async def get_all_halls_srv():
    return await reps.get_all_halls_reps()
async def get_tables_by_hall_srv(id:int):
    return await reps.get_tables_by_hall_reps(id)
async def add_table_srv(table):
    return await reps.add_new_table_reps(table)
async def delete_table_srv(hall):
    return await reps.delete_table_reps(hall)
async def add_hall_srv(hall):
    return await reps.add_new_hall_reps(hall)
async def delete_hall_srv(hall):
    tablesIsDeleted=await reps.delete_tables_reps(hall)
    if tablesIsDeleted:
        return await reps.delete_hall_reps(hall)
    return tablesIsDeleted