#!/bin/bash

# opens jupyter notebook in the jupyter directory
function jupen() {
cd ~/jupyter
jupyter notebook
}

# enable youtube for a number of minutes
function wake_youtube() {
sudo python3.6 ~/.custom_commands/custom_python_commands/wake_youtube.py $1 

}


function sleeptime() {
command="sleep $1; echo bla; pm-suspend"
sudo bash -c $command

}

function translate_keyboard() {
highlighted_text=$(xclip -o -selection primary);
translated=$(python3.6 ~/.custom_commands/custom_python_commands/translate_keyboard.py "$highlighted_text");
xdotool type "$translated";
}

function saybla() {
spd-say bla
}

