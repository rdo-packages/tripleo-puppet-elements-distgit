%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    	7.0.3
Release:    	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0: 	https://tarballs.openstack.org/tripleo-puppet-elements/tripleo-puppet-elements-%{upstream_version}.tar.gz

#

BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

%description
OpenStack TripleO Puppet Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images configured with
Puppet for the TripleO program.

%prep
%setup -q -n tripleo-puppet-elements-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%doc LICENSE
%doc README.md
%{python_sitelib}/tripleo_puppet_elements*
%{_datadir}/tripleo-puppet-elements

%changelog
* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 7.0.3-1
- Update to 7.0.3

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 7.0.2-1
- Update to 7.0.2

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 7.0.1-1
- Update to 7.0.1

* Thu Sep 14 2017 rdo-trunk <javier.pena@redhat.com> 7.0.0-1
- Update to 7.0.0

* Sun Sep 10 2017 rdo-trunk <javier.pena@redhat.com> 7.0.0-0.2.0rc1
- Update to 7.0.0.0rc2

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 7.0.0-0.1.0rc1
- Update to 7.0.0.0rc1

