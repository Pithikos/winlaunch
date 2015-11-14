# WinLaunch

A small tool that captures open windows and their positions and generates
a script that can be used to launch those windows again at those positions.

Only tools used are xdotool, xwininfo, xprop which are quite common in Linux.
The tool is very easy to use and although not 100% accurate it is very easy
to tweak in order to bring to your needs.

## Usage

1. Make sure you are in the same directory as the `winlaunch.py` file.
2. Run `python winlaunch.py generate-script`

A Python script will be generated in the same directory containing a snapshot
of all open windows and their location. Feel free to make some alterations to
the script since since small errors might be there (terminals tend to all look
the same for example).

You can run the script with `./launch_script.py`. Have a look below for the
full API.

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
