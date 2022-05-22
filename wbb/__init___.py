from info import DATABASE_URI as MONGO_URL

log.info("Initializing MongoDB client")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.wbb
