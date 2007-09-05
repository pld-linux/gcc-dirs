Summary:	Common dirs for GCC compilers and crosscompilers
Summary(pl.UTF-8):	Katalogi wspólne dla kompilatorów zwykłych i skrośnych z kolekcji GNU
Name:		gcc-dirs
Version:	1.0
Release:	5
License:	free
Group:		Base
Requires:	FHS
Conflicts:	gcc < 5:3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for GNU collection of compilers and crosscompilers.

%description -l pl.UTF-8
Katalogi wspólne dla kompilatorów zwykłych i skrośnych z kolekcji GNU.

%prep

%install
rm -rf $RPM_BUILD_ROOT
# still there's no gpc for gcc >= 3.4
install -d $RPM_BUILD_ROOT%{_libdir}/{gcc,gcc-lib}/%{_target_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/gcc*
