# climate

The ultimate command line tool for Linux!

![image](https://i.imgur.com/tJudq4U.gif)

**climate** provides a huge number of command line options for developers to automate their Linux system.


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



## Requirements

`climate` has the following dependencies:

```
upower wget curl rar unzip 7z xdg-open dig git python pip node npm ruby gem fdupes glances speedtest sensors sshfs http-server is-up
```

The installation command should automatically install these for `apt`-based systems
and `yum`-based systems (and of course, `dnf`). For others, please install them manually.



## Commands

**Meta**:

Command | Description
--- | ---
 `climate help` | show this help and exit
 `climate update` | update your climate install
 `climate uninstall` | uninstall your climate install :(
 `climate version` | display the version and credits


**Info**:

Command | Description
--- | ---
 `climate weather [location]` | get the weather


**General**:

Command | Description
--- | ---
 `climate battery` | display remaining battery
 `climate sleep` | put computer to sleep
 `climate lock` | lock computer
 `climate shutdown [minutes]` | shutdown the computer
 `climate restart` | restart the computer
 `climate time` | show the time
 `climate clock` | put a console clock in the top right corner
 `climate countdown <seconds>` | a countdown timer
 `climate stopwatch` | a stopwatch
 `climate ix` | pipe output to ix.io


**Files**:

Command | Description
--- | ---
 `climate biggest-files [path]` | find the biggest files recursively
 `climate biggest-dirs [path]` | find the biggest directories
 `climate dir-size [path]` | find directory size
 `climate remove-empty-dirs [path]` | remove empty directories
 `climate extract <file> [path]` | extract any given archive
 `climate grep <text> [ext]` | search for the given pattern recursively
 `climate find-duplicates [path]` | report duplicate files in a directory
 `climate count <file> <string>` | count the number of occurences
 `climate replace <text> <replacement> [ext]` | replace all occurences
 `climate monitor <file>` | monitor file for changes
 `climate ramfs <size> <path>` | create a ramfs of size (in MB) at path


**Network**:

Command | Description
--- | ---
 `climate speedtest` | test your network speed
 `climate local-ip` | retrieve your local ip address
 `climate is-online` | verify if you're online
 `climate public-ip` | retrieve your public ip address
 `climate ports` | list open ports
 `climate hosts` | edit the hosts file
 `climate http-server [port]` | http-server serving the current directory
 `climate is-up <domain>` | determine if server is up


**SSH**:

Command | Description
--- | ---
 `climate download-file <file>` | download file from server
 `climate download-dir <dir>` | download dir from server
 `climate upload <path> <remote-path>` | upload to server
 `climate ssh-mount <remote-path>` | mount a remote path
 `climate ssh-unmount <local-path>` | unmount a ssh mount


**git**:

Command | Description
--- | ---
 `climate undo-commit` | undo the latest commit
 `climate reset-local` | reset local repo to match remote
 `climate pull-latest` | sync local with remote
 `climate list-branches` | list all branches
 `climate repo-size` | calculate the repo size
 `climate user-stats <name>` | calculate total contribution for a user


**Performance**:

Command | Description
--- | ---
 `climate overview` | display an performance overview
 `climate memory` | find memory used
 `climate disk` | find disk used
 `climate get-pids <process>` | get all PIDs for a process name
 `climate trash-size` | find the trash size
 `climate empty-trash` | empty the trash
