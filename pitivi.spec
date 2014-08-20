%define _files_listed_twice_terminate_build 0
%define gstapi	1.0

Summary:	Non linear video editor under linux 
Name:		pitivi
Version:	0.93
Release:	2
License:	LGPLv2+
Group:		Video
Url:		http://www.pitivi.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/%{version}/%{name}-%{version}.tar.xz
Source100:	pitivi.rpmlintrc

BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	gnonlin >= 1.2.0
BuildRequires:	gnome-doc-utils


Requires:	gstreamer1.0-tools
Requires:	python-gi >= 2.90.2
Requires:	python-gi-cairo
Requires:	frei0r
Requires:	python-dbus
Requires:	xdg-utils
Requires:	gnonlin >= 1.2.0
Requires:	python-gstreamer1.0
Requires:	%{_lib}clutter-gst-gir2.0
Requires:	%{_lib}clutter-gtk-gir1.0

Suggests:	gstreamer%{gstapi}-libav
Suggests:	gstreamer%{gstapi}-plugins-good
Suggests:	gstreamer%{gstapi}-plugins-bad
Suggests:	gstreamer%{gstapi}-plugins-ugly
Suggests:	gstreamer%{gstapi}-plugin-ffmpeg

%description
Pitivi is a Non Linear Video Editor using the popular GStreamer media
framework.

%prep
%setup -q

%build
%configure --libdir=%{_datadir}
%make

%install
%makeinstall_std

desktop-file-edit --add-category "Video" %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README RELEASE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.*
%{_datadir}/help/*
%{_datadir}/appdata/pitivi.appdata.xml