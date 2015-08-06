#! /usr/bin/python
from winlaunch import *

# Nautilus
wid, pid = launch('nautilus /home/manos/tmp/coda')
win_size(wid, 568, 777)
win_pos(wid,  -18, 12)
win_desktop(wid, 0)

# IDE
wid, pid = launch('subl')
win_size(wid, 829, 701)
win_pos(wid,  536, 66)
win_desktop(wid, 0)

# Open hipchat
wid, pid = launch('hipchat')
win_size(wid, 733, 700)
win_pos(wid,  642, 113)
win_desktop(wid, 1)

# FreeAgent
URL = 'https://www.google.com'
wid, pid = launch('chromium-browser --incognito %s' % URL)
win_size(wid, 979, 699)
win_pos(wid,  396, 113)
win_desktop(wid, 1)
