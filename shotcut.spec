Name:           shotcut
Version:        18.09.16
Release:        2%{?dist}
Summary:        A free, open source, cross-platform video editor
License:        GPLv3+
Group:          Applications/Multimedia
Url:            http://www.shotcut.org/
Source0:        https://github.com/mltframework/shotcut/archive/v%{version}.tar.gz
Source1:	shotcut.desktop
Patch:	        mlt_path.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(mlt++) >= 6.10.0
BuildRequires:  pkgconfig(mlt-framework) >= 6.10.0
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  x264-devel

Requires:       qt5-qtquickcontrols
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtmultimedia
Requires:       frei0r-plugins
Requires:       ladspa
Requires:       mlt
Requires:       lame
Requires:       ffmpeg


%description
Shotcut is a free and open-source cross-platform video editing application for
Windows, OS X, and Linux. 

Shotcut supports many video, audio, and image formats via FFmpeg and screen, 
webcam, and audio capture. It uses a timeline for non-linear video editing of 
multiple tracks that may be composed of various file formats. Scrubbing and 
transport control are assisted by OpenGL GPU-based processing and a number of 
video and audio filters are available.

%prep
%setup -n %{name}-%{version}
%patch -p0

%build

qmake-qt5 'CONFIG-=c++11' \
          QMAKE_STRIP="" \
          PREFIX=%{buildroot}%{_prefix} \
          QMAKE_CFLAGS+="%{optflags}" \
          QMAKE_CXXFLAGS+="%{optflags}"

make V=1 %{?_smp_mflags}


%install
%make_install V=1
install -D icons/%{name}-logo-64.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -D --mode=644 %{S:1} %{buildroot}/usr/share/applications/shotcut.desktop
chmod a+x %{buildroot}/usr/share/shotcut/qml/export-edl/rebuild.sh

%files
%{_bindir}/shotcut
%{_datadir}/shotcut/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/org.shotcut.Shotcut.desktop
%{_datadir}/icons/hicolor/64x64/apps/org.shotcut.Shotcut.png
%{_datadir}/metainfo/org.shotcut.Shotcut.appdata.xml
%{_datadir}/mime/packages/org.shotcut.Shotcut.xml

%changelog

* Thu Sep 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.09.16-2 
- Updated to 18.09.16

* Sun Sep 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.09.15-2 
- Updated to 18.09.15

* Fri Sep 14 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.09.13-2 
- Updated to 18.09.13

* Fri Aug 17 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.08.14-2 
- Updated to 18.08.14

* Sat Aug 11 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.08.11-2 
- Updated to 18.08.11

* Thu Aug 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.08-2 
- Updated to 18.08

* Mon Jul 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.07-2 
- Updated to 18.07

* Wed Jun 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.06.02-2 
- Updated to 18.06.02

* Fri Jun 01 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.06-2 
- Updated to 18.06

* Wed May 09 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.05.08-2 
- Updated to 18.05.08

* Fri May 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.05-2 
- Updated to 18.05

* Mon Apr 09 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 18.04-2
- Updated to 18.04

* Wed Mar 07 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 18.03-2
- Updated to 18.03

* Wed Jan 03 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 18.01-2
- Updated to 18.01

* Wed Dec 06 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.12-2
- Updated to 17.12

* Sun Nov 05 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.11-2
- Updated to 17.11

* Mon Oct 02 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.10-1
- Updated to 17.10

* Tue Sep 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.09-1
- Updated to 17.09

* Thu Aug 10 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.08-1
- Updated to 17.08

* Sat Jun 10 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.06-1
- Updated 17.06-1

* Sat Mar 25 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 17.03-1
- Updated 17.03-1

* Wed Aug 24 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 16.08-1
- Updated

* Tue Jul 12 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 16.07-1
- Initial build
