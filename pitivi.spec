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

Requires:	python-gi >= 2.90.2
Requires:	python-gi-cairo
Requires:	frei0r
Requires:	python-dbus
Requires:	xdg-utils
Requires:	gnonlin >= 1.1.90
Requires:	gstreamer1.0-python
Suggests:	gstreamer1.0-libav

%description
Pitivi is a Non Linear Video Editor using the popular GStreamer media
framework.

%prep
%setup -q

# install python files to %%python_sitelib/pitivi
find . -name Makefile.am -exec sed -i -e 's|$(libdir)/pitivi/python/pitivi|$(pkgpythondir)|g' {} \;
find . -name Makefile.in -exec sed -i -e 's|$(libdir)/pitivi/python/pitivi|$(pkgpythondir)|g' {} \;

%build
%configure --libdir=%{_datadir}
%make

%install
%makeinstall_std

desktop-file-edit --add-category "Video" %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name} --with-help

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

