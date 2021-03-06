freebsd-builder-rpi
===================

This tool guides you through the creation of an image of FreeBSD suitable for a Raspberry Pi. Most of the final script has been taken from Oleksandr Tymoshenko (http://kernelnomicon.org/?p=275), and he also made the u-boot distribution (that is included in this git repo under the directory firmware/) to allow FreeBSD to boot on an RPi. Thanks to him. The others files in the firmware folder comes from the Raspberry Pi Foundation github repo.

It has been made to be user friendly, providing an optional Curses GUI, and checks the configuration to search for errors (work in progress). Not a lot of options are implemented yet, but I am working on it. Another alternative is the crochet-freebsd project (https://github.com/kientzle/crochet-freebsd) which supports many features. (and many boards, not only RPi)

What you need:
A FreeBSD operating system, with python3 and the curses library installed.

How to use:<br/>
You have to run the program from the root directory of the project folder.

Either run the tool ./freebsd_builder_rpi without any options, and it will fire up the curses GUI to help you configure your custom image, and create a bash script that you will need to execute (as a root) so it builds FreeBSD. This also saves your configuration so you can provide it next time to modify it through the GUI.<br/>

It is also possible not to use the GUI, to do so just start the program with the -n option. In this case, you need to provide a premade configuration file with the -c FILE option. Same as before it will create a bash script based on the provided FILE.<br/>
