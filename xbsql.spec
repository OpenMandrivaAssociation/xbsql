%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname -d %name

Summary:	An SQL wrapper for xbase
Name:		xbsql
Version:	0.11
Release:	17
License:	LGPLv2+
Group:		Databases
Source0: 	%{name}-%{version}.tar.bz2
Patch0:		xbsql-0.11-xbase64.patch
Patch1:		xbsql-0.11-link.patch
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
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{EVRD}
Obsoletes: %{name}-devel < %{version}-%{release}
Obsoletes: %{mklibname -d xbsql 0}

%description -n %{develname}
Headers for %{name}

%prep
%setup -q
%patch0 -p1
%patch1 -p0
sed -i -e 's#/usr/lib/libncurses#%{_libdir}/libncurses#' configure.*

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README AUTHORS TODO ChangeLog 
%{_bindir}/xql

%files -n %{libname}
%{_libdir}/libxbsql.so.%{major}*

%files -n %{develname}
%{_includedir}/xbsql.h
%{_libdir}/libxbsql.so
%{_libdir}/libxbsql.a 


%changelog
* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 0.11-15mdv2011.0
+ Revision: 597445
- build with xbase64
- fix linkage

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.11-14mdv2010.0
+ Revision: 445889
- rebuild

* Fri Apr 03 2009 Funda Wang <fwang@mandriva.org> 0.11-13mdv2009.1
+ Revision: 363765
- fix spec

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.11-13mdv2009.0
+ Revision: 262258
- rebuild

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 0.11-12mdv2009.0
+ Revision: 257470
- use sed magic rather than patch
- BR libtool
- bunzip2 the patch
- new devel package policy and license policy

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.11-11mdv2009.0
+ Revision: 256623
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.11-9mdv2008.1
+ Revision: 129855
- kill re-definition of %%buildroot on Pixel's request
- import xbsql


* Sun Dec 11 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.11-9mdk
- Patch0: fix ncurse detection on x86_64 and so fix build on that arch

* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.11-8mdk
- Fix BuildRequires

* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.11-7mdk
- Fix BuildRequires

* Mon Apr 04 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.11-6mdk
- %%mkrel 
- Rebuild for readline

* Sat Jun 5 2004 Spencer Anderson <sdander@oberon.ark.com> 0.11-5mdk
- correct %%Summary

* Sat Jun 5 2004 Spencer Anderson <sdander@oberon.ark.com> 0.11-4mdk
- rebuild
- spec cleaning

* Sun Jan 4 2004 Spencer Anderson <sdander@oberon.ark.com> 0.11-3mdk
- buildrequires libreadline-devel
- move some libs

* Thu Dec 25 2003 Spencer Anderson <sdander@oberon.ark.com> 0.11-2mdk
- include missing libraries
- buildrequires and requires

* Tue Nov 18 2003 Spencer Anderson <sdander@oberon.ark.com> 0.11-1mdk
- initial Mandrake release
- needed by rekall

