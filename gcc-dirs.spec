Summary:	Common dirs for GCC compilers and crosscompilers
Summary(pl):	Katalogi wspólne dla kompilatorów zwyk³ych i skro¶nych z kolekcji GNU
Name:		gcc-dirs
Version:	1.0
Release:	3
License:	free
Group:		Base
Requires:	gcc >= 5:3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for GNU collection of compilers and crosscompilers.

%description -l pl
Katalogi wspólne dla kompilatorów zwyk³ych i skro¶nych z kolekcji GNU.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gcc/%{_target_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{_target_platform}
