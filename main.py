# -*- coding: utf-8 -*-

from resources.lib import kodilogging
from resources.lib import service
from resources.modules import anitopy

import logging
import xbmcaddon

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon()
PLAYER = xbmc.Player()

kodilogging.config()

service.KitsuService(PLAYER)
