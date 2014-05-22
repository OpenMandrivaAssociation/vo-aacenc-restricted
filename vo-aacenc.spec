%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		vo-aacenc
Version:	0.1.2
Release:	1
Summary:	VisualOn AAC encoder library
License:	ASL 2.0
Group:		System/Libraries
URL:		http://opencore-amr.sourceforge.net/
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
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std


%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


