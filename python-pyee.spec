%define module pyee

Name:		python-pyee
Version:	13.0.1
Release:	1
Summary:	A rough port of Node.js's EventEmitter to Python
License:	MIT
Group:		Development/Python
URL:		https://pyee.readthedocs.io
# upstream repo: https://github.com/jfhbrook/pyee
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools_scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires: python%{pyver}dist(typing-extensions)

%description
pyee supplies a EventEmitter object that is similar to the EventEmitter class
from Node.js.

It also supplies a number of subclasses with added support for async and
threaded programming in python, such as async/await.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
