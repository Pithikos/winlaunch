# WinLaunch

A small tool that let's you save the position of open windows directly into
a script file that you can run alone to restore those windows later. This is
based on X tools like xdotool, xwininfo, xprop, etc.

The tool is very easy to use and although not 100% accurate it is very easy
to tweak in order to bring to your needs.

## Usage

1. Open a Python prompt in the directory where WinLaunch resides
2. Run `from winlaunch import scriptify; scriptify.open_windows()`

A file called launch_script.py should have been generated in the same directory.
If you close all open windows and run that script with `./launch_script.py` the
windows will be restored.

## Dependencies

sudo apt-get install xdotool xprop xwininfo

## API

| Function                     | Description                                                                                                                                      |   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---|
| launch(command)              | Runs a GUI application in the background. The window id (wid) is returned and the process id (pid) that the window belongs to.                   |   |
| win_size(wid, width, height) | Resizes the window with id `wid` to given width and height values. If no width and height are given, the current size of the window is returned. |   |
| win_pos(wid, x, y)           | Moves the window with id `wid` to the given x and y coordinates. If no x and y are given. the current window position is returned.               |   |
| win_desktop(wid, desktop)    | Sets the window with id `wid` to the given desktop. If desktop is not given the current desktop of the window is returned.                       |   |
| win_screen(wid)              | Gives the current screen where the window with id `wid` is.                                                                                      |   |
| scriptify.open_windows(filename) | Will generate a script file that can be run to restore the current state of all open windows.
