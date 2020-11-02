%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    	13.0.0
Release:    	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0: 	https://tarballs.openstack.org/tripleo-puppet-elements/tripleo-puppet-elements-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/tripleo-puppet-elements/tripleo-puppet-elements-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:	noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr

%description
OpenStack TripleO Puppet Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images configured with
Puppet for the TripleO program.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Mon Nov 02 2020 RDO <dev@lists.rdoproject.org> 13.0.0-1
- Update to 13.0.0

