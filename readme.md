# wifi_monitor
Collect Statistics of all WiFi traffic on a Raspberry Pi.

Step 1: 
    Start with a fresh image of raspian. 
    Complete setup upon switching on.
    
Step 2: Do any updates. Be sure to reboot in case it upgrades kernel.

    sudo apt-get update
    sudo apt-get upgrade
    sudo reboot

Step 3: Install Nexmon WiFi Driver for monitor mode.

    git clone https://github.com/jakejones/wifi_monitor.git
    cd wifi_monitor
    sudo su root
    chmod 777 mon_install.sh
    ./mon_install.sh

Step 4: Add the following configuration code to /etc/rc.local before the exit 0 line

    iw phy `iw dev wlan0 info | gawk '/wiphy/ {printf "phy" $2}'` interface add mon0 type monitor
    ifconfig mon0 up

Step 5: Reboot

    sudo apt-get install python-pip
    sudo pip install 
    sudo reboot


###Example Usage:


