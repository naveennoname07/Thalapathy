from pyrogram import Client,filters
import logging
import os

from geopy.geocoders import Nominatim

from plugins.shazam.function.pluginhelpers import edit_or_reply
from plugins.shazam.function.basic_helpers import get_text


GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@Client.on_message(filters.command(["gps", "locate"]))
async def gps(client, message):
    engine = message.Engine
    pablo = await edit_or_reply(message, engine.get_string("PROCESSING"))
    args = get_text(message)
    if not args:
        await pablo.edit(engine.get_string("INPUT_REQ").format("Location"))
        return
    try:
        geolocator = Nominatim(user_agent="FridayUB")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
    except Exception as e:
        logging.info(e)
        await pablo.edit(engine.get_string("GPS_2"))
        return
    gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
    await client.send_location(message.chat.id, float(latitude), float(longitude))
    await pablo.reply(
        "Open with: [Google Maps]({})".format(gm),
        disable_web_page_preview=False,
    )
    await pablo.delete()
