Name:		model-config-m0
Summary:	A Model configuration
Version:	0.0.1
Release:	0
Group:		System/Configuration
License:	Apache License, Version 2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/config
cp -f model-config.xml %{buildroot}/etc/config/model-config.xml

%files
/etc/config/model-config.xml
%manifest model-config.manifest
