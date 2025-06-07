# 1. Install Python

- Windows: Download from the [Microsoft Store](https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=neutral&gl=DE&ocid=pdpshare) and restart your PC
- Ubuntu: Install from your terminal: `sudo apt-get update` and `sudo apt-get install python3`
- MacOS: Install via Homebrew in your terminal: `brew install python@3.13`. If you don't have homebrew yet, install it by running `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` in your terminal and then try to install python again

# 2. Run Python in terminal

**First open a terminal**
- Windows:  Hit [Win] key or click on the Windows button on your taskbar to open the search field. Then type “terminal” and hit [Enter]
- Ubuntu: Press [Strg] + [Alt] + [T] to open a terminal.
- MacOS: Press [Cmd] + [Space] to open Spotlight, Then, type “terminal” and hit [Enter].

**Second, launch Python from the terminal:**

Inside the terminal, type “python3” and hit [Enter]. Voila!

# 3. Your very first Python program

It is an absolute necessity that your very first Python program MUST(!) be printing out the
text “Hello World”, as this is the standard first program in every (EVERY!) tutorial. Therefore,
it would be highly inadequate to start with something else. To achieve this, simply type

``` python
print(“hello world”)
```

and see what happens! Amazing!

Type `quit()` to exit Python.

During this robotics project, you will merely get a very short sneak peak on how to use
Python for controlling Dynamixel motors. In future semesters, you will get a more in-depth
introduction into how to program sophisticated scripts.

# 4. Install Visual Studio Code

Coding long and complex Python scripts within the terminal is cumbersome. This is better
done in an Integrated Development Environment (IDE). We would recommend an IDE called
Visual Studio Code. But of course, you can also use other IDEs, if you like. Download link:
https://code.visualstudio.com

With an IDE, you write code into a file. For Python code, this file needs to end with the suffix
“.py”.

Now reimplement your “hello world” script from above inside the IDE and save this code as a
file that you call “my_first_program.py” in your home directory.

# 5. Run Python scripts from the terminal

With an IDE (e.g. Visual Studio Code), you can write code and save it in a file. But how do
you execute this code? For this, we need the terminal, again.

Open the terminal, as described above. When you use the terminal, you always are inside
some directory (similarly to how you are inside some directory when you use the file
browser). When you open the terminal, you are automatically inside your home directory.
This is good, because this is the location where you saved your my_first_program.py file.
Now run the Python code from my_first_program.py by simply typing

``` shell
python3 my_first_program.py
```

and see what happens! Amazing!

# 6. Make your life easy - use other people’s code!

**We want to communicate with the Dynamixel motors.**

However, we do not want to create the code for this ourselves (because, this would take a
while)! Luckily, someone else has already implemented this for us. We just need to use it.
But before we can use other people’s code, we need to download it.

**What is Github?**

Code that is publically available is oftentimes published on Github - a platform that allows
users to share code and to collaborate. The underlying software used by Github is called Git,
a revisioning program. For this Robotics Project, you do not need to know how to use Git!
However, we highly recommend that you learn it.

**What is Gitlab?**

Many companies, research institutes, and universities have their own version of Github,
called Gitlab, to share code amongst their colleagues and students.

**What do we need to download for the Robotics Project?**

For this Robotics Project, you need to download code from Github that has been created by
Robotis (the company behind the Dynamixel motors), and from Gitlab that has been created
by members of the SIRo Lab from HRBO at BHT (i.e., Steffen). The code from Robotis
on Github provides general functionalities for communication with all kinds of Dynamixel
motors in all possible ways. And my code on Gitlab makes it stupidly simple to communicate
with the XL-330 motors which you are going to use during this course.

# 7. Prepare the Workspace

Let’s get your project environment up and running.

## Download the Workspace

Start by downloading the preconfigured workspace from this GitLab repository:

https://gitlab.bht-berlin.de/tore5980/ropro_setup

Click the **“Download”** button located just to the left of the blue **“Clone”** button.  
Download the code as a `.zip` file, extract it, and place the resulting folder wherever you like.

This workspace includes a ready-to-use project structure and some helpful utilities.

## Download External Code

Next, we need to add a few external packages to the workspace.

All of the following should be placed inside the `src` folder within the `ropro_setup` directory.

### 1. Download the DynamixelSDK

Grab the official DynamixelSDK from Robotis' GitHub:

https://github.com/ROBOTIS-GIT/DynamixelSDK

Click the green **“Code”** button on the right, then select **“Download ZIP”**.  
Extract the contents and place the folder inside the `src` directory.

### 2. Download `dynamixel-port` and `linear-interpolation`

Now download Steffen's repositories from the BHT GitLab:

- https://gitlab.bht-berlin.de/siro/teaching/dynamixel-port  
- https://gitlab.bht-berlin.de/siro/teaching/linear-interpolation

As before, click the **“Download”** button next to the **“Clone”** button, download each as a `.zip` file, extract, and place them into the `src` directory.

### 3. Rename the Folders

Make sure the folder names are clean. Remove any `-main` suffixes or other clutter.  
In the end, your `src` folder should contain:

- `DynamixelSDK`
- `dynamixel-port`
- `linear-interpolation`

## Open the Workspace in VS Code

Open VS Code and go to `File -> Open Folder`.  
Select the `ropro_setup` folder you downloaded earlier.

## Run the Installation Script

In VS Code, open a new terminal via `Terminal -> New Terminal`, then run:

```bash
python3 bootstrap.py
```

This script installs all necessary requirements and sets up a virtual environment for the project.

## Activate the Python Environment

To use the virtual environment, do the following:

1.	Press Ctrl+Shift+P (or Cmd+Shift+P on Mac) to open the Command Palette (Or click in `View -> Command Palette`).
2.	Type `Python: Select Interpreter` and select it.
3.	Choose the recommended interpreter (should point to .venv/bin/python).

Now, close the terminal by clicking the trash icon and open a new one. From now on, all commands will run inside the virtual environment.

## Test the Setup

Let’s confirm everything is working. Run the following in your terminal:

```shell
python3 test_dynamixel_port.py
```

If everything is set up correctly, you should see:

```shell
Test successful
```