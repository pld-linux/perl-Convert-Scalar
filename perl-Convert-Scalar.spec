#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Scalar
Summary:	Convert::Scalar - convert between different representations of perl scalars
Summary(pl):	Convert::Scalar - konwersja miêdzy ró¿nymi reprezentacjami perlowych skalarów
Name:		perl-Convert-Scalar
Version:	0.1e
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8fed7f80ed55e2f2593495513c3e1f8d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports various internal perl methods that change the
internal representation or state of a perl scalar. All of these work
in-place, that is, they modify their scalar argument.

%description -l pl
Ten modu³ eksportuje ró¿ne wewnêtrzne perlowe metody zmieniaj±ce
wewnêtrzn± reprezentacjê lub stan perlowego skalara. Wszystko to
dzia³a "na miejscu", czyli modyfikowany jest argument skalarny.

%prep
%setup -q -n %{pdir}-%{pnam}-0.1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/Convert/Scalar/Scalar.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Convert/Scalar/Scalar.so
%{_mandir}/man3/*
