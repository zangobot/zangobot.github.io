---
layout: post
title:  "The interesting PowerShell world"
date:   2019-11-20
categories: Blog
---

Since I was a "child", I spent my time digging inside the UNIX systems, learning the commands of the shell.
Today, after having set all the environment (see previous post), I decided to take a tour inside the world of **PowerShell scripting**.

If I should sum up PowerShell scripting in one line, I would say "a C#-like scripting language".
To let you grasp my enthusiasm, I just copy these commands:
```powershell
echo "Hello world!" > file.txt;
(Get-Content file.txt).Length
```
that correctly prints `12` on the PowerShell prompt.

You may notice two nice things:
* the presence of the `echo` and `>` commands (yeah, they ported some common UNIX shell commands to Windows);
* the output is not a string, but an object whose string representation is printed as a result.

The `Get-Content` is a so-called *cmdlet*, which is a command defined for the PowerShell environment.
They can be defined using methods from the *.NET framework* (that is kinda sexy if you have ever developed in .NET).
The behavior of this cmdlet is the same as the `cat` command under UNIX.
Just swap the two to see the result by yourself, as `cat` is just an alias for `Get-Content`.

# Basic scripting 

Let's have a look to this script.
```powershell
$flag = "flag{first_powershell_command};"
for($i=0; $i -lt $flag.Length; $i++){
    $flag[$i] -bxor 0x42
}
```
It is suddenly clear what it does, it is a simple *XOR encryption* with a one-byte-long key (which is `0x42`).
The string is contained inside the variable `$flag`, the `-bxor` function is the byte-level xor.
If you would have used the `-xor`, the result would have been Boolean (try to believe).

You can start learning PowerShell basics on the [official Microsoft reference](https://docs.microsoft.com/en-us/powershell/scripting/learn/understanding-important-powershell-concepts?view=powershell-6) or everywhere else on the internet.

# Messing up a bit

```powershell
$command = "";
$content = 79, 73, 66, 69, 10, 13, 98, 79, 70, 70, 69, 10, 93, 69, 88, 70, 78, 13;
;
foreach($c in $content){
    $command += [char]($c -bxor 42)
};
Invoke-Expression $command
```
While the encryption algorithm is the same, there is the `Invoke-Expression` cmdlet at the end, which dynamically execute the argument.
This means that, regardless of what we have stored inside `$command`, the PowerShell client will execute that expression.
In this simple case, the encoded command is 
```powershell
echo 'Hello world'
```
but of course, this can turn bad instantly.

# To sum up

This tiny blog-post was just a jump-start (for me) to have a glance of the powerful features of PowerShell.
I have to admit, I am impressed! There are so many things that could go wrong with a single script like this (in a security scenario, I mean...)

*See you next blog post!*