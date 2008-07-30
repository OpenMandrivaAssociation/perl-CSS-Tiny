%define module	CSS-Tiny
%define name	perl-%{module}
%define version 1.15
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Summary:	Read/Write .css files with as little code as possible
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/CSS/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/CSS
%{_mandir}/*/*

