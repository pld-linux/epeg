Summary:	JPEG Scaling Library
Name:		epeg
Version:	0.9.0
%define	_snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	3780cd02824944b1d64db8d57869b8fd
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epeg is a library which provides facilities for scaling JPEG images
very quickly.

%package devel
Summary:	Epeg headers, documentation and test programs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libjpeg-devel

%description devel
Headers, test programs and documentation for Epeg.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
%setup -q -n %{name}

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/epeg
%attr(755,root,root) %{_libdir}/libepeg.so*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libepeg.la
%attr(755,root,root) %{_bindir}/epeg-config
%{_includedir}/Epeg*

%files static
%defattr(644,root,root,755)
%{_libdir}/libepeg.a
