Summary:	JPEG Scaling Library
Summary(pl):	Biblioteka do skalowania JPEG-�w
Name:		epeg
Version:	0.9.0.004
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	ad8505bed8deb7049dfa6322ce908f99
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

%description -l pl
Epeg to biblioteka u�atwiaj�ca bardzo szybkie skalowanie obraz�w JPEG.

%package libs
Summary:	Epeg library
Summary(pl):	Biblioteka epeg
Group:		Libraries

%description libs
Epeg library.

%description libs -l pl
Biblioteka epeg.

%package devel
Summary:	Epeg header files
Summary(pl):	Pliki nag��wkowe Epeg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libjpeg-devel

%description devel
Header files for Epeg.

%description devel -l pl
Pliki nag��wkowe Epeg.

%package static
Summary:	Static Epeg library
Summary(pl):	Statyczna biblioteka Epeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Epeg library.

%description static -l pl
Statyczna biblioteka Epeg.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libepeg.a
