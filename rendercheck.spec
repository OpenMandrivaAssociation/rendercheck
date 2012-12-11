Name: rendercheck
Version: 1.4
Release: %mkrel 1
Summary: Test a Render extension implementation
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


%changelog
* Mon Nov 22 2010 Thierry Vignaud <tv@mandriva.org> 1.4-1mdv2011.0
+ Revision: 599631
- new release
- fix summary

* Mon Apr 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3-5mdv2010.1
+ Revision: 536775
- rebuild

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2010.0
+ Revision: 433332
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 269219
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2mdv2009.0
+ Revision: 194845
- rendercheck is a program to test a Render extension implementation against
  separate calculations of expected output.
- rendercheck package.

