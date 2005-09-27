%include	/usr/lib/rpm/macros.php
%define		_class		LiveUser
%define		_subclass	Admin
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - user authentication and permission management framework
Summary(pl):	%{_pearname} - uwierzytelnianie u¿ytkowników i zarz±dzanie uprawnieniami
Name:		php-pear-%{_pearname}
Version:	0.3.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4ff186006c64eb25a106cef255a18236
URL:		http://pear.php.net/package/LiveUser_Admin/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiveUser_Admin is meant to be used with the LiveUser package. It is
composed of all the classes necessary to administrate data used by
LiveUser.

In PEAR status of this package is: %{_status}.

%description -l pl
LiveUser_Admin przeznaczony jest do u¿ywania wraz z klas± LiveUser.
Sk³ada siê ze wszystkich klas potrzebnych do administracji danymi
u¿ywanymi przez klasê LiveUser.

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
