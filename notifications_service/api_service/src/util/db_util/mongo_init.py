from db.mongo import get_mongo_client

TEMPLATE_NAME_TO_FIELDS_MAPPING = {
    "user_registered.html": ["first_name", "last_name"],
    "new_episode.html": ["first_name", "last_name", "movie"]
}

NOTIFICATION_ID_TO_CHANNEL_MAPPING = {
    "user_registered": "email",
    "new_episode": "email",
    "most_viewed_movies": "email",
    "custom_distribution": "any"
}

NOTIFICATION_IDS = [
    "user_registered",
    "new_episode",
    "most_viewed_movies",
    "custom_distribution"
]


async def init_notifications_db():
    client = get_mongo_client()

    db = client.get_database("notifications_db")
    collection = db.get_collection("notifications")

    await populate_notifications_data(collection)


async def populate_notifications_data(collection):
    for notification_id in NOTIFICATION_IDS:
        notification = await collection.find_one({
            "id": notification_id
        })

        if notification is not None:
            continue

        await collection.insert_one({
            "id": notification_id,
            "channel": NOTIFICATION_ID_TO_CHANNEL_MAPPING[notification_id]
        })
