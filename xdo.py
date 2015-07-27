'''
Description:
This module makes it super easy to launch graphical programs
and set them in the correct desktops, at specific locations
in the screen, etc. in a fully automated way.

Todo:
    * Allow to pass logname to xrun.
'''

import subprocess
from time import sleep
import re
import sys




# Make sure xdotools is installed
try:
	subprocess.Popen('xdotool', stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
except OSError as e:
	if 'No such file' in e.args[1]:
		print("ERROR: The program 'xdotool' is not installed. Use "\
		      "'sudo apt-get install xdotool' to install it.")
		sys.exit(1)




# ------------------------- Starting processes -------------------------

def run_cmd(cmd):
	''' Command to run separated by blank spaces '''
	proc = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE,
	                                        stderr=subprocess.PIPE)
	return proc
	
def get_proc_output(proc):
	out, err = proc.communicate()
	return out.decode(), err.decode()

def get_cmd_output(cmd):
	return get_proc_output(run_cmd(cmd))

def xrun(cmd):
	''' Run a gui application '''
	open_windows = current_windows()
	proc = run_cmd(cmd)

	# Wait for new proc to open GUI
	while (open_windows == current_windows()):
		sleep(0.2)

	new_wids = [wid for wid in current_windows() if wid not in open_windows]
	if len(new_wids) > 1:
		print('ERROR: xrun(): too many window ids found')
		return None
	if len(new_wids) < 1:
		print('ERROR: xrun(): too few window ids found')
		return None
	wid = int(new_wids[0], 16)
	pid = win_pid(wid)
	return wid, pid




# -------------------------------- X Win -------------------------------

def xdo(do):
	out, err = get_cmd_output('xdotool ' + do)
	if err:
		print('ERROR: %s' % err)
	return out

def win_pid(wid):
	''' Gives the PID of the process that win id belongs to '''
	return xdo('getwindowpid %s' % wid).strip()

def current_windows():
	out, err = get_cmd_output('xprop -root')
	match = re.search(r'_NET_CLIENT_LIST_STACKING\(WINDOW\): window id # (.*)', out)
	if not match:
		return None
	return match.group(1).split(', ')

def win_size(wid, x=None, y=None):
	if not x or not y:
		out = xdo('getwindowgeometry %s' % wid)
		match = re.search(r'Geometry: (.*)', out)
		if not match:
			return None
		return map(int, match.group(1).split('x'))
	else:
		xdo('windowsize %s %s %s' % (wid, x, y))

def win_pos(wid, x=None, y=None):
	if not x or not y:
		out = xdo('getwindowgeometry %s' % wid)
		match = re.search(r'Position: (\d*,\d*)', out)
		if not match:
			return None
		return map(int, match.group(1).split(','))
	else:
		xdo('windowmove %s %s %s' % (wid, x, y))

def win_screen(wid):
	out = xdo('getwindowgeometry %s' % wid)
	match = re.search(r'Position: \d*,\d* \(screen: (\d*)\)', out)
	if not match:
		return None
	return int(match.group(1))

def win_desktop(wid, desktop=None):
	''' Gives the desktop number of the given window '''
	if desktop is None:
		return int(xdo('get_desktop_for_window %s' % wid).strip())
	else:
		return xdo('set_desktop_for_window %s %desktop' % (wid, desktop))
