import logging,asyncio
from pyrogram import Client

API_KEY = 20058505
API_HASH = "c6416428be72db3174999c1740524b88"
BOT_TOKEN = "6563744619:AAG4v_ABfLA3lCSGbcNLWlS07ZA_qUmseqM"

loop = asyncio.get_event_loop()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger('joinbot')

app = Client(
    "appname",
    api_id=API_KEY,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
