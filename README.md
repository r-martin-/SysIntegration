# systemIntegration

This is a custom shell which is developed using Python. It has very limited funicationally with a few linux commands built 
in that can be executed by the user.

When the user logs into the their profile on the system the shell runs once the user is logged in successfullly. 

There is a menu that can be accessed by the user showing the list of commands available -- help

If another user on the system wants to use this shell this command needs to be run

To make the custom shell executable for a user when they login do the following:
---------------------------------------------------------------------------------
cd /usr/bin
The .py file which is your shell should go in this directory
add  #!usr/bin/python to the first line of the .py file
chmod a+x .py file to make it executable
sudo chsh -s /usr/bin/ pShell.py *users name goes here*
Next time the user logs in this shell will run

---------------------------------------------------------------------------------

