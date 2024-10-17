Summary:	A lyrics provider plugin for gmpc
Name:		gmpc-lyrics
Version:	11.8.16
Release:	2
License:	GPLv2+
Group:		Sound
Url:		https://www.sarine.nl//gmpc-plugins-lyrics-provider
Source0:	http://download.sarine.nl/Programs/gmpc/11.8.16/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	libxml2-devel
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	gtk+2-devel >= 2.8
BuildRequires:	curl-devel
BuildRequires:	intltool
Requires:	gmpc

%description
A lyrics provider plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/lyricsplugin.so


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2mdv2011.0
+ Revision: 610906
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531609
- update to new version 0.20.0

* Sat Dec 26 2009 Funda Wang <fwang@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 482402
- BR intltool
- new version 0.19.0

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.18.0-2mdv2010.0
+ Revision: 455846
- rebuild for new curl SSL backend

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 379403
- BR curl
- New version 0.18.0

* Mon Dec 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.17.0-1mdv2009.1
+ Revision: 321126
- update to new version 0.17.0

* Wed Dec 03 2008 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 309576
- move plugins

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix file list
    - update to new version 0.16.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246283
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160391
- add missing buildrequires on libcurl
- add spec file
- add source
- Created package structure for gmpc-lyrics.


