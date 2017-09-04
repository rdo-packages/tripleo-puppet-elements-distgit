%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    	5.3.1
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
* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 5.3.1-1
- Update to 5.3.1

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 5.3.0-1
- Update to 5.3.0

* Tue Feb 14 2017 Alan Pevec <apevec AT redhat.com> 5.2.1-1
- Update to 5.2.1

* Wed Jan 04 2017 Jon Schlueter <jschluet@redhat.com> 5.2.0-1
- Update to 5.2.0

* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 5.1.0-1
- Update to 5.1.0

* Thu Oct 20 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-1
- Update to 5.0.0

* Thu Sep 29 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.3.0rc2
- Update to 5.0.0.0rc2

* Thu Sep 22 2016 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-0.2.0rc1
- Update to 5.0.0.0rc1

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.1.0b3
- Update to 5.0.0.0b3

