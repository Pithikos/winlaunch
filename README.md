# xdo

A small library that let's you move around, resize, switch between desktops, windows. The library depends on external X tools like xdotool, xwininfo, xprop, etc. These tools are in most cases already installed!

## Dependencies

sudo apt-get install xdotool xprop xwininfo

## API

| Function                     | Description                                                                                                                                      |   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---|
| xrun(command)                | Runs a GUI application in the background. The window id (wid) is returned and the process id (pid) that the window belongs to.                   |   |
| win_size(wid, width, height) | Resizes the window with id `wid` to given width and height values. If no width and height are given, the current size of the window is returned. |   |
| win_pos(wid, x, y)           | Moves the window with id `wid` to the given x and y coordinates. If no x and y are given. the current window position is returned.               |   |
| win_desktop(wid, desktop)    | Sets the window with id `wid` to the given desktop. If desktop is not given the current desktop of the window is returned.                       |   |
| win_screen(wid)              | Gives the current screen where the window with id `wid` is.                                                                                      |   |
