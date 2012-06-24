Summary:	Welsh dictionary for aspell
Summary(pl):	Walijski s�ownik dla aspella
Name:		aspell-cy
Version:	0.50
%define	subv	3
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/cy/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	d59fee193dba87973b38ac2862a090bb
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Welsh dictionary (i.e. word list) for aspell.

%description -l pl
Walijski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
