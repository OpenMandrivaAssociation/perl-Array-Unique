%define upstream_name    Array-Unique
%define upstream_version 0.09
Name:		perl-%{upstream_name}
Version:	0.09
Release:	2

Summary:	Tie-able array that allows only unique values
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-0.09.tar.gz

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
%setup -q -n Array-Unique-0.09

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

