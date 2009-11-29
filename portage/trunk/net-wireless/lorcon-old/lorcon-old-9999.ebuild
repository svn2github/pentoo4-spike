# Copyright 1999-2009 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

inherit toolchain-funcs eutils subversion


DESCRIPTION="A generic library for injecting 802.11 frames"
HOMEPAGE="http://802.11ninja.net/lorcon"
SRC_URI=""
ESVN_REPO_URI="https://802.11ninja.net/svn/lorcon/branch/lorcon-old"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE=""

DEPEND="$RDEPEND"
RDEPEND="dev-libs/libnl
		 net-libs/libpcap"

src_install() {
	DESTDIR="${D}" emake install
	# rename manpage to avoid conflict with lorcon
	mv "${D}"/usr/share/man/man3/lorcon.3 "${D}"/usr/share/man/man3/lorcon-old.3
}
