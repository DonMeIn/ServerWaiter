import repositories.order_reps as reps
async def event_check_srv(event):
    if await reps.check_order_reps(event.id):
        result=await reps.add_dish_in_order_reps(event)

    return 