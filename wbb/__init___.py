from info import DATABASE_URI aa MONGO_URL

log.info("Initializing MongoDB client")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.wbb
