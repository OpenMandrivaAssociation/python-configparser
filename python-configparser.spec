Name:           python-configparser
Version:        5.3.0
Release:        1
Summary:        Backport of the enhanced config parser introduced in Python 3.x
License:        MIT
Group:          Development/Languages/Python
URL:            http://docs.python.org/3/library/configparser.html
Source:         https://files.pythonhosted.org/packages/source/c/configparser/configparser-%{version}.tar.gz
#BuildRequires:  python3dist(backports)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  pkgconfig(python)
BuildRequires:  python-unittest2
Requires:       python-backports
BuildArch:      noarch

%description
The ancient ConfigParser module available in the standard library 2.x has
seen a major update in Python 3.x. This is a backport of those changes so
that they can be used directly in Python 2.7.

%prep
%setup -q -n configparser-%{version}
rm pytest.ini

%build
export LANG=en_US.UTF-8
%py_build

%install
export LANG=en_US.UTF-8
%py_install

%files
%doc README.rst CHANGES.rst
%license LICENSE
%{python_sitelib}/__pycache__/configparser.cpython-*.pyc
%{python_sitelib}/backports/configparser/
#{python_sitelib}/configparser-%{version}-info
%{python_sitelib}/configparser-*.dist-info
%{python_sitelib}/configparser.py

