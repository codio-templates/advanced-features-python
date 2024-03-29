# Turtle Python in Codio

Setting up a Codio box for Turtle Python involves a few essential steps.

## Installing X Server
Turtle Python requires X server, which can be installed directly within your project. To do so, navigate to `Tools` in the menu bar and select `Install Software`.

![Tools](.guides/img/tools_install.png)

In the new tab that opens, type `x` in the search box to locate the X server package. Click the blue icon next to it to initiate the installation.

![Install X Server](.guides/img/install_x_server.png)

When installation completes, select "Reload preview" button (two blue arrows icon) in preview window.

## Running the Python Script
Directly execute the Python script that incorporates Turtle graphics using the `TRY IT` button:

```bash
{try it | terminal}(python3 student_code/turtle_example.py)
```

Clicking `TRY IT` should produce graphical output, which may require refreshing (via the two blue arrows icon).

{try it | terminal}(python3 student_code/turtle_example.py)

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
{try it | background}(python3 student_code/turtle_example.py)
```

</details>

---

## Viewing the Output

Codio channels Tkinter content through port 3050. In the [editor settings](https://docs.codio.com/instructors/authoring/guides/page_editing.html#), choose the `3 Panels` layout for optimal organization: Guide, IDE, and output. Then, under ["Open Tabs"](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html#open-tabs), add two tabs – one for the Python file (`Panel 0`) and another for output preview (`Panel 1`) at `https://{{domain3050}}/`.

![Turtle Layout](.guides/img/turtle_layout.png)

This configuration places the IDE top-left, output bottom-left, and the Guide on the right.


## Understanding Slow Output

The X server operates remotely, not in the student's browser. Consequently, network quality can impact graphical output, potentially causing delays or uneven animations.