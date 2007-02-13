%include	/usr/lib/rpm/macros.php
%define		_class		LiveUser
%define		_subclass	Admin
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - user authentication and permission management framework
Summary(pl.UTF-8):	%{_pearname} - uwierzytelnianie użytkowników i zarządzanie uprawnieniami
Name:		php-pear-%{_pearname}
Version:	0.3.9
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7dd4abf529fd60b9a3637f0801374a33
URL:		http://pear.php.net/package/LiveUser_Admin/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-LiveUser >= 0.16.0
Requires:	php-pear-PEAR-core >= 1:1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiveUser_Admin is meant to be used with the LiveUser package. It is
composed of all the classes necessary to administrate data used by
LiveUser.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
LiveUser_Admin przeznaczony jest do używania wraz z klasą LiveUser.
Składa się ze wszystkich klas potrzebnych do administracji danymi
używanymi przez klasę LiveUser.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
