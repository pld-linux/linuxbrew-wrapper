Summary:	Homebrew package manager for Linux
Name:		linuxbrew-wrapper
Version:	20160506
Release:	1
License:	BSD-2-Clause
Group:		Applications
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.gz
# Source0-md5:	1d412434c1bb0c161ea7e5825fb83efc
Source1:	https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}-1.debian.tar.xz
# Source1-md5:	9dcd40ccb9197b8aa6ed19b9813082a0
URL:		http://linuxbrew.sh/
Requires:	build-essential
Requires:	curl
Requires:	git-core
Requires:	python-setuptools
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		_libexecdir	%{_prefix}/lib

%description
Linuxbrew is a fork of Homebrew, the Mac OS package manager, for
Linux.

It can be installed in your home directory and does not require root
access. The same package manager can be used on both your Linux server
and your Mac laptop. Installing a modern version of glibc and gcc in
your home directory on an old distribution of Linux takes five
minutes.

Features:
  - Can install software to a home directory and so does not require
    sudo
  - Install software not packaged by the native distribution
  - Install up-to-date versions of software when the native distribution
    is old
  - Use the same package manager to manage both your Mac and Linux
    machines

This package provides Linuxbrew upstream install and uninstall
scripts, and a wrapper script written by Debian package maintainer.

%prep
%setup -qc -a1
patch -p1 < debian/patches/fix-interpreter

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man7,%{_libexecdir}/%{name}}
install -p debian/bin/linuxbrew $RPM_BUILD_ROOT%{_bindir}
install -p install $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -p uninstall $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -p debian/linuxbrew-wrapper.7 $RPM_BUILD_ROOT%{_mandir}/man7
ln -s linuxbrew $RPM_BUILD_ROOT%{_bindir}/brew
ln -s linuxbrew-wrapper.7 $RPM_BUILD_ROOT%{_mandir}/man7/linuxbrew.7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/linuxbrew
%attr(755,root,root) %{_bindir}/brew
%{_mandir}/man7/linuxbrew-wrapper.7*
%{_mandir}/man7/linuxbrew.7*
%dir %{_libexecdir}/%{name}
%attr(755,root,root) %{_libexecdir}/%{name}/install
%attr(755,root,root) %{_libexecdir}/%{name}/uninstall
