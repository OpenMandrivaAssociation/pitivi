%define name pitivi
%define pitividir %_prefix/lib
%define gnonlin 0.10.6.1
Summary: Pitivi non linear video editor under linux 
Name: %name
Version: 0.11.1
Release: %mkrel 3
Source0: http://download.gnome.org/sources/pitivi/%{name}-%{version}.tar.bz2
Patch: pitivi-0.11.0-desktopentry.patch
License: GPL
Group: Video
URL: http://www.pitivi.org
BuildRequires:  python-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  perl-XML-Parser
Requires:  python-zope-interface
Requires:  python-setuptools
Requires:  pygtk2.0-libglade
Requires:  gnome-python
Requires:  gnome-python-gnomevfs
Requires:  gstreamer0.10-python
Requires:  gstreamer0.10-plugins-base
Requires:  gnonlin >= %gnonlin

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
%endif
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS  ChangeLog NEWS RELEASE
%{_datadir}/pitivi/
%{_bindir}/pitivi
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%pitividir/pitivi/
%_liconsdir/*png
%_iconsdir/*png
%_miconsdir/*png


