# Pygame and Codio

In terms of setting up Pygame in Codio, it is an identical process to that of Turtle Python.

## Installing X Server
Pygame requires the use of X server. This can be installed from within the project. Click `Tools` in the menu bar, and then select `Install Software`.

![Tools](.guides/img/tools_install.png)

Codio will open a new tab with additional software you can install. In the search box, type `x` to find the X server package. Click the blue icon next to X server to install it.

![Install X Server](.guides/img/install_x_server.png)

## Bash Script

Instead of calling the Python script directly, the Python script is passed to a bash script which invokes X server and generates graphical output. Create a file in `.guides` called `bg.sh` and copy/paste the code below into the script.

```bash
#!/bin/bash
set -e 
set -o pipefail

. /etc/profile.d/codio-xserver.sh

$1 -m py_compile $2

nohup $@ > /dev/null 2>&1&
```

Use the `TRY IT` button to call the `bg.sh` script and pass it the `python3` command and the path to the Python file.

```
{try it}(bash .guides/bg.sh python .guides/pygame_example.py)
```

The `TRY IT` button should now run the code and produce graphical output.

{try it}(bash .guides/bg.sh python .guides/pygame_example.py)

|||warning
You might have noticed that the Python commands are called with `python` and not `python3`. Pygame is preinstalled on the Python stack, but it is installed for Python 2 and not Python 3. Pygame works with Python 3, but you would have to use `pip3 install pygame` before hand.
|||

## Viewing the Output

Codio displays the content of Turtle Python on port 3000. In the [editor settings](https://docs.codio.com/courses/authoring/#editor-settings), select the [layout](https://docs.codio.com/courses/settings-actions/#page) that says `3 Panels without tree` (one panel for the Guide, one for the IDE, and the third for the output). Next click on ["Open Tabs"](https://docs.codio.com/courses/settings-actions/#open-tabs_1) and add two tabs. One tab should open a file. Enter the path for the Python file and set the "Panel" to 0. The second tab should preview (eye icon) the output. Ener `https://{{domain3000}}/`, which is how Codio addresses port 3000. Set this "Panel" to 1. 

![Pygame Layout](.guides/img/pygame_layout.png)

The IDE should be in the top-left, the output in the bottom-left, and the Guide will appear on the right.

## Errors

The `TRY IT` button runs the bash script, which runs without error every time. So the output in the guide will always be that the program ran successfully. 

![Program Ran Successfully](.guides/img/successfully.png)

This message does not refer to the Python code. So the output window will not appear if there is a bug in the Python code, but there is no visual feedback in the Guide on what went wrong. This makes debugging hard. If the Python code is called from the terminal, error messages will appear. You can use an [opening directive](https://docs.codio.com/courses/authoring/#examples) to open a terminal in a panel. 

```
[Open Terminal](open_terminal panel=0)
```

In the open terminal, students can type in the command to run their code. Try this out by removing the "B" from the `Ball` class declaration. Click on the `TRY IT` button. No error message. 

```python
import pygame

class all:
  def __init__(self, surface, color, x, y, r):
```

{try it}(bash .guides/bg.sh python .guides/pygame_example.py 1)

Click on the `TRY IT` button. No error message, but there is no output. Click on the link below to open the terminal and enter `python .guides/pygame_example.py`.

[Open Terminal](open_terminal panel=0)

You should see the error message that `name 'Ball' is not defined`.

![Terminal Error](.guides/img/pygame_error.png)

## Slow Output

X server is not running in the student's browser. It is running in a data center somewhere. So the graphical output has to travel across the network. Poor connections or heavy traffic can affect the output. Students may encounter slight pauses or "jumpy" animation.