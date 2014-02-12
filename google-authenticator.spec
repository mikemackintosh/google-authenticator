%global realname google-authenticator

Name:           %{realname}
Version:        1.0
Release:        1%{?dist}
Summary:        Google Authenticator library

Group:          Development/Security
License:        Apache License 2.0
URL:            https://http://code.google.com/p/%{realname}/
Source0:        http://%{realname}.googlecode.com/files/libpam-%{realname}-%{version}-source.tar.bz2

BuildArch:      noarch
BuildRequires:  pam-devel

%description
Used for google-authentication

%prep
%setup -q -n libpam-%{realname}-%{version}

%build
make

%install
make install

%changelog
* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.0-1
- Version 1.0
