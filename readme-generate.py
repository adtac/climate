#!/usr/bin/env python

with open("climate") as file:
    lines = file.readlines()

print("# Climate\n")

print("![image](https://i.imgur.com/Vgca4yS.png)\n")

print("""**Climate** is the ultimate command line tool for Linux. It
provides a huge number of command line options for developers to
automate their Linux system. This tool can be extremely helpful to
learn various unix commands too. There is an option to print each
command before they're executed to help you memorize them over time.

""")

print("""
## Installation

Clone the repository and run the `install` command:

```bash
$ git clone https://github.com/adtac/climate.git
$ cd climate
$ sudo ./install
```

The default location is `/usr/local/bin/`. If you want to write to a
different location, you can give an argument to the install command.

```bash
$ ./install [location]
```

You can also install using `curl` (although note that this
[might be insecure](https://www.seancassidy.me/dont-pipe-to-your-shell.html))

```bash
$ bash -c "$(curl -fsSL https://raw.githubusercontent.com/adtac/climate/master/install)"
```

Using `wget`:

```bash
$ bash -c "$(wget https://raw.githubusercontent.com/adtac/climate/master/install -q -O -)"
```

And that's it! It should automatically look for dependencies and install them.
After that's done, run `climate` to see the whole list of commands supported.

""")

print("""
## Requirements

`climate` has the following dependencies:

```
upower wget curl rar unzip 7z dig git python pip node npm fdupes glances speedtest sensors sshfs http-server httpstat is-up
```

The installation command should automatically install these for `apt`-based systems
and `yum`-based systems (and of course, `dnf`). For others, please install them manually.

""")

# commands
print("""
## Commands
""")
begun = False
print("Command | Description")
print("--- | ---")
for line in lines:
    line = line.strip()
    if begun and line.startswith("printf "):
        split = line.split("${PLAIN_BOLD}")
        if len(split) > 1:
            section = split[1].split(":")[0]
            print(" <br> | ")
    if begun and line.startswith("# ---"):
        break
    if line.startswith("shelp"):
        line = line.split('"')
        if len(line) > 2:
            begun = True
            command = " `climate " + line[1] + "`"
            helptext = line[3]
            print(command + " | " + helptext)

print("""\n
## License

```
    Climate - command line tools for Linux developers
    Copyright (C) 2016  Adhityaa Chandrasekar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

See the [LICENSE](LICENSE) file for more details.

""")
