Summary:	host program (NIKHOF's version)
Summary(pl.UTF-8):   Program host (wersja NIKHOF-a)
Name:		host-nikhof
Version:	991529
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.nikhef.nl/pub/network/host_%{version}.tar.Z
# Source0-md5:	f3c5589cbe168a49581e856fe26b4808
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

And many more; see the manual page, the RELEASE_NOTES, and the
extensively documented code for details.

%description -l pl.UTF-8
Całkowicie nowa implementacja programu host - narzędzia do odpytywania
serwerów nazw, podobnego do nslookup czy dig - ale bardziej
elastyczna i bogata w opcje.

Wśród nowych możliwości są:
- obszerna obsługa błędów
- opcjonalna (bardzo) duża ilość informacji diagnostycznych
- sprawdzanie przy listowaniu stref dodatkowych warunków, takich jak
  nieautorytatywne rekordy sklejające czy wadliwe delegacje
- sprawdzanie czy nazwy domen związane z hostami są kanoniczne
- kontrola spójności TTL przy listowaniu stref
- rekurencyjne przechodzenie wydelegowanych stref do zadanego poziomu
- prowadzenie statystyk rekordów i liczby hostów
- opcja do sprawdzania odwrotnych odwzorowań adresów hostów
- opcja do porównywania rekordów SOA podstawowego i zapasowego serwera
  nazw dla strefy w celu wykrycia anomalii typu zdesynchronizowane
  numery seryjne lub innych rozbieżności
- rozpoznawanie nowych typów rekordów, opisanych w RFC 1183/1348
- podstawowa obsługa NSAP zgodna z RFC 1637
- implementacja typów rekordów PX/GPOS zdefiniowanych w RFC 1664/1712
- implementacja typu rekordu LOC zdefiniowanego w RFC 1876
- rozpoznawanie rekordu AAAA zdefiniowanego w RFC 1884/1886
- obsługa nowych typów rekordów KEY/SIG/NXT/SRV (dopiero w drafcie)
- obsługa typu rekordu NAPTR, rozpoznawanie EID/NIMLOC/ATMA
- obsługa typu rekordu KX, rozpoznawanie CERT
- dopuszczanie wielu argumentów z linii poleceń lub standardowego
  wejścia
- konfigurowalne poprzez zmienną środowiskową opcje domyślne
- przewidywanie odpowiedzi innych niż od BIND-a przy listowaniu stref

i wiele więcej - całość opisana w manualu, RELEASE_NOTES oraz szeroko
udokumentowanym kodzie.

%prep
%setup -q -c host

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_BSD_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install host $RPM_BUILD_ROOT%{_bindir}/host-nikhof
install host.1 $RPM_BUILD_ROOT%{_mandir}/man1/host-nikhof.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
