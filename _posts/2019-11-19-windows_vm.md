---
layout: post
title:  "Setting up a Windows 10 VM for reversing"
date:   2019-02-03
categories: Blog
---
**I AM A NEWBIE AND I AM WILLING TO LEARN.**

Now you can keep reading :3

As I'm diving into reversing, I want to setup my own Virtual Machine (VM) with some tools that I found very useful while working in the field of computer security.
I'm expanding my research since my last paper: we successfully landed an *adversarial machine learning attack* against a Deep Neural malware detector (and it was rather easy to achieve...), that focused on static features.
Full description and details on the paper (just click here: [https://arxiv.org/abs/1901.03583](https://arxiv.org/abs/1901.03583))!
Now, I also want to consider the messy dynamic world of executable programs, so I need to setup an environment on the fly to test and analyze samples.
The goal is to create a Windows VM to run inside my host OS, which is a simple Ubuntu 18.10.

**Spoiler**: there are so many blog posts regarding how to setup a VM for malware analysis.
I'm a student who loves to try new things, this guide is just a recap of my experience.
If you need something more detailed or professional, you can visit the [OA Labs](https://oalabs.openanalysis) and their amazing tutorials.
In particular, they wrote a guide on this very same topic [here](https://oalabs.openanalysis.net/2018/07/16/oalabs_malware_analysis_virtual_machine/).

# Obtaining Windows 10 (legally)

Microsoft is kind enough to provide the .iso of their operating systems (I downloaded the [Windows 10 disk](https://www.microsoft.com/en-us/software-download/windows10ISO)).
If you're lazy and you don't want to setup the whole VM by yourself, you can download some VMs ready to be used inside the virtualization software you prefer.
Details [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).

![Alala helloworld](/assets/2019-11-19-windows_vm/alala.png)

# Chocolatey as there were no tomorrow

First of all, let me say that I love [Chocolatey](https://chocolatey.org/), since you can install everything (or almost everything) from the command line (which is not usually the best option under Windows...).
You can invoke this package manager using PowerShell at no costs (in a Unix-like fashion).
There are others, that I do not know, but this  [Microsoft dev-blog post](https://devblogs.microsoft.com/scripting/weekend-scripter-powershell-and-chocolatey/) covers the argument. 
To install Chocolatey, just follow [the instructions here](https://chocolatey.org/docs/installation).

# Windows applications
Before speaking of the reversing tools, I would like to setup my VM with the applications that I love using under Windows.

## Cmder
First of all, I'm not a big fan of the standard *cmd* or *PowerShell*.
Let's install [cmder](https://cmder.net/), which is one of my favourite terminal emulator under Windows.
The other one is [Hyper](https://hyper.is/), but it is too minimal.
To install cmder, just type 
```
choco install cmder
```
inside your cmd window, wait for the conclusion and then launch it using ```cmder``` (and then, you can say goodbye to that scarce cmd forever!)

## Firefox
No need to explain why.

## Visual Studio Code
When it comes the hard work of scripting some stuff, [Visual Studio Code](https://code.visualstudio.com/) IS MY BEST COMPANION. 
I spent years using Atom, Brackets, Sublime Text... but then everything felt right using VSCode.
Tons of extensions, super fluid, fast.
Of course, it is not an IDE like [PyCharm](https://www.jetbrains.com/pycharm/) (that is a must when you need to work on big projects in Python...)

## Python
I will surely need to script something in Python, create environments, do not mess with packages... so [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is what I'm looking for.
Reliable, small, stable.

**WARNING**: if you want to use *cmder*, remember to add *conda* as task! Have a look here for [a simple guide](https://stackoverflow.com/questions/54959918/anaconda-python-cmder-integration-on-windows-10).

# Reversing tools

## PE Bear
When you need to have a first view of the binary file you're reversing, [PE Bear](https://hshrzd.wordpress.com/pe-bear/) is literally one of the first things you might use.
Just ```choco install pebear``` and you're done!
Launch this amazing tool by typing ``pe-bear`` on the command line.

## x64dbg
This is a disassembler / debugger for Windows binaries.
It can be expanded with many many plugins.
You can find it [here](C:\ProgramData\chocolatey\lib\x64dbg.portable\tools) or installing it using 
```
choco install x64dbg.portable
```
and launching it with ``x96dbg``.

## Ghidra
I really like [Ghidra](https://ghidra-sre.org/), even if it is not mature as IDA.
It is open-source, it has a nice decompiler, while it lacks a debugger.
As its bigger/older sister, it has a support for plugins.

# Conclusions
This settings is really scarce, but at least I think it is the minimal amount of programs that someone can use to start having fun with binaries.
... and I will have fun with them, indeed :)

![it is done!](/assets/2019-11-19-windows_vm/vmready.png)

*See you next blog post!*