# Turtle Python in Codio

Setting up a Codio box for Turtle Python involves a few essential steps.

## Installing X Server
Turtle Python requires X server, which can be installed directly within your project. To do so, navigate to `Tools` in the menu bar and select `Install Software`.

![Tools](.guides/img/tools_install.png)

In the new tab that opens, type `x` in the search box to locate the X server package. Click the blue icon next to it to initiate the installation.

![Install X Server](.guides/img/install_x_server.png)

## Running the Python Script
Directly execute the Python script that incorporates Turtle graphics. Ensure it is [configured to use the X server](open_file .guides/turtle_example.py panel=0 ref="import os" count=4), essential for graphical operations.

[Remove highlighting](open_file .guides/turtle_example.py panel=0)

Use the `TRY IT` button for immediate script execution:

```bash
{try it}(python3 .guides/turtle_example.py)
```

Clicking `TRY IT` should produce graphical output, which may require refreshing (via the two blue arrows icon).

{try it}(python3 .guides/turtle_example.py)

## Viewing the Output

Codio channels Tkinter content through port 3050. In the [editor settings](https://docs.codio.com/instructors/authoring/guides/page_editing.html#), choose the `3 Panels` layout for optimal organization: Guide, IDE, and output. Then, under ["Open Tabs"](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#open-tabs), add two tabs – one for the Python file (`Panel 0`) and another for output preview (`Panel 1`) at `https://{{domain3050}}/`.

![Turtle Layout](.guides/img/turtle_layout.png)

This configuration places the IDE top-left, output bottom-left, and the Guide on the right.

## Handling Errors

The `TRY IT` button, when clicked, indicates if the Python script ran successfully.

![Program Ran Successfully](.guides/img/successfully.png)

A successful message signifies script execution, not Python code correctness. For error checking, use an [opening directive](https://docs.codio.com/instructors/authoring/guides/open_close_content.html#) to access the terminal:

```bash
[Open Terminal](open_terminal panel=0)
```

In the terminal, type the command to run your code. To test error handling, deliberately introduce a typo in the `hilbert` function name and observe the behavior.

```python
import os
import turtle

os.environ['DISPLAY'] = ':0.0'  # X11 forwarding setup

t = turtle.Turtle()

def ilbert(dist, rule, angle, depth, t):  # Intentional typo
  """Draw a Hilbert Curve"""
```

{try it}(python3 .guides/turtle_example.py)

[Open Terminal](open_terminal panel=0)

A `name 'hilbert' is not defined` error should be evident.

![Terminal Error](.guides/img/terminal_error.png)

## Understanding Slow Output

The X server operates remotely, not in the student's browser. Consequently, network quality can impact graphical output, potentially causing delays or uneven animations.