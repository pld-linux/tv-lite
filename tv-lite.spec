Summary:	Easy to use IPTV, Sopcast, Acestream Player
Name:		tv-lite
Version:	0.7.6
Release:	2
License:	GPL v2
Group:		Applications/Multimedia
Source0:	https://gitlab.com/cburneci/tv-lite/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c2cd068b0dcaec49e671da0c8df7f9ee
Patch0:		cxx-types.patch
URL:		https://www.tv-lite.com/
BuildRequires:	curl-devel
BuildRequires:	gettext
BuildRequires:	gtk+3-devel
BuildRequires:	pkgconfig
BuildRequires:	rapidjson-devel
BuildRequires:	sqlite3-devel
BuildRequires:	vlc-devel
BuildRequires:	wxGTK3-unicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TV-Lite is a IPTV player, with Sopcast and Acestream handling
capabilities. It uses the well known VLC for displaying media.

%prep
%setup -q
%patch -P 0 -p1

%build
mkdir -p build
cd build
%cmake ../src \
	-DWX_CONFIG=%{_bindir}/wx-gtk3-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang TVLite

%clean
rm -rf $RPM_BUILD_ROOT

%files -f TVLite.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/TVLite
%{_datadir}/TVLite
%{_desktopdir}/TVLite.desktop
%{_pixmapsdir}/TVLite.png

