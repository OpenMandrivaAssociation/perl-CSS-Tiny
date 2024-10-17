%define upstream_name	 CSS-Tiny
%define upstream_version 1.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Read/Write .css files with as little code as possible
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CSS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/CSS
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.190.0-2mdv2011.0
+ Revision: 680707
- mass rebuild

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 575587
- update to 1.19

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 551969
- update to 1.17

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.0
+ Revision: 402135
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.15-3mdv2009.0
+ Revision: 256389
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2008.1
+ Revision: 105303
- update to new version 1.15


* Tue Sep 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2007.0
- New version 1.14

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-2mdv2007.0
- Rebuild

* Thu Nov 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdk
- New release 1.11
- spec cleanup
- %%mkrel
- make tests in %%check
- fix directory ownership

* Tue Aug 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdk
- new version
- fix sources url for rpmbuildupdate

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.05-1mdk
- initial Mandriva package

