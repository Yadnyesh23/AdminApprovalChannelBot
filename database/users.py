from database.connection import db

user_cols = db['users']

async def get_user(user_id : int):
    return await user_cols.find_one({"user_id" : user_id })

async def create_user(user_id : int):
    user = await get_user(user_id)
    
    if user : 
        return user
    
    new_user = {
        "user_id" : user_id,
        "status" : "pending"
    }
    
    await user_cols.insert_one(new_user)
    return new_user
 