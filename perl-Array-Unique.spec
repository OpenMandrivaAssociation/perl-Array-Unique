%define module   Array-Unique
%define version    0.08
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Tie-able array that allows only unique values
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Array/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This package lets you create an array which will allow only one occurrence
of any value.

In other words no matter how many times you put in 42 it will keep only the
first occurrence and the rest will be dropped.

You use the module via tie and once you tied your array to this module it
will behave correctly.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


