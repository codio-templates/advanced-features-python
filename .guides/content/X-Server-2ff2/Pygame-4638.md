# Pygame in Codio

The setup process for Pygame in Codio mirrors that of Turtle Python, with a few distinct steps.

## Installing X Server
Pygame requires X server for graphical operations, which you can install within your project. Access this by navigating to `Tools` in the menu bar and selecting `Install Software`.

![Tools](.guides/img/tools_install.png)

A new tab will open, allowing you to search for the X server package by typing `x` in the search box. Initiate the installation by clicking the blue icon next to the X server.

![Install X Server](.guides/img/install_x_server.png)

When installation completes, select "Reload preview" button (two blue arrows icon) in preview window.

## Running the Python Script
Execute the Pygame Python script directly using the `TRY IT` button:

```bash
{try it | terminal}(python3 student_code/pygame_example.py)
```

Graphical output should appear upon clicking `TRY IT`, with the option to refresh if necessary (using the two blue arrows icon).

{try it | terminal}(python3 student_code/pygame_example.py)

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
{try it | background}(python3 student_code/pygame_example.py)
```

</details>

---

## Viewing the Output

Codio directs Pygame output through port 3050. Configure your workspace in the [editor settings](https://docs.codio.com/instructors/authoring/guides/page_editing.html#) by selecting the `3 Panels` layout. Then, in ["Open Tabs"](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#open-tabs), add two tabs: one to access the Python file (`Panel 0`) and the other for output preview (`Panel 1`) at `https://{{domain3050}}/`.

![Pygame Layout](.guides/img/pygame_layout.png)

This layout positions the IDE in the top-left, output at the bottom-left, and the Guide on the right.

## Understanding Slow Output

Since the X server operates remotely, network conditions can impact the graphical output from Pygame, potentially causing delays or irregular animations.