# Climate

![image](https://i.imgur.com/Ma1UIe7.png)

**Climate** is the ultimate command line tool for Linux. It
provides a huge number of command line options for developers to
automate their Linux system. This tool can be extremely helpful to
learn various unix commands too. There is an option to print each
command before they're executed to help you memorize them over time.



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



## Requirements

`climate` has the following dependencies:

```
upower wget curl rar unzip 7z dig git python pip node npm fdupes glances speedtest sensors sshfs http-server httpstat is-up
```

The installation command should automatically install these for `apt`-based systems
and `yum`-based systems (and of course, `dnf`). For others, please install them manually.



## Commands

Command | Description
--- | ---
 `climate help` | show this help and exit
 `climate update` | update your climate install
 `climate uninstall` | uninstall your climate install :(
 `climate version` | display the version and credits
 <br> | 
 `climate weather [location]` | get the weather
 <br> | 
 `climate battery` | display remaining battery
 `climate sleep` | put computer to sleep
 `climate lock` | lock computer
 `climate shutdown [minutes]` | shutdown the computer
 `climate restart` | restart the computer
 `climate time` | show the time
 `climate clock [remove]` | put a console clock in the top right corner
 `climate countdown <seconds>` | a countdown timer
 `climate stopwatch` | a stopwatch
 `climate ix` | pipe output to ix.io
 <br> | 
 `climate biggest-files [path]` | find the biggest files recursively
 `climate biggest-dirs [path]` | find the biggest directories
 `climate dir-size [path]` | find directory size
 `climate remove-empty-dirs [path]` | remove empty directories
 `climate extract <file> [path]` | extract any given archive
 `climate search <text> [ext]` | search for the given pattern recursively
 `climate find-duplicates [path]` | report duplicate files in a directory
 `climate count <file> <string>` | count the number of occurences
 `climate replace <text> <replacement> [ext]` | replace all occurences
 `climate monitor <file>` | monitor file for changes
 `climate ramfs <size> <path>` | create a ramfs of size (in MB) at path
 <br> | 
 `climate speedtest` | test your network speed
 `climate local-ip` | retrieve your local ip address
 `climate is-online` | verify if you're online
 `climate public-ip` | retrieve your public ip address
 `climate ports` | list open ports
 `climate hosts` | edit the hosts file
 `climate http-server [port]` | http-server serving the current directory
 `climate is-up <domain>` | determine if server is up
 `climate httpstat <url>` | visualizes curl statistics with httpstat
 <br> | 
 `climate download-file <file>` | download file from server
 `climate download-dir <dir>` | download dir from server
 `climate upload <path> <remote-path>` | upload to server
 `climate ssh-mount <remote-path>` | mount a remote path
 `climate ssh-unmount <local-path>` | unmount a ssh mount
 <br> | 
 `climate undo-commit` | undo the latest commit
 `climate reset-local` | reset local repo to match remote
 `climate pull-latest` | sync local with remote
 `climate list-branches` | list all branches
 `climate repo-size` | calculate the repo size
 `climate user-stats <name>` | calculate total contribution for a user
 <br> | 
 `climate overview` | display an performance overview
 `climate memory` | find memory used
 `climate disk` | find disk used
 `climate get-pids <process>` | get all PIDs for a process name
 `climate trash-size` | find the trash size
 `climate empty-trash` | empty the trash


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


