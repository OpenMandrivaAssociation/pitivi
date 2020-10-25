%define url_ver %(echo %{version}|cut -d. -f1,2)
%define pitividir %{_prefix}/lib
%define gstapi 1.0
%define debug_package %{nil}

Summary:	Non linear video editor under linux 
Name:		pitivi
Version:	2020.09.2
Release:	1
License:	LGPLv2+
Group:		Video
Url:		http://www.pitivi.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	pitivi.rpmlintrc

BuildRequires:  yelp
BuildRequires:  yelp-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(yelp-xsl)
BuildRequires:	git-core
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	meson
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(py3cairo)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(gst-transcoder-1.0)
Requires:	gnome-video-effects
Requires:	python-gi
Requires:	python-gi-cairo
Requires:	python-gstreamer1.0
Requires:	gstreamer1.0-nle
Requires: python-matplotlib
Requires: python-matplotlib-cairo
Requires:	frei0r
Requires:	python-dbus
Requires:	xdg-utils
Requires:	typelib(Gst)
Requires:	typelib(GES)
Requires:	typelib(Clutter)
Requires:	typelib(Cogl)
Requires:	typelib(GObject)
Requires:	typelib(Gdk)
Requires:	typelib(GdkPixbuf)
Requires:	typelib(Gio)
Requires:	typelib(GstPbutils)
Requires:	typelib(Gtk)
Requires:	typelib(GtkClutter)
Requires:	typelib(Pango)
Requires:	typelib(GDesktopEnums)
Requires: typelib(GstTranscoder)
Requires: typelib(GstValidate)

Recommends:	gstreamer%{gstapi}-libav
Recommends:	gstreamer%{gstapi}-plugins-good
Recommends:	gstreamer%{gstapi}-plugins-bad
Recommends:	gstreamer%{gstapi}-plugins-ugly
Recommends:	gstreamer%{gstapi}-plugin-ffmpeg

%description
Pitivi is a Non Linear Video Editor using the popular GStreamer media
framework.

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS MAINTAINERS README.md
%{python_sitearch}/%{name}/
%{_datadir}/pitivi/
%{_datadir}/metainfo/org.pitivi.Pitivi.appdata.xml
%{_bindir}/pitivi
%{_datadir}/applications/org.pitivi.Pitivi.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/org.pitivi.Pitivi-mime.xml


#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

# install python files to %%python_sitelib/pitivi
sed -i -e 's|/pitivi/python/|/python%{python3_version}/site-packages/|g' meson.build

%build
%meson
%meson_build

%install
%meson_install

#missing files
#install -Dpm644 docs/pitivi.1 %{buildroot}%{_mandir}/man1/pitivi.1

# we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name} --with-gnome

%check
#gw it currently needs an installed pitivi
#https://bugzilla.gnome.org/show_bug.cgi?id=594985
#xfvb-run make check

