#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Request-WithApacheSession
Summary:	MasonX::Request::WithApacheSession - add a session to the Mason Request object
Summary(pl):	MasonX::Request::WithApacheSession - dodawanie sesji do obiektu Mason Request
Name:		perl-MasonX-Request-WithApacheSession
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d613565d3c7b2242b75e9f7552470dcf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Apache-Session-Wrapper >= 0.13
BuildRequires:	perl-HTML-Mason >= 1.16
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module integrates Apache::Session into Mason by adding methods to
the Mason Request object available in all Mason components.

%description -l pl
Ten modu³ integruje Apache::Session w Masona poprzez dodanie do
obiektu Mason Request metod dostêpnych we wszystkich komponentach
Masona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
