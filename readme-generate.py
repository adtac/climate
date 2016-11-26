#!/usr/bin/env python

with open("climate") as file:
    lines = file.readlines()

print("# climate\n")
print("The ultimate command line tool for Linux!\n")

print("![image](https://i.imgur.com/tJudq4U.gif)\n")

print("**climate** provides a huge number of command line options "
      "for developers to automate their Linux system.\n")

print("""
## Installation

Using `curl`:

```bash
$ bash -c "$(curl -fsSL https://raw.githubusercontent.com/adtac/climate/master/install)"
```

Using `wget`:

```bash
$ bash -c "$(wget https://raw.githubusercontent.com/adtac/climate/master/install -O -)"
```

And that's it! It should automatically look for dependencies and install them.
After that's done, run `climate` to see the whole list of commands supported.

""")

print("""
## Requirements

`climate` has the following dependencies:

```
upower wget curl rar unzip 7z xdg-open dig git python pip node npm ruby gem fdupes glances speedtest sensors sshfs http-server is-up
```

The installation command should automatically install these for `apt`-based systems
and `yum`-based systems (and of course, `dnf`). For others, please install them manually.

""")

# commands
print("""
## Commands
""")
begun = False
print("**Meta**:\n")
print("Command | Description")
print("--- | ---")
for line in lines:
    line = line.strip()
    if begun and line.startswith("printf "):
        split = line.split("${PLAIN_BOLD}")
        if len(split) > 1:
            section = split[1].split(":")[0]
            print("\n\n**" + section + "**:\n")
            print("Command | Description")
            print("--- | ---")
    if begun and line.startswith("# ---"):
        break
    if line.startswith("shelp"):
        line = line.split('"')
        if len(line) > 2:
            begun = True
            command = " `climate " + line[1] + "`"
            helptext = line[3]
            print(command + " | " + helptext)
