#!/bin/bash

#apt-get -y update && apt-get -y upgrade
sudo apt-get -y install raspberrypi-kernel-headers git libgmp3-dev gawk qpdf bison flex make

git clone https://github.com/seemoo-lab/nexmon.git
cd nexmon
cd buildtools/isl-0.10
./configure
make
make install
ln -s /usr/local/lib/libisl.so /usr/lib/arm-linux-gnueabihf/libisl.so.10

cd ../../
source setup_env.sh
make
cd patches/bcm43430a1/7_45_41_46/nexmon/
make
make backup-firmware
make install-firmware

cd ../../../../
cd utilities/nexutil/
make && make install
cd ../../

apt-get -y remove wpasupplicant

mv "$(modinfo brcmfmac -n)" "$(modinfo brcmfmac -n).orig"
cp patches/bcm43430a1/7_45_41_46/nexmon/brcmfmac_4.14.y-nexmon/brcmfmac.ko "$(modinfo brcmfmac -n)"
depmod -a