#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyroute2.ndb
Version  : 0.6.5
Release  : 11
URL      : https://files.pythonhosted.org/packages/04/ad/b1463f337c8d9b7d4be04edf187626b9707765be47dfb9f30d03bb053562/pyroute2.ndb-0.6.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/ad/b1463f337c8d9b7d4be04edf187626b9707765be47dfb9f30d03bb053562/pyroute2.ndb-0.6.5.tar.gz
Summary  : Python Netlink library: NDB module
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pypi-pyroute2.ndb-bin = %{version}-%{release}
Requires: pypi-pyroute2.ndb-license = %{version}-%{release}
Requires: pypi-pyroute2.ndb-python = %{version}-%{release}
Requires: pypi-pyroute2.ndb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: pyroute2.ndb
Provides: pyroute2.ndb-python
Provides: pyroute2.ndb-python3
BuildRequires : pypi(pyroute2.core)

%description
============
        
        PyRoute2 is a pure Python **netlink** library.
        
        NDB is a high-level network management module. It provides a transactional DB
        with multiple sources, from local RTNL source to netns and remote systems. The
        DB provides Python API and HTTP RPC (json and plain text), my run as a
        standalone service or may be used as a Python module.
        
        links
        =====

%package bin
Summary: bin components for the pypi-pyroute2.ndb package.
Group: Binaries
Requires: pypi-pyroute2.ndb-license = %{version}-%{release}

%description bin
bin components for the pypi-pyroute2.ndb package.


%package license
Summary: license components for the pypi-pyroute2.ndb package.
Group: Default

%description license
license components for the pypi-pyroute2.ndb package.


%package python
Summary: python components for the pypi-pyroute2.ndb package.
Group: Default
Requires: pypi-pyroute2.ndb-python3 = %{version}-%{release}

%description python
python components for the pypi-pyroute2.ndb package.


%package python3
Summary: python3 components for the pypi-pyroute2.ndb package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2.ndb)
Requires: pypi(pyroute2.core)

%description python3
python3 components for the pypi-pyroute2.ndb package.


%prep
%setup -q -n pyroute2.ndb-0.6.5
cd %{_builddir}/pyroute2.ndb-0.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641478985
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ndb
cp %{_builddir}/pyroute2.ndb-0.6.5/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ndb/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.ndb-0.6.5/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ndb/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyroute2-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyroute2.ndb/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pypi-pyroute2.ndb/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
