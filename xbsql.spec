%define name		xbsql
%define version		0.11
%define release		%mkrel 9
%define major		0
%define libname		%mklibname %name %major

Summary:	XBSQL: An SQL wrapper for xbase
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
Source: 	%{name}-%{version}.tar.bz2
Patch0:		xbsql-ncurces-x86_64.patch.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://www.quaking.demon.co.uk/xbsql/
BuildRequires:  libxbase-devel 
BuildRequires:  libreadline-devel
BuildRequires:  ncurses-devel
BuildRequires:  bison
Requires:	xbase

%description
Xbase DBMS is a C++ library which supports access to Xbase type datafiles and
indexes (ie., .dbf and related files).

%package -n %{libname}
Summary: Libraries needed for %{name}
Group:   System/Libraries
Provides: lib%{name} = %version-%release

%description -n %{libname}
Libraries needed for %{name}

%package -n %{libname}-devel
Summary: Headers for %{name} 
Group: Development/Other
Requires: %{libname} = %version-%release
Provides: %name-devel = %version-%release
Provides: lib%{name}-devel = %version-%release
Obsoletes: %{name}-devel < %version-%release

%description -n %{libname}-devel
Headers for %{name}

%prep
%setup -n %{name}-%{version}
%patch0

%build
rm -f config.cache
%configure
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
%{_libdir}/libxbsql.la
%{_libdir}/libxbsql.so.0
%{_libdir}/libxbsql.so.0.0.0

%files -n %{libname}-devel
%defattr(-,root,root,-)
%{_includedir}/xbsql.h
%{_libdir}/libxbsql.so
%{_libdir}/libxbsql.a 

