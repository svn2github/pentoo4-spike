# Copyright 1999-2004 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /root/portage/app-fuzz/protos/protos-0.1.ebuild,v 1.1.1.3 2006/03/08 18:55:18 grimmlin Exp $

SNMP_VER="r1"
HTTP_VER="r1"
H2250_VER="r2"
LDAP_VER="r1"
SIP_VER="r2"
ISAKMP_VER="r1"

DESCRIPTION="The protos fuzzing collection, containing http-reply, ldapv3, snmpv1, sip, h2250v4 and isakmp"
HOMEPAGE="http://www.ee.oulu.fi/research/ouspg/protos/"
SRC_URI="http://www.ee.oulu.fi/research/ouspg/protos/testing/c05/http-reply/c05-http-reply-${HTTP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/ldapv3/c06-ldapv3-enc-${LDAP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/ldapv3/c06-ldapv3-app-${LDAP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/snmpv1/c06-snmpv1-req-app-${SNMP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/snmpv1/c06-snmpv1-req-enc-${SNMP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/snmpv1/c06-snmpv1-trap-app-${SNMP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c06/snmpv1/c06-snmpv1-trap-enc-${SNMP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c07/sip/c07-sip-${SIP_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c07/h2250v4/c07-h2250v4-${H2250_VER}.jar
	 http://www.ee.oulu.fi/research/ouspg/protos/testing/c09/isakmp/c09-isakmp-${ISAKMP_VER}.jar
"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~x86"
IUSE=""

DEPEND="virtual/jre"

src_unpack () {
	einfo "Nothing to unpack"
	mkdir "${S}"
}

src_compile () {
	einfo "Nothing to compile"
	einfo "Copying binary files"
	for x in $A
	do
		cp "${DISTDIR}"/"${x}" "${S}"/
	done
}

src_install () {
	insinto /opt/protos/
	for x in $A
	do
		doins "${x}"
	done
	dosbin "${FILESDIR}"/protos
}
