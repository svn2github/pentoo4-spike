subarch: i686
version_stamp: 2006.2
target: livecd-stage1
rel_type: default
profile: default-linux/x86/2006.1
snapshot: 2006.2
source_subpath: default/stage3-i686-2006.2
portage_confdir: /root/catalyst-pentoo/x86/portage
portage_overlay: /usr/local/portage

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
# pkgcache_path:

livecd/use: X livecd -gnome -nls gtk fbcon opengl -kde -eds gtk2 cairo -pam firefox gpm dvdr oss mmx sse sse2 -quicktime -qt -cups -spell png

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages:
app-admin/gamin
app-admin/localepurge
app-admin/syslog-ng
app-arch/gzip
app-crypt/chntpw
app-crypt/plaintoo
app-editors/hexedit
app-editors/mp
app-editors/nano
app-forensics/cmospwd
app-fuzz/bss
app-misc/emelfm
app-misc/examine
app-misc/livecd-tools
app-mobilephone/obexftp
app-portage/gentoolkit
app-text/dos2unix
dev-db/edb
dev-libs/eet
dev-libs/embryo
dev-libs/engrave
dev-libs/libxslt
dev-libs/openobex
dev-perl/gtk-perl
dev-python/pygtk
dev-util/dialog
dev-util/e_utils
dev-util/subversion
media-gfx/entice
media-gfx/scrot
media-libs/edje
media-libs/epeg
media-libs/epsilon
media-libs/imlib2
media-plugins/xmms-liveice
media-sound/alsa-utils
media-sound/sox
media-sound/xmms
net-analyzer/amap
net-analyzer/arpwatch
net-analyzer/dsniff
net-analyzer/wireshark
net-analyzer/ettercap
net-analyzer/hping
net-analyzer/ike-scan
net-analyzer/macchanger
=net-analyzer/metasploit-2.6
net-analyzer/nbtscan
net-analyzer/nessus
net-analyzer/netcat
net-analyzer/nikto
net-analyzer/nmap
net-analyzer/p0f
net-analyzer/thcrut
net-analyzer/traceroute
net-analyzer/xprobe
net-analyzer/yersinia
net-dialup/minicom
net-dns/bind-tools
net-firewall/firehol
net-firewall/iptables
net-ftp/ftp
net-ftp/oftpd
net-im/gaim
net-irc/irssi
net-irc/xchat
net-misc/dhcpcd
net-misc/ipsorcery
net-misc/rdesktop
net-misc/telnet-bsd
net-wireless/aircrack-ng
net-wireless/airsnort
net-wireless/bluez-firmware
net-wireless/bluez-libs
net-wireless/bluez-utils
#net-wireless/btscanner commented due to compile problem
net-wireless/hostapd
net-wireless/hostap-utils
net-wireless/ipw3945d
net-wireless/wifi-radar
net-wireless/wifitap
net-wireless/wireless-tools
sys-apps/baselayout
sys-apps/coldplug
sys-apps/eject
sys-apps/hwdata-gentoo
sys-apps/hwsetup
sys-apps/iproute2
sys-apps/less
sys-apps/parted
sys-apps/pciutils
sys-apps/portage
sys-apps/slocate
sys-block/disktype
sys-block/gparted
sys-boot/grub
sys-boot/syslinux
sys-devel/gettext
sys-fs/jfsutils
sys-fs/reiserfsprogs
sys-fs/reiser4progs
sys-fs/squashfs-tools
sys-fs/udev
sys-libs/gpm
sys-libs/libkudzu
sys-power/acpid
www-client/mozilla-firefox-bin
x11-base/xorg-x11
x11-libs/ecore
x11-libs/esmart
x11-libs/evas
x11-libs/ewl
x11-libs/gtk+
x11-misc/xdialog
x11-terms/eterm
x11-terms/xterm
x11-wm/e

# x11-plugins/e_modules

