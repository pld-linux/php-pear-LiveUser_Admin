%include	/usr/lib/rpm/macros.php
%define		_class		LiveUser
%define		_subclass	Admin
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - user authentication and permission management framework
Summary(pl):	%{_pearname} - uwierzytelnianie u¿ytkowników i zarz±dzanie uprawnieniami
Name:		php-pear-%{_pearname}
Version:	0.3.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	30fcdc534c1b2f039bb7186f4afdb532
URL:		http://pear.php.net/package/LiveUser_Admin/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
