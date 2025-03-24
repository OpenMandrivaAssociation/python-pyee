%define module pyee

Name:		python-pyee
Version:	13.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Summary:	A rough port of Node.js's EventEmitter to Python
URL:		https://pypi.org/project/pyee/
License:	MIT
Group:		Development/Python

BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-wheel
BuildRequires:	python-typing-extensions
BuildRequires:	python-docutils
Requires: python-typing-extensions

%description
pyee supplies a EventEmitter object that is similar to the EventEmitter class
from Node.js.

It also supplies a number of subclasses with added support for async and
threaded programming in python, such as async/await.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build
rst2man docs/man.rst docs/pyee.1
zstd -r --rm docs/pyee.1

%install
%py3_install
install -Dpm 0644 docs/pyee.1.zst %{buildroot}%{_mandir}/man1/pyee.1.zst

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-*.*-info
%{_mandir}/man1/pyee.1.zst
%doc README.md
%license LICENSE