#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	List processing tools and functional utilities
Summary(pl.UTF-8):	Narzędzia do przetwarzania list oraz funkcyjne
Name:		python-toolz
# keep 0.10.x here for python2 support
Version:	0.10.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/toolz/
Source0:	https://files.pythonhosted.org/packages/source/t/toolz/toolz-%{version}.tar.gz
# Source0-md5:	3cb4317dbaff18b5a9201b69e57692a6
URL:		https://pypi.org/project/toolz/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of utility functions for iterators, functions, and dictionaries.

%description -l pl.UTF-8
Zbiór funkcji narzędziowych do iteratorów, funkcji i słowników.

%package -n python3-toolz
Summary:	List processing tools and functional utilities
Summary(pl.UTF-8):	Narzędzia do przetwarzania list oraz funkcyjne
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-toolz
A set of utility functions for iterators, functions, and dictionaries.

%description -n python3-toolz -l pl.UTF-8
Zbiór funkcji narzędziowych do iteratorów, funkcji i słowników.

%prep
%setup -q -n toolz-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest toolz/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest toolz/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/toolz/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/toolz/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/tlz
%{py_sitescriptdir}/toolz
%{py_sitescriptdir}/toolz-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-toolz
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/tlz
%{py3_sitescriptdir}/toolz
%{py3_sitescriptdir}/toolz-%{version}-py*.egg-info
%endif
