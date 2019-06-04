#!/bin/bash

# opens jupyter notebook in its directory
function jupen() {
cd ~/jupyter
jupyter notebook
}

# enable youtube for a number of minutes
function wake_youtube() {
sudo python3.6 .custom_python_commands/wake_youtube.py $1 

}
