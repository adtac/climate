#!/usr/bin/env python

with open("climate") as file:
    lines = file.readlines()

print("# climate\n")
print("The ultimate command line tool for Linux!\n")

print("![image](https://i.imgur.com/Ma1UIe7.png)\n")

print("""**climate** provides a huge number of command line options
for developers to automate their Linux system. Check out the Commands
section below to see the whole list of available commands.

This tool can be extremely helpful to learn various unix commands too.
There is an option to print each each command before they're executed to
help you memorize them over time.

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
upower wget curl rar unzip 7z dig git python pip node npm fdupes glances speedtest sensors sshfs http-server is-up
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

print("""\n
## License

Thanks to [guarinogabriel/Mac-CLI](https://github.com/guarinogabriel/Mac-CLI)
for the idea.

See the [LICENSE](LICENSE.md) file for license rights and limitations (AGPL).

""")
