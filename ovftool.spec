Summary: VMware OVFTool
Name: VMware-ovftool
Version: 3.5.0
Release: 1
Distribution: lin
Group: VMware/OVFTool
License: VMware
Source: %{expand:%%(pwd)}
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-%{release}
%define _rpmfilename %{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}-%%{DISTRIBUTION}.%%{ARCH}.rpm

%description
VMware OVFTool

%post
ln -sf /usr/lib/vmware-ovftool/ovftool /usr/bin/ovftool

%preun
rm -f /usr/bin/ovftool

%files
/usr/lib/vmware-ovftool/
