%define name pitivi
%define pitividir %_prefix/lib
%define gnonlin 0.10.13
Summary: Pitivi non linear video editor under linux 
Name: %name
Version: 0.13.3.2
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2

License: LGPLv2+
Group: Video
URL: http://www.pitivi.org
%py_requires -d
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
Requires:  python-zope-interface
Requires:  python-pkg-resources
Requires:  pygtk2.0-libglade
Requires:  gnome-python
Requires:  gnome-python-gnomevfs
Requires:  gstreamer0.10-python >= 0.10.16
Requires:  gstreamer0.10-plugins-base >= 0.10.24
Requires:  gnonlin >= %gnonlin
Requires:  python-pygoocanvas
#gw for make check
#BuildRequires:  x11-server-xvfb
#BuildRequires:  python-zope-interface
#BuildRequires:  python-pkg-resources
#BuildRequires:  pygtk2.0-libglade
#BuildRequires:  gnome-python
#BuildRequires:  gnome-python-gnomevfs
#BuildRequires:  gstreamer0.10-python >= 0.10.16
#BuildRequires:  gstreamer0.10-plugins-base >= 0.10.24
#BuildRequires:  gnonlin >= %gnonlin
#BuildRequires:  python-pygoocanvas

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Pitivi is a Non Linear Video Editor using the popular GStreamer media
framework.


%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%pitividir
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name

%check
#gw it currently needs an installed pitivi
#https://bugzilla.gnome.org/show_bug.cgi?id=594985
#xfvb-run make check

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%update_menus
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor
%postun
%clean_menus
%clean_mime_database
%clean_desktop_database
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS  ChangeLog NEWS RELEASE
%{_datadir}/pitivi/
%{_bindir}/pitivi
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/mime/packages/%name.xml
%pitividir/pitivi/
