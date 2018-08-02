# wifi_monitor
Collect Statistics of all WiFi traffic on a Raspberry Pi 3B utilizing the Nexmon wifi driver.

Step 1: 
    Start with a fresh image of raspian. 
    Complete setup upon switching on. Be sure to set your timezone.
    
Step 2: Do any updates. Be sure to reboot in case it upgrades kernel.

    sudo apt-get update
    sudo apt-get upgrade
    sudo reboot

Step 3: Install Nexmon WiFi Driver for monitor mode.

    cd /home/pi
    git clone https://github.com/jakejones/wifi_monitor.git
    cd wifi_monitor
    sudo su root
    chmod 777 mon_install.sh
    ./mon_install.sh

Step 4: Add the following configuration code to /etc/rc.local before the 'exit 0' line

    iw phy `iw dev wlan0 info | gawk '/wiphy/ {printf "phy" $2}'` interface add mon0 type monitor
    ifconfig mon0 up

Step 5: Finally

    sudo apt-get install python-pip
    sudo pip install scapy datetime
    cd /home/pi/wifi_monitor
    sudo chmod +x monitor.py
    sudo chmod +x sort.py
    sudo chmod +x run.sh
    sudo reboot

Step 6: Create service that starts monitor on boot (Optional)

    cd /home/pi/wifi_monitor
    sudo cp wifi-monitor.service /etc/systemd/system/wifi-monitor.service
    sudo systemctl daemon-reload
    sudo systemctl enable wifi-monitor
    sudo reboot

To check on the status of the service run:
    sudo systemctl status wifi-monitor

You can find the data in "/home/pi/wifi_monitor/data/". It will be sorted by day and hour.



### Example 1:
In the terminal call the monitor.py script like the following:

    sudo ./monitor.py > output.log

For every packet detected this will save the MAC address alongside the time into the file output.log.

### Example 2:

    sudo ./monitor.py | ./sort.py "data" 

This will save the output in files under the directory "data" sorted by date and the hour of day. e.g.
    data/2018-08-02/14.log
Will contain all the mac addresses logged between 2:00pm and 3:00pm on the 2nd aug 2018.

The benefet of doing this is to speed up the time to query the data especially as the data set grows over time.
