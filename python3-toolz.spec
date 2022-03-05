#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	List processing tools and functional utilities
Summary(pl.UTF-8):	Narzędzia do przetwarzania list oraz funkcyjne
Name:		python3-toolz
Version:	0.11.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/toolz/
Source0:	https://files.pythonhosted.org/packages/source/t/toolz/toolz-%{version}.tar.gz
# Source0-md5:	6326604f5ed1bc84fa4538b6ab37ad5d
URL:		https://pypi.org/project/toolz/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of utility functions for iterators, functions, and dictionaries.

%description -l pl.UTF-8
Zbiór funkcji narzędziowych do iteratorów, funkcji i słowników.

%prep
%setup -q -n toolz-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest toolz/tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/toolz/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md LICENSE.txt README.rst
%{py3_sitescriptdir}/tlz
%{py3_sitescriptdir}/toolz
%{py3_sitescriptdir}/toolz-%{version}-py*.egg-info
