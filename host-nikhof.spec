Summary:	host program (NIKHOF's version)
Summary(pl):	Program host (wersja NIKHOF'a)
Name:		host-nikhof
Version:	991529
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.nikhef.nl/pub/network/host_%{version}.tar.Z
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A completely new version of 'host', a nameserver query utility a la
'nslookup' and 'dig', but much more versatile and robust.

Among the new features are:
 - Extensive error checking.
 - Optionally (very) verbose output and debugging info.
 - Checking for extraneous conditions during zone listings such as
   non-authoritative glue records and lame delegations.
 - Checking for illegal characters in certain domain names.
 - Verify that some host-related domain names are canonical.
 - Perform ttl consistency checking during zone listings.
 - Recursive traversion of delegated zones up to a given level.
 - Maintaining of resource record and host count statistics.
 - Option to check reverse mappings of host addresses.
 - Option to compare SOA records at the primary and secondary
   nameservers of a zone to check for anomalies such as out-of-sync
   serial numbers, and other discrepancies.
 - Recognition of the new RR types as defined by RFC 1183/1348.
 - Basic NSAP support according to RFC 1637.
 - Implement PX/GPOS RR types as defined by RFC 1664/1712.
 - Implement LOC RR type as defined by RFC 1876.
 - Recognize AAAA RR type as defined by RFC 1884/1886.
 - Support for new RR types KEY/SIG/NXT/SRV (still in draft).
 - Support for RR type NAPTR. Recognize EID/NIMLOC/ATMA.
 - Support for RR type KX. Recognize CERT.
 - Allow multiple arguments on command line or from stdin.
 - Configurable default options via an environment variable.
 - Anticipate non-BIND behaviour during zone listings.

And many more; see the manual page, the RELEASE NOTES, and the
extensively documented code for details.

%description -l pl
Ca³kowicie nowa implementacja host'a z wieloma nowymi mo¿liwo¶ciami.

%prep
%setup -q -c host

%build
%{__make} CFLAGS="%{rpmcflags} -D_BSD_SOURCE" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d   $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install host $RPM_BUILD_ROOT%{_bindir}/host-nikhof
install host.1 $RPM_BUILD_ROOT%{_mandir}/man1/host-nikhof.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
