#
# RPM Spec for pScheduler Simplestream Test
#

%define short	simplestream
%define perfsonar_auto_version 4.3.0
%define perfsonar_auto_relnum 0.a0.0

Name:		pscheduler-test-%{short}
Version:	%{perfsonar_auto_version}
Release:	%{perfsonar_auto_relnum}%{?dist}

Summary:	Simplestream test class for pScheduler
BuildArch:	noarch
License:	ASL 2.0
Vendor:	perfSONAR
Group:		Unspecified

Source0:	%{short}-%{version}.tar.gz

Provides:	%{name} = %{version}-%{release}

Requires:	pscheduler-server >= 1.1.6
Requires:	python-pscheduler > 1.3.2.6.0
Requires:	python-jsontemplate

BuildRequires:	pscheduler-rpm


%description
Simplestream test class for pScheduler


%prep
%setup -q -n %{short}-%{version}


%define dest %{_pscheduler_test_libexec}/%{short}

%build
make \
     DESTDIR=$RPM_BUILD_ROOT/%{dest} \
     install



%post
pscheduler internal warmboot


%postun
pscheduler internal warmboot


%files
%defattr(-,root,root,-)
%license LICENSE
%{dest}
