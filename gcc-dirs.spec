Summary:	Common dirs for GCC compilers and crosscompilers
Summary(pl):	Katalogi wspólne dla kompilatorów zwyk³ych i skro¶nych z kolekcji GNU
Name:		gcc-dirs
Version:	1.0
Release:	1
License:	free
Group:		Base
Conflicts:	gcc <= 5:3.3.4-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for GNU collection of compilers and crosscompilers.

%description -l pl
Katalogi wspólne dla kompilatorów zwyk³ych i skro¶nych z kolekcji GNU.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/{gcc,gcc-lib/%{arch}-pld-linux}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc-lib
%dir %{_libdir}/gcc-lib/%{arch}-pld-linux
