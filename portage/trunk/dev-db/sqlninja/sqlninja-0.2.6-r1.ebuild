# Copyright 1999-2010 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /root/portage/net-analyzer/sqlinject/sqlinject-1.1.ebuild,v 1.1.1.1 2006/03/21 14:30:26 grimmlin Exp $

EAPI=4

MY_P="${P}-r1"

DESCRIPTION="A SQL Server injection & takeover tool"
HOMEPAGE="http://sqlninja.sourceforge.net/"
SRC_URI="mirror://sourceforge/${PN}/${MY_P}.tgz"
LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE=""

DEPEND=""
RDEPEND="dev-lang/perl
	dev-perl/NetPacket
	dev-perl/Net-Pcap
	dev-perl/Net-DNS
	dev-perl/Net-RawIP
	dev-perl/IO-Socket-SSL
	dev-perl/List-MoreUtils"

S="${WORKDIR}"/"${MY_P}"

src_install () {
	dodoc sqlninja-howto.html ChangeLog
	rm sqlninja-howto.html ChangeLog README LICENSE
	dodir /usr/lib/"${PN}"/
	cp -R * "${D}"/usr/lib/"${PN}"/
	dosbin "${FILESDIR}"/"${PN}"
	dosym /usr/lib/"${PN}"/makescr.pl /usr/sbin/makescr.pl
}