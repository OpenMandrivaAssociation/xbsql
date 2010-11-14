%define name		xbsql
%define version		0.11
%define release		%mkrel 15
%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname -d %name

Summary:	XBSQL: An SQL wrapper for xbase
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		Databases
Source: 	%{name}-%{version}.tar.bz2
Patch0:		xbsql-0.11-xbase64.patch
Patch1:		xbsql-0.11-link.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://www.quaking.demon.co.uk/xbsql/
BuildRequires:  xbase-devel
BuildRequires:  readline-devel
BuildRequires:  bison
Requires:	xbase

%description
Xbase DBMS is a C++ library which supports access to Xbase type datafiles and
indexes (ie., .dbf and related files).

%package -n %{libname}
Summary: Libraries needed for %{name}
Group:   System/Libraries

%description -n %{libname}
Libraries needed for %{name}

%package -n %{develname}
Summary: Headers for %{name} 
Group: Development/Other
Conflicts: %{libname} < 0.11-15
Requires: %{libname} = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %{name}-devel < %version-%release
Obsoletes: %{mklibname -d xbsql 0}

%description -n %{develname}
Headers for %{name}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p0
sed -i -e 's#/usr/lib/libncurses#%{_libdir}/libncurses#' configure.*

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{libname}-devel -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname}-devel -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README AUTHORS TODO ChangeLog 
%{_bindir}/xql

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libxbsql.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/xbsql.h
%{_libdir}/libxbsql.so
%{_libdir}/libxbsql.la
%{_libdir}/libxbsql.a 
