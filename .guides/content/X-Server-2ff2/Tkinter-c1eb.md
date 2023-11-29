# Tkinter in Codio

Tkinter is a popular GUI library for Python, and setting it up in Codio involves a few key steps.

## Installing X Server
Tkinter requires X server for its graphical interface. You can install it within your project by going to `Tools` in the menu bar and selecting `Install Software`.

![Tools](.guides/img/tools_install.png)

In the new tab that opens, search for the X server package by typing `x` in the search box, and then click the blue icon next to it to start the installation.

![Install X Server](.guides/img/install_x_server.png)

When installation completes, select "Reload preview" button (two blue arrows icon) in preview window.

## Running the Python Script
Directly execute the Python script that uses Tkinter using the `TRY IT` button.

```bash
{try it | terminal}(python3 student_code/tkinter_example.py)
```

After clicking `TRY IT`, graphical output should be visible, and you might need to refresh the output using the two blue arrows icon.

{try it | terminal}(python3 student_code/tkinter_example.py)

---
<details>
  <summary>
     <b>Launching command from terminal window</b>
  </summary>

In this updated setup, we use the terminal to run Python scripts, which differs from the previous method of using <code>TRY IT</code> buttons. This change enhances the learning experience for two main reasons:

1. **Error Monitoring:** Running scripts directly in the terminal allows for immediate and clear visibility of any errors or issues, facilitating easier debugging and understanding of your code.

2. **Execution Reliability:** This method ensures consistent and reliable script execution, avoiding timeouts and other constraints that may occur when using button-based commands in the Codio environment.

An alternative is to run the script in the background, which will not open a terminal window or include error feedback.
```bash
{try it | background}(python3 student_code/tkinter_example.py)
```

</details>

---

## Viewing the Output

Codio routes Tkinter output through port 3050. In the [editor settings](https://docs.codio.com/instructors/authoring/guides/page_editing.html#), select the `3 Panels` layout for an organized workspace. Then, in ["Open Tabs"](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#open-tabs), set up two tabs: one for the Python file (`Panel 0`) and another for output preview (`Panel 1`) at `https://{{domain3050}}/`.

![Tkinter Layout](.guides/img/tkinter_layout.png)

This layout places the IDE in the top-left, the output at the bottom-left, and the Guide on the right.

## Understanding Slow Output

The X server operates remotely, not in the student's browser, which means network conditions can impact the graphical output from Tkinter, leading to potential delays or inconsistent animations.