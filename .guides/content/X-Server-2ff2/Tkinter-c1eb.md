# Tkinter in Codio

Tkinter is a popular GUI library for Python, and setting it up in Codio involves a few key steps.

## Installing X Server
Tkinter requires X server for its graphical interface. You can install it within your project by going to `Tools` in the menu bar and selecting `Install Software`.

![Tools](.guides/img/tools_install.png)

In the new tab that opens, search for the X server package by typing `x` in the search box, and then click the blue icon next to it to start the installation.

![Install X Server](.guides/img/install_x_server.png)

## Running the Python Script
Directly execute the Python script that uses Tkinter, making sure it is [configured to utilize the X server](open_file .guides/tkinter_example.py panel=0 ref="import os" count=4).

[Remove highlighting](open_file .guides/tkinter_example.py panel=0)

Use the `TRY IT` button for immediate execution:

```bash
{try it}(python3 .guides/tkinter_example.py)
```

After clicking `TRY IT`, graphical output should be visible, and you might need to refresh the output using the two blue arrows icon.

{try it}(python3 .guides/tkinter_example.py)

## Viewing the Output

Codio routes Tkinter output through port 3050. In the [editor settings](https://docs.codio.com/instructors/authoring/guides/page_editing.html#), select the `3 Panels` layout for an organized workspace. Then, in ["Open Tabs"](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#open-tabs), set up two tabs: one for the Python file (`Panel 0`) and another for output preview (`Panel 1`) at `https://{{domain3050}}/`.

![Tkinter Layout](.guides/img/tkinter_layout.png)

This layout places the IDE in the top-left, the output at the bottom-left, and the Guide on the right.

## Handling Errors

The `TRY IT` button shows if the Python script ran successfully.

![Program Ran Successfully](.guides/img/successfully.png)

A successful message indicates script execution, not the correctness of the Python code. To debug, use an [opening directive](https://docs.codio.com/instructors/authoring/guides/open_close_content.html#) to access the terminal:

```bash
[Open Terminal](open_terminal panel=0)
```

In the terminal, run your code. Introduce an intentional error, like a typo, to test error detection.

```python
import os
import tkinter

os.environ['DISPLAY'] = ':0.0'  # X11 forwarding setup

window = tkinter.Tk()
window.title("My Window")
window.geometry("500x350")

# Intentional error in function call
my_label = tkinter.Label(window, text="Hello World", font="DejaVuSerif 18")
mylabel.grid(row=0, column=0)  # Misspelled variable

window.mainloop()
```

{try it}(python3 .guides/tkinter_example.py)

[Open Terminal](open_terminal panel=0)

Look for an error message, such as `name 'mylabel' is not defined`.

![Terminal Error](.guides/img/tkinter_error.png)

## Understanding Slow Output

The X server operates remotely, not in the student's browser, which means network conditions can impact the graphical output from Tkinter, leading to potential delays or inconsistent animations.