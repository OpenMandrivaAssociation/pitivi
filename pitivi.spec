%define name pitivi
%define pitividir %_prefix/lib
%define gnonlin 0.10.11
Summary: Pitivi non linear video editor under linux 
Name: %name
Version: 0.13.1.2
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2

Patch: pitivi-0.13.0.3-desktopentry.patch
License: LGPLv2+
Group: Video
URL: http://www.pitivi.org
%py_requires -d
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
Requires:  python-zope-interface
Requires:  python-pkg-resources
Requires:  pygtk2.0-libglade
Requires:  gnome-python
Requires:  gnome-python-gnomevfs
Requires:  gstreamer0.10-python
Requires:  gstreamer0.10-plugins-base
Requires:  gnonlin >= %gnonlin
Requires:  python-pygoocanvas

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Pitivi is a Non Linear Video Editor using the popular GStreamer media
framework.


%prep
%setup -q
%patch -p1

%build
./configure --prefix=%_prefix --libdir=%pitividir
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name

mkdir -p %buildroot/{%_liconsdir,%_miconsdir,%_iconsdir} 
install pitivi/pixmaps/pitivi-video.png %buildroot/%_liconsdir/%name.png
convert -scale 32 pitivi/pixmaps/pitivi-video.png %buildroot/%_iconsdir/%name.png
convert -scale 16 pitivi/pixmaps/pitivi-video.png %buildroot/%_miconsdir/%name.png

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
%_datadir/pixmaps/%name.png
%_datadir/icons/hicolor/*/apps/*
%_datadir/mime/packages/%name.xml
%pitividir/pitivi/
%_liconsdir/*png
%_iconsdir/*png
%_miconsdir/*png
