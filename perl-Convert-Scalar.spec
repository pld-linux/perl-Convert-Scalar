#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Convert
%define		pnam	Scalar
Summary:	Convert::Scalar - convert between different representations of perl scalars
Summary(pl.UTF-8):	Convert::Scalar - konwersja między różnymi reprezentacjami perlowych skalarów
Name:		perl-Convert-Scalar
Version:	1.04
Release:	15
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	849a207e94b7714c677f476608418199
URL:		http://search.cpan.org/dist/Convert-Scalar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports various internal perl methods that change the
internal representation or state of a perl scalar. All of these work
in-place, that is, they modify their scalar argument.

%description -l pl.UTF-8
Ten moduł eksportuje różne wewnętrzne perlowe metody zmieniające
wewnętrzną reprezentację lub stan perlowego skalara. Wszystko to
działa "na miejscu", czyli modyfikowany jest argument skalarny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Convert/Scalar.pm
%dir %{perl_vendorarch}/auto/Convert/Scalar
%attr(755,root,root) %{perl_vendorarch}/auto/Convert/Scalar/Scalar.so
%{_mandir}/man3/*
