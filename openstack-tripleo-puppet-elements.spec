%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    	6.2.4
Release:    	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0: 	https://tarballs.openstack.org/tripleo-puppet-elements/tripleo-puppet-elements-%{upstream_version}.tar.gz

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
* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 6.2.4-1
- Update to 6.2.4

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 6.2.3-1
- Update to 6.2.3

* Thu Oct 05 2017 rdo-trunk <javier.pena@redhat.com> 6.2.2-1
- Update to 6.2.2

* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 6.2.1-1
- Update to 6.2.1

* Thu Jul 27 2017 rdo-trunk <javier.pena@redhat.com> 6.2.0-1
- Update to 6.2.0

* Fri Jul 14 2017 Alfredo Moralejo <amoralej@redhat.com> 6.1.0-1
- Update to 6.1.0

* Wed Mar 08 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-1
- Update to 6.0.0

* Mon Mar 06 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.2.0rc2
- Update to 6.0.0.0rc2

* Fri Feb 17 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.1.0rc1
- Update to 6.0.0.0rc1

