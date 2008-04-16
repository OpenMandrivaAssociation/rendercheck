Name: rendercheck
Version: 1.3
Release: %mkrel 2
Summary: a program to test a Render extension implementation
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/rendercheck
%{_mandir}/man1/rendercheck.*
