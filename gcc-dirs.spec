Summary:	Common dirs for GCC compilers and crosscompilers
Summary(pl):	Katalogi wspólne dla kompilatorów zwyk³ych i skro¶nych z kolekcji GNU
Name:		gcc-dirs
Version:	1.0
Release:	3
License:	free
Group:		Base
Conflicts:	gcc < 5:3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for GNU collection of compilers and crosscompilers.

%description -l pl
Katalogi wspólne dla kompilatorów zwyk³ych i skro¶nych z kolekcji GNU.

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
