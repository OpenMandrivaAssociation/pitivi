%define url_ver %(echo %{version}|cut -d. -f1,2)
%define pitividir %{_prefix}/lib
%define gstapi	1.0

Summary:	Non linear video editor under linux 
Name:		pitivi
Version:	0.92
Release:	5
License:	LGPLv2+
Group:		Video
Url:		http://www.pitivi.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Requires:	python-gi >= 2.90.2
Requires:	python-gi-cairo
Requires:	frei0r
Requires:	python-dbus
Requires:	xdg-utils
Requires:	gnonlin >= 1.1.90
Requires:	gstreamer%{gstapi}-python
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
%apply_patches

# install python files to %%python_sitelib/pitivi
find . -name Makefile.am -exec sed -i -e 's|$(libdir)/pitivi/python/pitivi|$(pkgpythondir)|g' {} \;
find . -name Makefile.in -exec sed -i -e 's|$(libdir)/pitivi/python/pitivi|$(pkgpythondir)|g' {} \;

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
%doc AUTHORS NEWS RELEASE
%{python_sitelib}/%{name}/
%{_datadir}/pitivi/
%{_datadir}/appdata/pitivi.appdata.xml
%{_bindir}/pitivi
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml
