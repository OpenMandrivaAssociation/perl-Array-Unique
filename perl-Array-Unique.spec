%define upstream_name    Array-Unique
Name:		perl-%{upstream_name}
Version:	0.08
Release:	6

Summary:	Tie-able array that allows only unique values
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Array/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This package lets you create an array which will allow only one occurrence
of any value.

In other words no matter how many times you put in 42 it will keep only the
first occurrence and the rest will be dropped.

You use the module via tie and once you tied your array to this module it
will behave correctly.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 654875
- rebuild for updated spec-helper

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 402980
- rebuild using %0.08 Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 384437
- import perl-Array-Unique


* Tue Jun 09 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

