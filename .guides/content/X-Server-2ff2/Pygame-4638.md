# Pygame in Codio

The setup process for Pygame in Codio mirrors that of Turtle Python, with a few distinct steps.

## Installing X Server
Pygame requires X server for graphical operations, which you can install within your project. Access this by navigating to `Tools` in the menu bar and selecting `Install Software`.

![Tools](.guides/img/tools_install.png)

A new tab will open, allowing you to search for the X server package by typing `x` in the search box. Initiate the installation by clicking the blue icon next to the X server.

![Install X Server](.guides/img/install_x_server.png)

## Running the Python Script
Execute the Pygame Python script directly, ensuring it [utilizes the X server](open_file .guides/pygame_example.py panel=0 ref="import os" count=4) for graphical displays.

[Remove highlighting](open_file .guides/pygame_example.py panel=0)

Use the `TRY IT` button to run the script easily:

```bash
{try it}(python3 .guides/pygame_example.py)
```

Graphical output should appear upon clicking `TRY IT`, with the option to refresh if necessary (using the two blue arrows icon).

{try it}(python3 .guides/pygame_example.py)

## Viewing the Output

Codio directs Pygame output through port 3050. Configure your workspace in the [editor settings](https://docs.codio.com/instructors/authoring/guides/page_editing.html#) by selecting the `3 Panels` layout. Then, in ["Open Tabs"](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#open-tabs), add two tabs: one to access the Python file (`Panel 0`) and the other for output preview (`Panel 1`) at `https://{{domain3050}}/`.

![Pygame Layout](.guides/img/pygame_layout.png)

This layout positions the IDE in the top-left, output at the bottom-left, and the Guide on the right.

## Handling Errors

Clicking the `TRY IT` button will indicate whether the Python script executed successfully.

![Program Ran Successfully](.guides/img/successfully.png)

A successful run message implies script execution, not necessarily Python code accuracy. For debugging, access the terminal through an [opening directive](https://docs.codio.com/instructors/authoring/guides/open_close_content.html#):

```bash
[Open Terminal](open_terminal panel=0)
```

Run your code in the terminal. For error testing, introduce a typo in a crucial function or class name and note the response.

```python
import os
import pygame

os.environ['DISPLAY'] = ':0.0'  # Setting up X11 forwarding

# Example of intentional error in class name
class all:  
  def __init__(self, surface, color, x, y, r):
  """ Class setup """
```

{try it}(python3 .guides/pygame_example.py)

[Open Terminal](open_terminal panel=0)

Errors, such as `name 'Ball' is not defined`, should now be visible.

![Terminal Error](.guides/img/pygame_error.png)

## Understanding Slow Output

Since the X server operates remotely, network conditions can impact the graphical output from Pygame, potentially causing delays or irregular animations.