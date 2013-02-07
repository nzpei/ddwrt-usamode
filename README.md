ddwrt-usamode
=============

USA Mode Web UI for DD-WRT Routers

ddwrt-usamode allows you to control whether you wish to pretend to be in the USA or not on a per-device basis.
This is achieved by adding custom routes for each client on the network that wishes to be routed down the VPN.
Of course, instead of pretending you're in the USA this could be used to toggle connectivity via any OpenVPN tunnel.

Author: Pei Huang
Date: 9/Jan/2013; Published to Github 7/Feb/2013

Prerequisites:
- Modern DD-WRT Router (i.e. BCM47XX chipset, such as Asus RT-N16) 
- DD-WRT version with OpenVPN
- Pre-configured VPN connection with StrongVPN or another provider - assumes tun device is "tun0" and that the tunnel is established on boot, set up and working on the router per the provider's instructions
- JFFS support on the router

Install Guide:
- Enable JFFS
- Ensure redirect-gateway is commented out of the OpenVPN config and persisted in NVRAM. 
- Copy the contents of this directory to /jffs/usa/
- Chmod the directories and contents to 755
- Add a line to the router startup to run /jffs/usa/startup.sh
- Reboot the router

(Optional):
- Add a static DNS entry into dnsmasq as follows: 
address=/usamode/192.168.1.1
 (substituting in your router's ip address. This allows users to browse to http://usamode./ to access the WebUI.

User Guide:
- User browses to http://usamode./ (or http://<router IP address>/) 
- Click on "Toggle" button to turn on/off USA mode
- Check you are on the right IP address by visiting http://www.whatismyip.com/ or similar.

Important Notes:
- Clicking "Toggle" should take effect immediately, but it's worth checking your IP address before browsing any geo-location filtered sites
- Your normal DD-WRT web interface will be run on port 81 instead of port 80
- Mode preferences will not persist after a router reboot

