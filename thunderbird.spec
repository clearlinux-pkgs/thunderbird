Name     : thunderbird
Version  : 52.2.0
Release  : 1
URL      : http://ftp.mozilla.org/pub/thunderbird/releases/52.2.0/linux-x86_64/en-US/thunderbird-52.2.0.tar.bz2
Source0  : http://ftp.mozilla.org/pub/thunderbird/releases/52.2.0/linux-x86_64/en-US/thunderbird-52.2.0.tar.bz2
Source1  : http://ftp.mozilla.org/pub/thunderbird/releases/52.2.0/source/thunderbird-52.2.0.source.tar.bz2
Source2  : thunderbird.desktop
Source3  : thunderbird.sh
Summary  : Thunderbird mail client
Group    : Development/Tools
License  : GPL-2.0+ MPL-2.0
Requires : alsa-lib bzip2 tar

%description
Introduction
============
Stub package to assist with installation of Mozilla Thunderbird Email Client

%install
rm -rf %{buildroot}
install -D -m 00644 %{SOURCE0} %{buildroot}/usr/share/thunderbird-stub/thunderbird-%{version}.tar.bz2

# Desktop launcher
install -D -m 00644 %{SOURCE2} %{buildroot}/usr/share/applications/thunderbird.desktop

# Binwrapper - extracts and sets up thunderbird, or passes through, as appropriate
install -D -m 00755 %{SOURCE3} %{buildroot}/usr/bin/thunderbird

# Ensure the versioning is consistent - centralise this stuff.
sed -i %{buildroot}/usr/bin/thunderbird -e 's/\#\#VERSION\#\#/%{version}/g'

%files
%defattr(-,root,root,-)
/usr/bin/thunderbird
/usr/share/thunderbird-stub/thunderbird-%{version}.tar.bz2
/usr/share/applications/thunderbird.desktop
