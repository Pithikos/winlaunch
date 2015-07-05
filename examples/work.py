#! /usr/bin/python

from xdo import *

# Nautilus
wid, pid = xrun('nautilus /home/manos/tmp/coda')
win_size(wid, 568, 777)
win_pos(wid,  -18, 12)
win_desktop(wid, 0)

# IDE
wid, pid = xrun('subl')
win_size(wid, 829, 701)
win_pos(wid,  536, 66)
win_desktop(wid, 0)

# Open hipchat
wid, pid = xrun('hipchat')
win_size(wid, 733, 700)
win_pos(wid,  642, 113)
win_desktop(wid, 1)

# FreeAgent
URL = 'https://www.google.com'
wid, pid = xrun('chromium-browser --incognito %s' % URL)
win_size(wid, 979, 699)
win_pos(wid,  396, 113)
win_desktop(wid, 1)
