#!/usr/bin/env bash

# ----------------------------------------------------------------------------
# Colors

if [[ $USE_COLORS == "false" ]]; then
    RED=""
    GREEN=""
    BLUE=""
    YELLOW=""
    PLAIN=""

    RED_BOLD=""
    GREEN_BOLD=""
    BLUE_BOLD=""
    YELLOW_BOLD=""
    PLAIN_BOLD=""
else
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    BLUE='\033[0;34m'
    YELLOW='\033[0;33m'
    PLAIN='\033[0m'

    RED_BOLD='\033[1;31m'
    GREEN_BOLD='\033[1;32m'
    BLUE_BOLD='\033[1;34m'
    YELLOW_BOLD='\033[1;33m'
    PLAIN_BOLD='\033[1;37m'
fi

# ----------------------------------------------------------------------------
# Utilities

trap ctrl_c INT
ctrl_c() {
    tput cnorm
    if [[ -z $(jobs -p) ]]; then
        kill $(jobs -p)
    fi
    exit
}

spinner() {
    spin="\\|/-"
    i=0
    tput civis
    while kill -0 $1 2>/dev/null; do
        i=$(( (i+1) %4 ))
        printf "\b${spin:$i:1}"
        printf "\b"
        sleep 0.07
    done
    tput cnorm
}

log() {
    if [[ $SHOW_COMMAND == "true" ]]; then
        printf "+ "
        echo "$@"
    fi
}

shelp() {
    COMMAND_SIZE=-40s
    HELP_SIZE=15s
    printf " ${BLUE}climate %${COMMAND_SIZE} ${PLAIN}%s\n" "${1}" "${2}"
}

extract () {
    if [[ -f $1 ]] ; then
        if [[ $2 == "" ]]; then
            case $1 in
                *.rar)                             rar x   $1       ${1%.rar}/        ;;
                *.tar.bz2)  mkdir -p ${1%.tar.bz2} && tar xjf $1 -C ${1%.tar.bz2}/ ;;
                *.tar.gz)   mkdir -p ${1%.tar.gz}  && tar xzf $1 -C ${1%.tar.gz}/  ;;
                *.tar.xz)   mkdir -p ${1%.tar.xz}  && tar xf  $1 -C ${1%.tar.xz}/  ;;
                *.tar)      mkdir -p ${1%.tar}     && tar xf  $1 -C ${1%.tar}/     ;;
                *.tbz2)     mkdir -p ${1%.tbz2}    && tar xjf $1 -C ${1%.tbz2}/    ;;
                *.tgz)      mkdir -p ${1%.tgz}     && tar xzf $1 -C ${1%.tgz}/     ;;
                *.zip)                             unzip   $1 -d ${1%.zip}/        ;;
                *.7z)                              7za e   $1 -o${1%.7z}/          ;;
                *)          printf "${RED}'$1' cannot be extracted.\n"             ;;
            esac
        else
            case $1 in
                *.rar)                     rar x   $1    $2 ;;
                *.tar.bz2)  mkdir -p $2 && tar xjf $1 -C $2 ;;
                *.tar.gz)   mkdir -p $2 && tar xzf $1 -C $2 ;;
                *.tar.xz)   mkdir -p $2 && tar xf  $1 -C $2 ;;
                *.tar)      mkdir -p $2 && tar xf  $1 -C $2 ;;
                *.tbz2)     mkdir -p $2 && tar xjf $1 -C $2 ;;
                *.tgz)      mkdir -p $2 && tar xzf $1 -C $2 ;;
                *.zip)                     unzip   $1 -d $2 ;;
                *.7z)                      7z  e   $1 -o$2/ ;;
                *)          printf "${RED}'$1' cannot be extracted.\n"             ;;
            esac
        fi
    else
        printf "${RED}'$1' does not exist.\n"
    fi
    printf "${PLAIN}"
}

replace() {
    find_this="$1"
    replace_with="$2"
    shift 2

    items=$(ag -l --nocolor "$find_this" "$@")
    temp="${TMPDIR:-/tmp}/climate_replace_temp.$$"
    IFS=$'\n'
    for item in $items; do
      sed "s/$find_this/$replace_with/g" "$item" > "$temp" && mv "$temp" "$item"
    done
}

ix() {
    local opts
    local OPTIND
    [[ -f "$HOME/.netrc" ]] && opts='-n'
    while getopts ":hd:i:n:" x; do
        case $x in
            h) echo "ix [-d ID] [-i ID] [-n N] [opts]"; return;;
            d) $echo curl $opts -X DELETE ix.io/$OPTARG; return;;
            i) opts="$opts -X PUT"; local id="$OPTARG";;
            n) opts="$opts -F read:1=$OPTARG";;
        esac
    done
    shift $(($OPTIND - 1))
    [[ -t 0 ]] && {
        local filename="$1"
        shift
        [[ "$filename" ]] && {
            curl $opts -F f:1=@"$filename" $* ix.io/$id
            return
        }
        echo "^C to cancel, ^D to send."
    }
    curl $opts -F f:1='<-' $* ix.io/$id
}

ipinfo() {
    external_ip="$1"
    result=$(curl --silent https://ipinfo.io/$external_ip)
    log "curl --silent https://ipinfo.io/$external_ip"
    
    if [[ $result == "Please provide a valid IP address" || -z $result ]]; then
        printf "${RED_BOLD}Please provide a valid IP address!\n"
        exit
    fi

    json_ip=$(echo "$result" | jq -r ".ip")
    json_hostname=$(echo "$result" | jq -r ".hostname")
    json_city=$(echo "$result" | jq -r ".city")
    json_region=$(echo "$result" | jq -r ".region")
    json_country=$(echo "$result" | jq -r ".country")
    json_loc=$(echo "$result" | jq -r ".loc")
    json_org=$(echo "$result" | jq -r ".org")
    json_postal=$(echo "$result" | jq -r ".postal")


    printf "${GREEN_BOLD}IP-Address: ${YELLOW}${json_ip}\n"
    printf "${GREEN_BOLD}Hostname: ${YELLOW}${json_hostname}\n"
    printf "${GREEN_BOLD}Network: ${YELLOW}${json_org}\n"
    printf "${GREEN_BOLD}City: ${YELLOW}${json_city}, ${json_region}, ${json_country}\n"
    printf "${GREEN_BOLD}Postal Code: ${YELLOW}${json_postal}\n"
    printf "${GREEN_BOLD}Latitude/Longitude: ${YELLOW}${json_loc}\n"
}

# ----------------------------------------------------------------------------
# Parse Args

command=$1
commandargs=$2
commandargs2=$3

TRASH_PATH="$HOME/.local/share/Trash"

help=$(
    printf "${RED_BOLD}"
    printf "┌────────────────────────────────────────┐\n"
    printf "│ "
    printf "${PLAIN_BOLD}"
    printf "climate - command line tools for Linux "
    printf "${RED_BOLD}"
    printf "│\n"
    printf "└────────────────────────────────────────┘\n"

    printf "${PLAIN_BOLD}Meta:\n"
    shelp "help" "show this help and exit"
    shelp "update" "update your climate install"
    shelp "uninstall" "uninstall climate :("
    shelp "version" "display the version and credits"

    printf "\n${PLAIN_BOLD}Info:\n"
    shelp "weather [location]" "get the weather"

    printf "\n${PLAIN_BOLD}General:\n"
    shelp "battery" "display remaining battery"
    shelp "sleep" "put computer to sleep"
    shelp "lock" "lock computer"
    shelp "shutdown [minutes]" "shutdown the computer"
    shelp "restart" "restart the computer"
    shelp "time" "show the time"
    shelp "clock [remove]" "put a console clock in the top right corner"
    shelp "countdown <seconds>" "a countdown timer"
    shelp "stopwatch" "a stopwatch"
    shelp "ix" "pipe output to ix.io"

    printf "\n${PLAIN_BOLD}Files:\n"
    shelp "biggest-files [path]" "find the biggest files recursively"
    shelp "biggest-dirs [path]" "find the biggest directories"
    shelp "dir-size [path]" "find directory size"
    shelp "remove-empty-dirs [path]" "remove empty directories"
    shelp "extract <file> [path]" "extract any given archive"
    shelp "search <text> [ext]" "search for the given pattern recursively"
    shelp "find-duplicates [path]" "report duplicate files in a directory"
    shelp "count <file> <string>" "count the number of occurences"
    shelp "replace <text> <replacement> [ext]" "replace all occurences"
    shelp "monitor <file>" "monitor file for changes"
    shelp "ramfs <size> <path>" "create a ramfs of size (in MB) at path"

    printf "\n${PLAIN_BOLD}Network:\n"
    shelp "speedtest" "test your network speed"
    shelp "local-ip" "retrieve your local ip address"
    shelp "is-online" "verify if you're online"
    shelp "public-ip" "retrieve your public ip address"
    shelp "ports" "list open ports"
    shelp "hosts" "edit the hosts file"
    shelp "http-server [port]" "http-server serving the current directory"
    shelp "is-up <domain>" "determine if server is up"
    shelp "httpstat <url>" "visualizes curl statistics with httpstat"
    shelp "ipinfo [ip]" "lookup IP with ipinfo.io API"

    printf "\n${PLAIN_BOLD}SSH:\n"
    shelp "download-file <file>" "download file from server"
    shelp "download-dir <dir>" "download dir from server"
    shelp "upload <path> <remote-path>" "upload to server"
    shelp "ssh-mount <remote-path>" "mount a remote path"
    shelp "ssh-unmount <local-path>" "unmount a ssh mount"

    printf "\n${PLAIN_BOLD}git:\n"
    shelp "undo-commit" "undo the latest commit"
    shelp "reset-local" "reset local repo to match remote"
    shelp "pull-latest" "sync local with remote"
    shelp "list-branches" "list all branches"
    shelp "repo-size" "calculate the repo size"
    shelp "user-stats <name>" "calculate total contribution for a user"

    printf "\n${PLAIN_BOLD}Performance:\n"
    shelp "overview" "display an performance overview"
    shelp "memory" "find memory used"
    shelp "disk" "find disk used"
    shelp "get-pids <process>" "get all PIDs for a process name"
    shelp "trash-size" "find the trash size"
    shelp "empty-trash" "empty the trash"

    printf "\n")

# ----------------------------------------------------------------------------
# Meta

if [[ $command == "help" || -z $command ]]; then
    printf "${help}\n"

# ----------------------------------------------------------------------------
# Update climate

elif [[ $command == "update" ]]; then
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/adtac/climate/master/install)"

# ----------------------------------------------------------------------------
# Uninstall climate

elif [[ $command == "uninstall" ]]; then
    sudo rm /usr/local/bin/climate -rf
    sudo rm /etc/bash_completion.d/climate_completion

    home=$(eval echo "~$(logname)")
    if [[ -f "$home/.bashrc" ]]; then
        mv $home/.bashrc $home/.oldbashrc
        grep -v "source /etc/bash_completion.d/climate_completion" $home/.oldbashrc > $home/.bashrc
        rm $home/.oldbashrc
    fi

    if [[ -f "$home/.zshrc" ]]; then
        mv $home/.zshrc $home/.oldzshrc
        grep -v "source /etc/bash_completion.d/climate_completion" $home/.oldzshrc  > $home/.zshrc
        rm $home/.oldzshrc
    fi

    printf "Uninstalling climate: "
    if [[ -f /usr/local/bin/climate ]] ; then
        printf "${RED_BOLD}Failed${PLAIN}"
    else
        printf "${GREEN_BOLD}Success${PLAIN}\n"
        printf "Sorry to see you go. If you faced any bugs, please file "
        printf "them at https://github.com/adtac/climate"
    fi
    printf "\n"

# ----------------------------------------------------------------------------
# Display version and credits

elif [[ $command == "version" ]]; then
    printf "${BLUE_BOLD}climate${PLAIN} v0.3\n\n"
    printf "${PLAIN}Copyright (C) 2016  Adhityaa Chandrasekar\n\n"
    printf "${PLAIN}This program is licensed under the GNU Affero General "
    printf "Public License.\nFor more details, refer to the LICENSE file "
    printf "that should have been\ndistributed along with this program.\n"

# ----------------------------------------------------------------------------
# Get the weather from wttr.in

elif [[ $command == "weather" ]]; then
    log 'curl -s wttr.in/$commandargs | head -n 7 && printf "\n"'
    curl -s wttr.in/$commandargs | head -n 7 && printf "\n" &
    spinner $!

# ----------------------------------------------------------------------------
# Display battery status

elif [[ $command == "battery" ]]; then
    PERCENTAGE=$(upower -i "$(upower -e | grep battery)" |
    awk -F: '/percentage/{gsub(/^\s+|[\s%]+$/, "", $2); print $2}')
    TIME_REMAINING=$(upower -i "$(upower -e | grep battery)" |
    awk -F: '/time to empty/{gsub(/^\s+|\s+$/, "", $2); print $2}')

    if [[ "$PERCENTAGE" -gt "30" ]]; then
        PERCENTAGE_COLOR=$GREEN_BOLD
    elif [[ "$PERCENTAGE" -gt "10" ]]; then
        PERCENTAGE_COLOR=$YELLOW_BOLD
    else
        PERCENTAGE_COLOR=$RED_BOLD
    fi

    printf "${PERCENTAGE_COLOR}${PERCENTAGE}%%${PLAIN} (${TIME_REMAINING} left)\n"

# ----------------------------------------------------------------------------
# Power options

elif [[ $command == "sleep" ]]; then
    log 'systemctl suspend'
    systemctl suspend

elif [[ $command == "lock" ]]; then
    log 'kxdg-screensaver lock'
    xdg-screensaver lock

elif [[ $command == "shutdown" ]]; then
    if [[ $commandargs == "" ]]; then
        log 'sudo shutdown -h now'
        sudo shutdown -h now
    else
        log 'sudo shutdown -h $commandargs'
        sudo shutdown -h $commandargs
    fi

elif [[ $command == "restart" ]]; then
    if [[ $commandargs == "" ]]; then
        log 'sudo reboot'
        sudo reboot
    else
        log 'sudo -- sh -c "sleep $commandargs; reboot"'
        sudo -- sh -c "sleep $commandargs; reboot"
    fi

# ----------------------------------------------------------------------------
# Time

elif [[ $command == "time" ]]; then
    DATE_TIME=$(date "+%l:%M %p, %A, %d %h %Y")
    printf "${PLAIN_BOLD}${DATE_TIME}${PLAIN}\n"

elif [[ $command == "clock" ]]; then
    if [[ $commandargs == "remove" ]]; then
        PARENT_SHELL=$(ps -p "$$" -o ppid=)
        if [[ -f "/tmp/clock.$PARENT_SHELL" ]]; then
            # kill the clock subshell
            kill -9 $(cat "/tmp/clock.$PARENT_SHELL") > /dev/null
            rm "/tmp/clock.$PARENT_SHELL"

            # clear out the clock
            DATE_STR=$(date)
            LENGTH=${#DATE_STR}
            tput sc
            tput cup 0 $(($(tput cols)-29))
            for i in $(seq 1 $LENGTH); do printf " "; done;
            tput rc
        fi
    else
        log 'while sleep 1;do tput sc;tput cup 0 $(($(tput cols)-29));date;tput rc;done'
        (while sleep 1; do
            tput sc
            tput cup 0 $(($(tput cols)-29))
            date
            tput rc
        done) &
        CLOCK_PID=$!
        PARENT_SHELL=$(ps -p "$$" -o ppid= | xargs)
        # write the PID of the clock to a file
        echo "$CLOCK_PID" > "/tmp/clock.$PARENT_SHELL"
    fi

elif [[ $command == "countdown" ]]; then
    now=$(date --utc +%s)
    date1=$(expr $now + $commandargs);
    tput civis
    while [[ "$date1" -ge $(date +%s) ]]; do
        now=$(date --utc +%s)
        echo -ne "$(date --utc --date @$(expr $date1 - $now) +%H:%M:%S)\r";
        sleep 1
    done
    tput cnorm

elif [[ $command == "stopwatch" ]]; then
    start_time=$(date --utc +%s)
    tput civis
    while true; do
        now=$(date --utc +%s)
        echo -ne "$(date -u --date @$(expr $now - $start_time) +%H:%M:%S)\r";
        sleep 1
    done
    tput cnorm

# ----------------------------------------------------------------------------
# ix.io

elif [[ $command == "ix" ]]; then
    ix

# ----------------------------------------------------------------------------
# Recursively find the biggest files in the given directory

elif [[ $command == "biggest-files" ]]; then
    if [[ $commandargs == "" ]]; then
        commandargs="."
    fi

    log 'find $commandargs -type f -print0 | xargs -0 du | sort -rn | head -n 10 | cut -f2 | xargs -I{} du -sh {}'
    find $commandargs -type f -print0 |
        xargs -0 du |
        sort -rn |
        head -n 10 |
        cut -f2 |
        xargs -I{} du -sh {} &
    spinner $!

# ----------------------------------------------------------------------------
# List the biggest directories in the given directory

elif [[ $command == "biggest-dirs" ]]; then
    if [[ $commandargs == "" ]]; then
        commandargs="."
    fi

    log 'find $commandargs -maxdepth 1 -type d -print0 | xargs -0 du --max-depth=1 | sort -rn | head -n 11 | tail -n +2 | cut -f2 | xargs -I{} du -sh {}'
    find $commandargs -maxdepth 1 -type d -print0 |
        xargs -0 du --max-depth=1 |
        sort -rn |
        head -n 11 |
        tail -n +2 |
        cut -f2 |
        xargs -I{} du -sh {} &
    spinner $!

# ----------------------------------------------------------------------------
# Get director size

elif [[ $command == "dir-size" ]]; then
    if [[ $commandargs == "" ]]; then
        commandargs="."
    fi

    log 'du -sh $commandargs | cut -f1'
    du -sh $commandargs | cut -f1 &
    spinner $!

# ----------------------------------------------------------------------------
# Remove empty directories

elif [[ $command == "remove-empty-dirs" ]]; then
    if [[ $commandargs == "" ]]; then
        commandargs="."
    fi

    log 'find $commandargs -maxdepth 1 -type d -empty | xargs rm -rf'
    find $commandargs -maxdepth 1 -type d -empty | xargs rm -rf

# ----------------------------------------------------------------------------
# count

elif [[ $command == "count" ]]; then
    if [[ $commandargs != "" && -f $commandargs ]]; then
        if [[ $commandargs2 != "" ]]; then
            printf "${PLAIN_BOLD}"
            log 'grep -c "$commandargs2" $commandargs | tr -d "\n"'
            grep -c "$commandargs2" $commandargs | tr -d '\n'
            printf "${PLAIN} occurences\n"
        fi
    fi

# ----------------------------------------------------------------------------
# Duplicates

elif [[ $command == "find-duplicates" ]]; then
    if [[ $commandargs == "" ]]; then
        commandargs="."
    fi

    log 'fdupes $commandargs'
    fdupes $commandargs &
    spinner $!

# ----------------------------------------------------------------------------
# Find and replace

elif [[ $command == "search" ]]; then
    if [[ $commandargs2 != ".*" && $commandargs2 != "" ]]; then
        commandargs2="."$commandargs2
    fi
    log 'find . -iname "*"$commandargs2 -type f | xargs grep -in --color "$commandargs"'
    find . -iname "*"$commandargs2 -type f | xargs grep -in --color "$commandargs"

elif [[ $command == "replace" ]]; then
    log 'replace $commandargs $commandargs2'
    replace $commandargs $commandargs2 &
    spinner $!

# ----------------------------------------------------------------------------
# Monitor file for changes

elif [[ $command == "monitor" ]]; then
    if [[ $commandargs != "" ]]; then
        log 'tail -f $commandargs'
        tail -f $commandargs
    fi

# ----------------------------------------------------------------------------
# RAMFS

elif [[ $command == "ramfs" ]]; then
    if [[ $commandargs != "" ]]; then
        if [[ $commandargs2 != "" ]]; then
            m="m"
            if [[ -d $commandargs2 ]]; then
                printf "${RED}Error: `${commandargs2}` already exists\n"
                printf "${PLAIN}Please remove it and try again.\n"
            else
                mkdir $commandargs2
                log 'sudo mount -t tmpfs tmpfs ./$commandargs2 -o size=$commandargs$m'
                sudo mount -t tmpfs tmpfs ./$commandargs2 -o size=$commandargs$m
            fi
        fi
    fi

# ----------------------------------------------------------------------------
# Extract the given archive independent of the type

elif [[ $command == "extract" ]]; then
    extract $commandargs $commandargs2

# ----------------------------------------------------------------------------
# Network utilities

elif [[ $command == "speedtest" ]]; then
    log 'speedtest --simple'
    speedtest --simple &
    spinner $!

elif [[ $command == "local-ip" ]]; then
    ifconfig | awk -v RS="\n\n" '{ for (i=1; i<=NF; i++) if ($i == "inet" && $(i+1) != "127.0.0.1" ) printf "%s\t%s\n", $1, $(i+1) }'

elif [[ $command == "is-online" ]]; then
    is-online

elif [[ $command == "public-ip" ]]; then
    dig +short myip.opendns.com @resolver1.opendns.com &
    spinner $!

elif [[ $command == "ports" ]]; then
    sudo lsof -iTCP -sTCP:LISTEN -P

elif [[ $command == "hosts" ]]; then
    sudo $EDITOR /etc/hosts

elif [[ $command == "http-server" ]]; then
    if [[ $commandargs == "" ]]; then
        http-server -a 0.0.0.0
    else
        http-server -a 0.0.0.0 -p $commandargs
    fi

elif [[ $command == "httpstat" ]]; then
    if [[ $commandargs != "" ]]; then
        httpstat "$commandargs"
    fi

elif [[ $command == "is-up" ]]; then
    if [[ $commandargs != "" ]]; then
        is-up "$commandargs"
    fi

elif [[ $command == "ipinfo" ]]; then
    ipinfo "$commandargs"

# ----------------------------------------------------------------------------
# SSH

elif [[ $command == "download-file" ]]; then
    if [[ $commandargs != "" ]]; then
        printf "username@server: "
        read server
        if [[ $server != "" ]]; then
            scp $server:$commandargs .
        fi
    fi

elif [[ $command == "download-dir" ]]; then
    if [[ $commandargs != "" ]]; then
        printf "username@server: "
        read server
        if [[ $server != "" ]]; then
            scp -r $server:$commandargs .
        fi
    fi

elif [[ $command == "upload" ]]; then
    if [[ $commandargs != "" ]]; then
        printf "username@server: "
        read server
        if [[ $server != "" ]]; then
            scp $commandargs $server:$commandargs2
        fi
    fi

elif [[ $command == "ssh-mount" ]]; then
    if [[ $commandargs != "" ]]; then
        printf "username@server: "
        read server
        if [[ $server != "" ]]; then
            dir=$(basename $commandargs)
            if [[ -d $dir ]]; then
                printf "${RED}Error: `${dir}` already exists\n"
                printf "${PLAIN}Please remove it and try again.\n"
            else
                mkdir $dir
                sshfs $server:$commandargs ./$dir
            fi
        fi
    fi

elif [[ $command == "ssh-unmount" ]]; then
    if [[ $commandargs != "" ]]; then
        fusermount -u ./$commandargs && rm ./$commandargs -rf
    fi

# ----------------------------------------------------------------------------
# git

elif [[ $command == "undo-commit" ]]; then
    git reset --soft HEAD~

elif [[ $command == "reset-local" ]]; then
    git fetch origin
    git reset --hard origin/master

elif [[ $command == "pull-latest" ]]; then
    git pull --rebase origin master

elif [[ $command == "list-branches" ]]; then
    git branch -a

elif [[ $command == "repo-size" ]]; then
    (
        git bundle create .tmp-git-bundle --all > /dev/null 2>&1
        du -sh .tmp-git-bundle | cut -f1
        rm .tmp-git-bundle) &
    spinner $!

elif [[ $command == "user-stats" ]]; then
    if [[ $command != "" ]]; then
        git log --author="$commandargs" --pretty=tformat: --numstat | gawk -v GREEN=$GREEN_BOLD -v PLAIN=$PLAIN -v RED=$RED_BOLD 'BEGIN { add = 0; subs = 0 } { add += $1; subs += $2 } END { printf "Total: %s+%s%s / %s-%s%s\n", GREEN, add, PLAIN, RED, subs, PLAIN }'
    fi

# ----------------------------------------------------------------------------
# Performance overview

elif [[ $command == "overview" ]]; then
    glances

# ----------------------------------------------------------------------------
# Memory usage

elif [[ $command == "memory" ]]; then
    AVAILABLE=$(cat /proc/meminfo | grep MemAvailable | awk '{printf "%d", $2}')
    TOTAL=$(cat /proc/meminfo | grep MemTotal | awk '{printf "%d", $2}')
    USED=$(expr $TOTAL - $AVAILABLE)
    USED_GB=$(echo $USED | awk '{printf "%.1fG", $1/1048576}')

    printf "${PLAIN_BOLD}${USED_GB}${PLAIN} / ${PLAIN_BOLD}"
    cat /proc/meminfo | grep MemTotal | awk '{printf "%.1fG", $2/1048576}'
    printf "${PLAIN} used\n"

# ----------------------------------------------------------------------------
# Disk usage

elif [[ $command == "disk" ]]; then
    df -H | grep 'da' | awk -v BOLD=$PLAIN_BOLD -v PLAIN=$PLAIN '{ printf "%s - %s%s%s / %s%s%s used\n", $1, BOLD, $3, PLAIN, BOLD, $2, PLAIN }'

# ----------------------------------------------------------------------------
# Obtain process PIDs

elif [[ $command == "get-pids" ]]; then
    if [[ $commandargs != "" ]]; then
        ps aux | grep $commandargs | cut -f2 -d' ' | grep -v -e '^$'
    fi

# ----------------------------------------------------------------------------
# Trash size

elif [[ $command == "trash-size" ]]; then
    if [[ -d ${TRASH_PATH} ]]; then
        printf "Trash size: ${PLAIN_BOLD}%s${PLAIN}\n" $(du -hs ${TRASH_PATH} | cut -f1) &
        spinner $!
    else
        printf "${RED_BOLD}Error: Unable to find trash size. Check if ${TRASH_PATH} exists.${PLAIN}\n"
    fi

# ----------------------------------------------------------------------------
# Empty trash

elif [[ $command == "empty-trash" ]]; then
    if [[ -d ${TRASH_PATH} ]]; then
        rm -rf ${TRASH_PATH}/* &
        spinner $!
    else
        printf "${RED_BOLD}Error: Unable to empty trash. Check if ${TRASH_PATH} exists.${PLAIN}\n"
    fi

# ----------------------------------------------------------------------------
# Welp, we don't know this command

elif [[ $command != "" ]]; then
    printf "${help}\n\n"
    printf "${RED_BOLD}Error: '${command}' command not available\n${PLAIN}"
fi
# ----------------------------------------------------------------------------
