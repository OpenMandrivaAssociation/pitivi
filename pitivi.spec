%define url_ver %(echo %{version}|cut -d. -f1,2)
%define pitividir %{_prefix}/lib
%define gnonlin	0.10.16
%define gstpy	0.10.19
%define gstapi	0.10

Summary:	Non linear video editor under linux 
Name:		pitivi
Version:	0.15.2
Release:	1
License:	LGPLv2+
Group:		Video
Url:		http://www.pitivi.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(python)
Requires:	python-zope-interface
Requires:	python-pkg-resources
Requires:	pygtk2.0-libglade
Requires:	gnome-python
Requires:	gnome-python-gnomevfs
Requires:	gstreamer%{gstapi}-python >= %{gstpy}
Requires:	gstreamer%{gstapi}-plugins-base >= 0.10.24
Requires:	gnonlin >= %{gnonlin}
Requires:	python-pygoocanvas
Requires:	python-dbus
Requires:	pyxdg
#gw for make check
#BuildRequires:	x11-server-xvfb
#BuildRequires:	python-zope-interface
#BuildRequires:	python-pkg-resources
#BuildRequires:	pygtk2.0-libglade
#BuildRequires:	gnome-python
#BuildRequires:	gnome-python-gnomevfs
#BuildRequires:	gstreamer%{gstapi}-python >= %{gstpy}
#BuildRequires:	gstreamer%{gstapi}-plugins-base >= 0.10.24
#BuildRequires:	gnonlin >= %{gnonlin}
#BuildRequires:	python-pygoocanvas
Suggests:	gstreamer%{gstapi}-plugins-good
Suggests:	gstreamer%{gstapi}-plugins-bad
Suggests:	gstreamer%{gstapi}-plugins-ugly
Suggests:	gstreamer%{gstapi}-plugin-ffmpeg

%description
Pitivi is a Non Linear Video Editor using the popular GStreamer media
framework.

%prep
%setup -q
%apply_patches

%build
./configure --prefix=%{_prefix} --libdir=%{pitividir}
%make

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%check
#gw it currently needs an installed pitivi
#https://bugzilla.gnome.org/show_bug.cgi?id=594985
#xfvb-run make check

%files -f %{name}.lang
%doc AUTHORS  ChangeLog NEWS RELEASE
%{_bindir}/pitivi
%{pitividir}/pitivi/
%{_datadir}/pitivi/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/%{name}.1*

