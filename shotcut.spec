#
# spec file for package shotcut
#
# Copyright (c) 2021 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%define _legacy_common_support 1

Name:           shotcut
Version:        21.10.31
Release:        7%{?dist}
Summary:        A free, open source, cross-platform video editor
License:        GPLv3+
Group:          Applications/Multimedia
Url:            http://www.shotcut.org/
Source0:        https://github.com/mltframework/shotcut/archive/v%{version}.tar.gz
Source1:	shotcut.desktop

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
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  mlt7-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  libappstream-glib
BuildRequires:  webvfx-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  x264-devel
#
BuildRequires:  libsndfile
BuildRequires:  flac-libs
#
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtmultimedia
Requires:       frei0r-plugins
Requires:       ladspa
Requires:       mlt7
Requires:       python3-mlt7
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
%autosetup -n %{name}-%{version} -p1

%build
%{qmake_qt5} QMAKE_STRIP="" \
          PREFIX=%{buildroot}%{_prefix} \
          QMAKE_CFLAGS+="%{optflags}" \
          QMAKE_CXXFLAGS+="%{optflags}" \
          QMAKE_CFLAGS_RELEASE="%{optflags}" \
          SHOTCUT_VERSION=ARCH-%{version} \
          QMAKE_CXXFLAGS_RELEASE="%{optflags}" \
          DEFINES+=SHOTCUT_NOUPGRADE 

%make_build

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
%{_datadir}/icons/hicolor/*/apps/org.shotcut.Shotcut.png
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/mime/packages/org.shotcut.Shotcut.xml
%{_mandir}/man1/shotcut.1.gz

%changelog

* Fri Nov 19 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.10.31-7 
- Updated to 21.10.31

* Fri Oct 01 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.09.20-7 
- Updated to 21.09.20

* Mon Sep 20 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.09.13-7 
- Updated to 21.09.13

* Fri Sep 03 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.09.13-7 
- Updated to 21.09.13

* Thu Jul 08 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.06.29-7 
- Updated to 21.06.29

* Sat May 29 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.05.18-7 
- Updated to 21.05.18
- Requires mlt7

* Sat Mar 20 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.03.21-7 
- Updated to 21.03.21

* Mon Feb 01 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 21.01.29-7 
- Updated to 21.01.29

* Mon Dec 07 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.11.28-7 
- Updated to 20.11.28

* Mon Sep 28 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.09.27-7 
- Updated to 20.09.27

* Mon Sep 14 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.09.13-7 
- Updated to 20.09.13

* Sun Jul 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.07.11-7 
- Updated to 20.07.11

* Fri Jul 03 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.06.28-7 
- Updated to 20.06.28

* Mon Jun 08 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.06.05-7 
- Updated to 20.06.05

* Sun Apr 12 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.04.12-7 
- Updated to 20.04.12

* Mon Apr 06 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.04.05-7 
- Updated to 20.04.05

* Tue Mar 03 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.04.01-7 
- Updated to 20.04.01

* Thu Feb 20 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 20.02.17-7 
- Updated to 20.02.17

* Wed Jan 01 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.12.31-7 
- Updated to 19.12.31

* Fri Dec 20 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.12.16-7 
- Updated to 19.12.16

* Fri Dec 13 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.12.08-7 
- Updated to 19.12.08

* Thu Oct 24 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.10.20-7 
- Updated to 19.10.20

* Sat Sep 14 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.09.14-7 
- Updated to 19.09.14

* Tue Aug 20 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.08.16-7 
- Updated to 19.08.16

* Thu Jul 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.07.15-2 
- Updated to 19.07.15

* Tue Jun 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.06.15-2 
- Updated to 19.06.15

* Tue Jun 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.06.04-2 
- Updated to 19.06.04

* Sat Jun 01 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.04.30-2 
- Updated to 19.04.30

* Fri Mar 01 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.02.28-2 
- Updated to 19.02.28

* Tue Feb 26 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.02.20-2 
- Updated to 19.02.20

* Fri Feb 01 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.01.27-2 
- Updated to 19.01.27

* Sat Jan 26 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.01.24-2 
- Updated to 19.01.24

* Thu Jan 24 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.01.19-2 
- Updated to 19.01.19

* Thu Dec 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.12.23-2 
- Updated to 18.12.23

* Tue Dec 18 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.12.15-2 
- Updated to 18.12.15

* Mon Nov 19 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.11.18-2 
- Updated to 18.11.18

* Wed Nov 14 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.11.13-2 
- Updated to 18.11.13

* Sun Nov 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.11.04-2 
- Updated to 18.11.04

* Wed Oct 10 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.10.08-2 
- Updated to 18.10.08

* Thu Oct 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.10.01-2 
- Updated to 18.10.01

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
