from re import M
from plugins.VC.logger import LOGGER
try:
   import os
   import heroku3
   from ast import literal_eval as is_enabled
   from pytgcalls.types.input_stream.quality import (
        HighQualityVideo,
        HighQualityAudio,
        MediumQualityAudio,
        MediumQualityVideo,
        LowQualityAudio,
        LowQualityVideo
    )

except ModuleNotFoundError:
    import os
    import sys
    import subprocess
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)


class Config:
    #Telegram API Stuffs
    ADMIN = os.environ.get("ADMINS", '')
    SUDO = [int(admin) for admin in (ADMIN).split()] # Exclusive for heroku vars configuration.
    ADMINS = [int(admin) for admin in (ADMIN).split()] #group admins will be appended to this list.
    API_ID = int(os.environ.get("API_ID", ''))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")     
    SESSION = os.environ.get("SESSION_STRING", "")

    #Stream Chat and Log Group
    CHAT = int(os.environ.get("CHAT", ""))
    LOG_GROUP=os.environ.get("LOG_GROUP", "")

    #Stream 
    STREAM_URL=os.environ.get("STARTUP_STREAM", "https://www.youtube.com/watch?v=zcrUCvBD16k")
   
    #Database
    DATABASE_URI=os.environ.get("DATABASE_URI", None)
    DATABASE_NAME=os.environ.get("DATABASE_NAME", "VCPlayerBot")


    #heroku
    API_KEY=os.environ.get("HEROKU_API_KEY", None)
    APP_NAME=os.environ.get("HEROKU_APP_NAME", None)
    
    #Optional Configuration
    SHUFFLE=is_enabled(os.environ.get("SHUFFLE", 'True'))
    ADMIN_ONLY=is_enabled(os.environ.get("ADMIN_ONLY", "False"))
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", False)
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    #others
    
    RECORDING_DUMP=os.environ.get("RECORDING_DUMP", False)
    RECORDING_TITLE=os.environ.get("RECORDING_TITLE", False)
    TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Kolkata")    
    IS_VIDEO=is_enabled(os.environ.get("IS_VIDEO", 'True'))
    IS_LOOP=is_enabled(os.environ.get("IS_LOOP", 'True'))
    DELAY=int(os.environ.get("DELAY", '10'))
    PORTRAIT=is_enabled(os.environ.get("PORTRAIT", 'False'))
    IS_VIDEO_RECORD=is_enabled(os.environ.get("IS_VIDEO_RECORD", 'True'))
    DEBUG=is_enabled(os.environ.get("DEBUG", 'False'))

    #Quality vars
    BITRATE=os.environ.get("BITRATE", False)
    FPS=os.environ.get("FPS", False)
    CUSTOM_QUALITY=os.environ.get("QUALITY", "HIGH")




    #Dont touch these, these are not for configuring player
    GET_FILE={}
    DATA={}
    STREAM_END={}
    SCHEDULED_STREAM={}
    DUR={}
    msg = {}

    SCHEDULE_LIST=[]
    playlist=[]

    ADMIN_CACHE=False
    CALL_STATUS=False
    YPLAY=False
    YSTREAM=False
    STREAM_SETUP=False
    LISTEN=False
    STREAM_LINK=False
    IS_RECORDING=False
    WAS_RECORDING=False
    PAUSE=False
    MUTED=False
    HAS_SCHEDULE=None
    IS_ACTIVE=None
    VOLUME=100
    CURRENT_CALL=None
    BOT_USERNAME=None
    USER_ID=None

    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    if not API_KEY or \
       not APP_NAME:
       HEROKU_APP=None
    else:
       HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME]


    if EDIT_TITLE in ["NO", 'False']:
        EDIT_TITLE=False
        LOGGER.info("Title Editing turned off")
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
        REPLY_PM=True
        LOGGER.info("Reply Message Found, Enabled PM MSG")
    else:
        REPLY_MESSAGE=None
        REPLY_PM=False

    if BITRATE:
       try:
          BITRATE=int(BITRATE)
       except:
          LOGGER.error("Invalid bitrate specified.")
          BITRATE=False
    else:
       BITRATE=False
    
    if FPS:
       try:
          FPS=int(FPS)
       except:
          LOGGER.error("Invalid FPS specified")
          if BITRATE:
             FPS=False
       if not FPS <= 30:
          FPS=False
    else:
       FPS=False

    if CUSTOM_QUALITY.lower() == 'high':
       VIDEO_Q=HighQualityVideo()
       AUDIO_Q=HighQualityAudio()
    elif CUSTOM_QUALITY.lower() == 'medium':
       VIDEO_Q=MediumQualityVideo()
       AUDIO_Q=MediumQualityAudio()
    elif CUSTOM_QUALITY.lower() == 'low':
       VIDEO_Q=LowQualityVideo()
       AUDIO_Q=LowQualityAudio()
    else:
       LOGGER.warning("Invalid QUALITY specified.Defaulting to High.")
       VIDEO_Q=HighQualityVideo()
       AUDIO_Q=HighQualityVideo()
