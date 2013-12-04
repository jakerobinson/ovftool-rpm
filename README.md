#ovftool-rpm
===========

RPM spec and instructions for building an RPM for OVFtool


## Creating an RPM in CentOS


1. Install rpmbuild: $`sudo yum install rpm-build `

2. Download and install the ovftool of your choice: [http://vmware.com/go/ovftool
](http://vmware.com/go/ovftool)

3. $`git clone git@github.com:VMop/ovftool-rpm.git`

4. Modify ovftool spec to match version

5. $`rpmbuild -bb ovftool-rpm/ovftool.spec`

6. Build will fail with an error. We just do this so it creates most of our directory structure for us. `
error: File not found: /home/vagrant/rpmbuild/BUILDROOT/ovftool-3.5.0-1.x86_64/usr/lib/vmware-ovftool
`

7. Create the rest of the directory structure by adding /usr/lib at the end since rpmbuild didn't do that for us: $`mkdir -p /home/vagrant/rpmbuild/BUILDROOT/ovftool-3.5.0-1.x86_64/usr/lib`

8. Copy the ovftool files to the build directory: $`cp -r /usr/lib/vmware-ovftool/ /home/vagrant/rpmbuild/BUILDROOT/ovftool-3.5.0-1.x86_64/usr/lib`

9. re-run rpmbuild: $`rpmbuild -bb ovftool-rpm/ovftool.spec`

10. The RPM will be located in `rpmbuild/RPMS/x86_64/ovftool-3.5.0-1.x86_64.rpm`