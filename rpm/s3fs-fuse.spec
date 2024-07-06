# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       s3fs-fuse

# >> macros
# << macros

Summary:    mount an S3 bucket via FUSE
Version:    1.94
Release:    0
Group:      Applications
License:    GPLv2
URL:        https://github.com/s3fs-fuse/s3fs-fuse
Source0:    %{name}-%{version}.tar.gz
Source100:  s3fs-fuse.yaml
Source101:  s3fs-fuse-rpmlintrc
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  curl-devel

%description
%{summary}.

s3fs allows Linux, macOS, and FreeBSD to mount an S3 bucket via FUSE
(Filesystem in Userspace)

To use with Backblaze B2, see
https://help.backblaze.com/hc/en-us/articles/360047773653-Using-S3FS-with-B2

e.g.
s3fs -f -s $mybucket $mntpt -o passwd_file=$pwdf -o url=https://s3.eu-central-003.backblazeb2.com«

%if "%{?vendor}" == "chum"
Title: S3FS
Type: console-application
PackagedBy: nephros
Categories:
 - System
 - Network
 - Filesystem
Custom:
  Repo: %{url}
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static

# >> build post
%make_build
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%make_install
# << install pre

# >> install post

# do not package documentation:
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_mandir}
# << install post

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
# >> files
# << files
