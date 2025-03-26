%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		vo-aacenc
Version:	0.1.3
Release:	1
Summary:	VisualOn AAC encoder library
License:	ASL 2.0
Group:		System/Libraries
URL:		https://opencore-amr.sourceforge.net/
Source0:	http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

This package is in restricted because the AAC encoding standard is
covered by patents.

%package -n %{libname}
Group:		System/Libraries
Summary:	VisualOn AAC encoder library

%description -n %{libname}
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

This package is in restricted because the AAC encoding standard is
covered by patents.

%package -n %{develname}
Group:		Development/C
Summary:	development files for %{name} AAC encoding library
Provides:	libvo-aacenc-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Header files and development libraries for %{name}

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%__rm -rf %{buildroot}%{_libdir}/lib%{name}.la

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%doc COPYING ChangeLog NOTICE README
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu May 17 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.1.2-1
- New version 1.2
- Add docs
- Don't package .a & .la files
- Change tainted to restricted in description

* Thu May 26 2011 cjw <cjw> 0.1.1-2.mga1.tainted
+ Revision: 100421
- add library dependency on devel package

* Tue May 10 2011 cjw <cjw> 0.1.1-1.mga1
+ Revision: 96794
- add 'tainted' notice
- imported package vo-aacenc

