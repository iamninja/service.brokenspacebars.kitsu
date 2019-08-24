# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
import logging
import time
import xbmc
import xbmcaddon


ADDON = xbmcaddon.Addon()
PLAYER = xbmc.Player()

logger = logging.getLogger(ADDON.getAddonInfo('id'))


def run():
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        if PLAYER.isPlayingVideo():
            logger.debug("Player is playing video: %s" %
                         PLAYER.getPlayingFile())
            logger.debug("Metadata: %s" % PLAYER.getVideoInfoTag().getTitle())
            print(PLAYER.getVideoInfoTag())
            logger.debug("Metadata: %s" %
                         PLAYER.getVideoInfoTag().getTVShowTitle())
            logger.debug("Metadata: %s" %
                         PLAYER.getVideoInfoTag().getEpisode())
            kodiutils.notification("Kitsu", PLAYER.getPlayingFile())
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(5):
            # Abort was requested while waiting. We should exit
            break
        logger.debug("hello addon! %s" % time.time())
