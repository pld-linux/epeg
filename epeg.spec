#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	JPEG Scaling Library
Summary(pl.UTF-8):   Biblioteka do skalowania JPEG-ów
Name:		epeg
Version:	0.9.0.007
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	383db51e46d13d986966459e4918d236
URL:		http://enlightenment.org/Libraries/Epeg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epeg is a library which provides facilities for scaling JPEG images
very quickly.

%description -l pl.UTF-8
Epeg to biblioteka ułatwiająca bardzo szybkie skalowanie obrazów JPEG.

%package libs
Summary:	Epeg library
Summary(pl.UTF-8):   Biblioteka epeg
Group:		Libraries

%description libs
Epeg library.

%description libs -l pl.UTF-8
Biblioteka epeg.

%package devel
Summary:	Epeg header files
Summary(pl.UTF-8):   Pliki nagłówkowe Epeg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libjpeg-devel

%description devel
Header files for Epeg.

%description devel -l pl.UTF-8
Pliki nagłówkowe Epeg.

%package static
Summary:	Static Epeg library
Summary(pl.UTF-8):   Statyczna biblioteka Epeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Epeg library.

%description static -l pl.UTF-8
Statyczna biblioteka Epeg.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/epeg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepeg.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epeg-config
%attr(755,root,root) %{_libdir}/libepeg.so
%{_libdir}/libepeg.la
%{_includedir}/Epeg*
%{_pkgconfigdir}/epeg.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libepeg.a
%endif
