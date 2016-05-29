---
layout: post
title: Dualbooting Elementary on a Mac + getting wireless internet without an ethernet port
---

Elementary OS is a clean and lightweight Linux operating system. If you have a Mac and want to use this alongside your native OS (e.g. Lion, Mountain Lion, Maverick), here's a detailed tutorial for you! 

##### Materials
You will need:

* An empty USB or CD with sufficient space

* At least 10GB of space on your harddrive

##### Dualbooting
First, install rEFInd, a boot manager for computers. This allows you to choose between operating systems (in this case, Mac/Linux) when you start up. Download it from [here](http://sourceforge.net/projects/refind/files/0.8.1/refind-bin-0.8.1.zip/download) and unzip it by double-clicking on it. Install it by navigating into the unzipped folder on Terminal (Mac) and running `./install.sh`. Alternatively, to install, [/u/IO4](http://www.reddit.com/user/IO4) on reddit says: "simply drag and drop the install.sh into a terminal window in OSX".

Next, you need to partition your hard drive. You need a decent amount of space, I would suggest at least 10GB. You can check how much space you have by going to  -> About this Mac. Click ‘more info’, then click the ‘storage’ tab. Delete some unneeded files if you don't have much space. 

Now, open Disk Utility. Click the top-most item in the list. It should look something like this (this is after I partitioned it):

![Disk Utility](http://i.imgur.com/qlYcQCm.png)

Now, click the ‘partition’ tab. Click the + sign at the bottom left of the section, and make the format 'free space'. Enter how much space you want for Elementary in 'size' - I chose 12GB. If anything goes wrong, it can probably be fixed by going to the First Aid tab and clicking ‘repair disk’ at the bottom right. 

Next, install the iso off [the website](http://elementaryos.org/). You should be using 64 bit on new macs, so download that and go make some tea while it downloads. Now, plug in your USB. On Terminal (Mac), change the iso to an img using `hdiutil convert /path/to/elementary.iso -format UDRW -o /path/to/target.img` Obviously, replace /path/to/ubuntu.iso with something like ~/Downloads/elementaryos-stable-amd64.20130810.iso and /path/to/target.img with something like ~/Downloads/elementaryos.img 

Now, burn it to the USB by following steps 5-11 [here](https://help.ubuntu.com/community/How%20to%20install%20Ubuntu%20on%20MacBook%20using%20USB%20Stick#Manual_Approach).

Now shut down, and plug in the USB again. Turn the computer back on and you might see rEFInd. If it just takes you to your desktop, then restart and it should come up this time.

Use the arrows to navigate to the USB disk which should be the yellow disk with a USB symbol (mine said ‘Windows’ for some reason) and hit enter. Once it loads, it should ask you whether you want to try or install. Click install.

Then it will give you some options, whether you want to erase, add, or install alongside. DO NOT ERASE unless you want to lose all your existing files. I chose 'install alongside existing OS', which seemed easiest. There you have it. You have dual-booted Elementary, and can do anything offline that you want, or use wired internet using an ethernet cable. 

#### Getting wireless internet while OFFLINE (for Macs without an ethernet port) 

If you want wi-fi, though, you need to install firmware. As the Macbook Pro Retina does not have an ethernet port (among other newer Macs), there are a few extra steps to take to install it OFFLINE. First, staying in eOS, navigate to the Terminal (Linux) and type in `lspci -vvnn | grep 14e4`. This will tell you what broadcom chip you have. It will say something like `Broadcom Corporation BCM4311`. Write down the chip ID code, which will take the form of BCMXXXX e.g. BCM4311 as mine was. 

Lastly, do `uname -r` and write down the number you get. 

Restart and boot into your native OS (e.g. Lion, Maverick). 

##### Downloading b43-fwcutter
Use [this document](https://help.ubuntu.com/community/WifiDocs/Driver/bcm43xx#Drivers_available_in_Ubuntu) to see which instructions you need to follow, looking for which chip ID you had (e.g. BCM4311). If it says b43, go [here](https://launchpad.net/ubuntu/+source/b43-fwcutter) Pick one of the releases and download one of the .deb files under ‘Package files’ that pertains to your computer. For new macs it should be `b43-fwcutter_[something]_amd64.deb`. Download this file and copy this file to a USB - you don’t have to but it makes things easier. This downloads a utility for extracting firmware which you will later install.

##### Downloading b43 firmware
You also have to download the firmware. Go [here](http://wireless.kernel.org/en/users/Drivers/b43#Other_distributions_not_mentioned_above) If the number you had from `uname -r` was 3.2 or higher, navigate to “If you are using the b43 driver from 3.2 kernel or newer”. Download [this](http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2), and copy it to a USB too.

##### Putting it all together
Now restart and boot into eOS. Move the files off the USB and into your main home folder or somewhere accessible. 

First, go to Terminal (Linux) and change your directory to the b43-fwcutter folder. Then type this to install the utility: `sudo dpkg -i b43-fwcutter*`

If you didn’t get the right b43-fwcutter for you, eOS should alert you in ‘software updater’ and make you uninstall it. 

Now, use this Terminal (Linux) command to extract and install the firmware using the recently-installed b43-fwcutter utility. Make sure you replace `broadcom-wl-5.100.138.tar.bz2` with the exact file name of the firmware you installed in ‘Downloading b43 firmware’, if it is different: 

`tar xfvj broadcom-wl-5.100.138.tar.bz2`

`sudo b43-fwcutter -w /lib/firmware broadcom-wl-5.100.138/linux/wl_apsta.o`

Let it run, then restart. When you boot into eOS, finally it should let you choose a wireless network. You’re done! You can now use eOS with wireless internet.