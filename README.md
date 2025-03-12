# Dog Monitoring Camera 🐶📷

Ever wonder if your pup is sneaking onto the couch while you're away? This project uses a Wyze camera with an RTSP feed and some clever AI to catch couch-surfing canines in the act. Get alerts, track their mischief, and maybe even win the eternal battle of "No dogs on the couch!"

## Raspberry Pi

Connect from Macbook using `ssh raspberrypi.local` when it is booted up and online. Alternatively, its IP is `192.168.1.120` so you can ssh using `ssh pi@192.168.1.120`.

Password is `Cornell!32A`.

To get ssh working, had to select custom settings in Raspberry Pi Imager. Using SSID information, no account set up, then SSH key-gen. After flashing it to the SD, created a file called ssh in bootfs by running `touch /Volumes/bootfs/ssh`. Then, booting up the Pi with SD for a few minutes, `ssh pi@192.168.1.120` worked.

Can also access at <https://connect.raspberrypi.com/devices>.

Can access the GUI view by using RealVNC, IP `192.168.1.120` with username `pi` and password `Cornell!32A`.

## Transmitter
The button shorts across two pads when pressed. The voltage across these is 3.3V.