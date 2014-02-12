%global realname google-authenticator

Name:           %{realname}
Version:        1.1
Release:        2%{?dist}
Summary:        Google Authenticator library

Group:          Development/Security
License:        Apache License 2.0
URL:            https://http://code.google.com/p/%{realname}/
Source0:        https://github.com/mikemackintosh/google-authenticator/archive/master.zip

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

%clean
make clean

%changelog
* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.1-2
- Added %clean

* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.1-1
- Version 1.1

* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.0-1
- Version 1.0
