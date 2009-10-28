subarch: i686
version_stamp: minimal
target: livecd-stage1
rel_type: default
profile: default/linux/x86/2008.0
snapshot: 2009.0
source_subpath: default/stage3-i686-2009.0
portage_confdir: /var/svn/pentoo/livecd/trunk/portage
portage_overlay: /usr/local/portage /usr/portage/local/layman/enlightenment
# /usr/portage/local/layman/jokey
cflags: -Os -march=i686 -mtune=prescott -pipe -fomit-frame-pointer
cxxflags: -Os -march=i686 -mtune=prescott -pipe -fomit-frame-pointer


# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
# pkgcache_path:

livecd/use: -X livecd -gnome -nls -gtk -kde -eds -gtk2 -cairo pam -firefox gpm
mmx sse sse2 mpi wps offensive
wifi injection lzma speed gnuplot pyx bluetooth test-programs fwcutter subversion
-quicktime -qt -qt3 -qt3support -qt4 -webkit -cups -spell lua curl
-xrandr
consolekit
sqlite -truetype
-opengl dbus binary-drivers -hal acpi usb

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages:
=sys-kernel/pentoo-sources-2.6.31-r1
sys-apps/pentoo
app-admin/localepurge
app-admin/syslog-ng
app-arch/gzip
app-crypt/johntheripper
app-editors/hexedit
app-editors/nano
app-forensics/cmospwd
app-misc/livecd-tools
app-misc/screen
app-portage/layman
net-analyzer/netcat
net-analyzer/nmap
#net-analyzer/ntop
net-analyzer/tcpdump
net-analyzer/traceroute
net-dialup/linux-atm
net-dialup/lrzsz
net-dialup/minicom
net-dns/bind-tools
net-fs/nfs-utils
net-fs/mount-cifs
net-ftp/ftp
net-ftp/oftpd
net-irc/irssi
net-misc/bridge-utils
net-misc/dhcpcd
net-misc/netsed
net-misc/ntp
net-misc/openvpn
net-misc/socat
net-misc/stunnel
net-wireless/aircrack-ng
net-wireless/airoscript
net-wireless/broadcom-firmware-downloader
#net-wireless/intel-wimax-network-service
net-wireless/kismet
net-wireless/rfkill
net-wireless/wireless-tools
net-wireless/wpa_supplicant
sys-apps/hwsetup
sys-apps/iproute2
sys-apps/less
sys-apps/microcode-ctl
sys-apps/microcode-data
sys-apps/pciutils
sys-apps/sysvinit
sys-apps/v86d
sys-block/disktype
sys-boot/grub
sys-boot/syslinux
sys-fs/device-mapper
sys-fs/jfsutils
sys-fs/reiserfsprogs
sys-fs/reiser4progs
sys-fs/squashfs-tools
sys-libs/libkudzu
sys-power/acpid
sys-power/acpitool
sys-power/powertop
www-client/lynx
