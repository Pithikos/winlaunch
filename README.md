# WinLaunch

A small tool that let's you save the position of open windows directly into
a script file that you can run alone to restore those windows later. This is
based on X tools like xdotool, xwininfo, xprop, etc.

The tool is very easy to use and although not 100% accurate it is very easy
to tweak in order to bring to your needs.

## Usage

1. Make sure you are in the same directory as the `winlaunch.py` file.
2. Run `python -B -c 'import winlaunch; winlaunch.scriptify.open_windows()'`

A file called launch_script.py will get generated in the same directory. This
script contains the instructions to launch all currently open windows to their
current positions. You can test this by closing everything and running `./launch_script.py`.
Notice that minor mistakes might be apparent in the script (ie. launch commands). These
can easily be fixed by having a look in the script.

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
