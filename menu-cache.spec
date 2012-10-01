Summary:	Library creating and utilizing menu caches
Name:		menu-cache
Version:	0.3.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	a14b0b162cd64d56c16bf6af16f3a47f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
brary creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus

%package devel
Summary:	Header files for menu-cache library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for menu-cache library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/menu-cache-gen
%attr(755,root,root) %{_libexecdir}/menu-cached
%attr(755,root,root) %ghost %{_libdir}/libmenu-cache.so.?
%attr(755,root,root) %{_libdir}/libmenu-cache.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmenu-cache.so
%{_libdir}/libmenu-cache.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

