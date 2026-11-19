import schemas.eventTypes as types
async def create_order_reps(order):
    return
async def add_dish_in_order_reps(order):
    
    return 
async def check_order_reps(order):
    return await types.orderSchema.find(types.orderSchema.order_id==order.order_id).exists()