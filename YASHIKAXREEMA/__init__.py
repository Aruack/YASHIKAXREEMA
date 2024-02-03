from YASHIKAXREEMA.core.bot import Anony
from YASHIKAXREEMA.core.dir import dirr
from YASHIKAXREEMA.core.git import git
from YASHIKAXREEMA.core.userbot import Userbot
from YASHIKAXREEMA.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
