Name: rendercheck
Version: 1.5
Release: 1
Summary: Test a Render extension implementation
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libxrender-devel

%description
rendercheck is a program to test a Render extension implementation against
separate calculations of expected output.

%prep
%setup -q -n %{name}-%{version}

%build
%configure

%make

%install
%makeinstall_std

%files
%{_bindir}/rendercheck
%{_mandir}/man1/rendercheck.*
