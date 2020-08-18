# Setup

## Installation
- install qemu
    sudo apt install qemu
- download dependencies
    - Download latest image from: http://downloads.raspberrypi.org/raspbian_lite/images/
    - Download a qemu kernel and the dtb for image from: https://github.com/dhruvvyas90/qemu-rpi-kernel
    - 
## Running
Use the following command:

    qemu-system-arm -M versatilepb -dtb versatile-pb-buster.dtb -cpu arm1176 -kernel kernel-qemu-4.19.50-buster -m 256 -drive file=2020-02-13-raspbian-buster-lite.img,format=raw -append "rw console=ttyAMA0 rootfstype=ext4 root=/dev/sda2 loglevel=8" -net user,hostfwd=tcp::22023-:22,hostfwd=tcp::9090-:9090 -net nic -serial stdio


    