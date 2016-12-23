#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mongodict
Version  : 0.3.1
Release  : 14
URL      : https://pypi.python.org/packages/source/m/mongodict/mongodict-0.3.1.tar.gz
Source0  : https://pypi.python.org/packages/source/m/mongodict/mongodict-0.3.1.tar.gz
Summary  : MongoDB-backed Python dict-like interface
Group    : Development/Tools
License  : GPL-3.0
Requires: mongodict-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
mongodict - MongoDB-backed Python dict-like interface
=====================================================

%package python
Summary: python components for the mongodict package.
Group: Default

%description python
python components for the mongodict package.


%prep
%setup -q -n mongodict-0.3.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
