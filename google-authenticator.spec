%global realname google-auth
%define _binaries_in_noarch_packages_terminate_build   0

Name:           shutterstock-%{realname}-pam
Version:        1.1
Release:        2%{?dist}
Summary:        Google Authenticator library
Packager: 	Mike Mackintosh <m@rocketho.me>

Group:          System Environment/Libraries
License:        Apache License 2.0
URL:            http://code.google.com/p/google-authenticator/
Source0:        https://github.com/mikemackintosh/google-authenticator/archive/master.zip
BuildArch:      noarch
BuildRequires:  pam-devel

%description
Used for google-authentication

Provides: google-authenticator
Obsoletes: google-authenticator

%description
The Google Authenticator package contains a pluggable authentication
module (PAM) which allows login using one-time passcodes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Passcode generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm currently in draft.

%prep
%setup -q -n google-authenticator-master/libpam

%build
#make CFLAGS="${CFLAGS:-%optflags}" LDFLAGS=-ldl %{?_smp_mflags}
make

#%check
#./pam_google_authenticator_unittest

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security
install -m0755 pam_google_authenticator.so $RPM_BUILD_ROOT/%{_lib}/security/pam_google_authenticator.so

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0755 google-authenticator $RPM_BUILD_ROOT/%{_bindir}/google-authenticator

%files
/%{_lib}/security/*
%{_bindir}/google-authenticator

%doc FILEFORMAT README totp.html

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.1-2
- Version 1.2
- fixed build

* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.1-1
- Version 1.1

* Wed Jan 12 2014 Mike Mackintosh <m@rocketho.me> - 1.0-1
- Version 1.0
