Summary:	Test a Render extension implementation
Name:		rendercheck
Version:	1.5
Release:	3
License:	MIT
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros) >= 1.8
BuildRequires:	pkgconfig(xrender)

%description
rendercheck is a program to test a Render extension implementation against
separate calculations of expected output.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/rendercheck
%doc %{_mandir}/man1/rendercheck.*
