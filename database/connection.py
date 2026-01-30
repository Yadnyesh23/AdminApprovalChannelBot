from motor.motor_asyncio import AsyncIOMotorClient
from config.env import MONGO_URI, DB_NAME

mongo = AsyncIOMotorClient(MONGO_URI)
db = mongo[DB_NAME]