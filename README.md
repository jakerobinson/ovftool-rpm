#ovftool-rpm
===========

RPM spec and instructions for building an RPM for OVFtool


## Creating an RPM in CentOS


1. Install rpmbuild: $`sudo yum install rpm-build `

2. Download and install the ovftool of your choice: [http://vmware.com/go/ovftool
](http://vmware.com/go/ovftool)

3. $`git clone git@github.com:VMop/ovftool-rpm.git`

4. Modify ovftool spec to match version and build

5. $`rpmbuild -bb ovftool-rpm/ovftool.spec`

6. Build will fail with an error. We just do this so it creates most of our directory structure for us, because we are lazy. `
error: File not found: /home/vagrant/rpmbuild/BUILDROOT/VMware-ovftool-3.5.0-1274719-lin.x86_64/usr/lib/vmware-ovftool
`

7. Copy and paste the directory structure into a mkdir command (excluding the vmware-ovftool directory): $`mkdir -p /home/vagrant/rpmbuild/BUILDROOT/VMware-ovftool-3.5.0-1274719-lin.x86_64/usr/lib`

8. Copy the ovftool files to the build directory: $`cp -r /usr/lib/vmware-ovftool/ /home/vagrant/rpmbuild/BUILDROOT/VMware-ovftool-3.5.0-1274719-lin.x86_64/usr/lib`

9. Re-run rpmbuild: $`rpmbuild -bb ovftool-rpm/ovftool.spec`

10. The RPM will be located in `rpmbuild/RPMS/x86_64/`

11. You can now install the RPM with `yum`, `rpm` or the `vmware-ovftool` puppet module