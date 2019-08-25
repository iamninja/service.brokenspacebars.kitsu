# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
from resources.modules.anitopy import anitopy

import logging
import time
import xbmc
import xbmcaddon


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))


class KitsuService():

    def __init__(self, player):
        self.player = player
        self.run()

    def run(self):
        monitor = xbmc.Monitor()

        while not monitor.abortRequested():
            if self.player.isPlayingVideo():
                logger.debug("Player is playing video: %s" %
                             self.player.getPlayingFile())
                filename = xbmc.getInfoLabel('Player.Filename')
                logger.debug("filename: %s" % filename)
                kodiutils.notification("Kitsu", filename)
                data = anitopy.parse(filename)
                logger.debug(data)
            # Sleep/wait for abort for 10 seconds
            if monitor.waitForAbort(5):
                # Abort was requested while waiting. We should exit
                break
            logger.debug("hello addon! %s" % time.time())
