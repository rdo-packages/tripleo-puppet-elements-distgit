
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    	12.3.1
Release:    	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0: 	https://tarballs.openstack.org/tripleo-puppet-elements/tripleo-puppet-elements-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr

%description
OpenStack TripleO Puppet Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images configured with
Puppet for the TripleO program.

%prep
%setup -q -n tripleo-puppet-elements-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%doc LICENSE
%doc README.rst
%{python3_sitelib}/tripleo_puppet_elements*
%{_datadir}/tripleo-puppet-elements

%changelog
* Tue Jul 28 2020 RDO <dev@lists.rdoproject.org> 12.3.1-1
- Update to 12.3.1

* Tue May 26 2020 RDO <dev@lists.rdoproject.org> 12.3.0-1
- Update to 12.3.0

