# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    	10.3.2
Release:    	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0: 	https://tarballs.openstack.org/tripleo-puppet-elements/tripleo-puppet-elements-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python%{pyver}-devel
BuildRequires:	python%{pyver}-setuptools
BuildRequires:	python%{pyver}-pbr
%if %{pyver} == 2
BuildRequires:	python-d2to1
%else
BuildRequires:	python%{pyver}-d2to1
%endif

%description
OpenStack TripleO Puppet Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images configured with
Puppet for the TripleO program.

%prep
%setup -q -n tripleo-puppet-elements-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%doc LICENSE
%doc README.rst
%{pyver_sitelib}/tripleo_puppet_elements*
%{_datadir}/tripleo-puppet-elements

%changelog
* Wed Sep 11 2019 RDO <dev@lists.rdoproject.org> 10.3.2-1
- Update to 10.3.2

* Fri Jul 05 2019 RDO <dev@lists.rdoproject.org> 10.3.1-1
- Update to 10.3.1

* Thu Apr 18 2019 RDO <dev@lists.rdoproject.org> 10.3.0-1
- Update to 10.3.0

