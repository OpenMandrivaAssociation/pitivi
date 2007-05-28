%define name pitivi
%define pitividir %_prefix/lib
%define gnonlin 0.10.6.1
Summary: Pitivi non linear video editor under linux 
Name: %name
Version: 0.10.2.2
Release: %mkrel 1
Source0: http://download.gnome.org/sources/pitivi/%{name}-%{version}.tar.bz2
License: GPL
Group: Video
URL: http://www.pitivi.org
BuildRequires:  pygtk2.0-devel
BuildRequires:  pygtk2.0-libglade
BuildRequires:  gnome-python
BuildRequires:  gnome-python-gnomevfs
BuildRequires:  gstreamer0.10-python >= 0.10
BuildRequires:  libgstreamer-devel >= 0.10
BuildRequires: gnonlin >= %gnonlin
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
Requires:  pygtk2.0-libglade
Requires:  gnome-python
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

%build
./configure --prefix=%_prefix --libdir=%pitividir
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name} 
?package(%{name}): command="%name" icon="%name.png" longtitle="Non-linear video editor" title="Pitivi" needs=x11 section="Multimedia/Video" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --add-category="Video;AudioVideoEditing" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p %buildroot/{%_liconsdir,%_miconsdir,%_iconsdir} 
install pitivi/pixmaps/pitivi-video.png %buildroot/%_liconsdir/%name.png
convert -scale 32 pitivi/pixmaps/pitivi-video.png %buildroot/%_iconsdir/%name.png
convert -scale 16 pitivi/pixmaps/pitivi-video.png %buildroot/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%update_menus
%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS  ChangeLog NEWS RELEASE
%{_datadir}/pitivi/
%{_bindir}/pitivi
%_menudir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%pitividir/pitivi/
%_liconsdir/*png
%_iconsdir/*png
%_miconsdir/*png


