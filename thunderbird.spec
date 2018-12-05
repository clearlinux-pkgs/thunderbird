Name     : thunderbird
Version  : 60.3.3
Release  : 1
URL      : http://ftp.mozilla.org/pub/thunderbird/releases/60.3.3/linux-x86_64/en-US/thunderbird-60.3.3.tar.bz2
Source0  : http://ftp.mozilla.org/pub/thunderbird/releases/60.3.3/linux-x86_64/en-US/thunderbird-60.3.3.tar.bz2
Source1  : http://ftp.mozilla.org/pub/thunderbird/releases/60.3.3/source/thunderbird-60.3.3.source.tar.xz
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
mkdir -p  %{buildroot}/usr/share/thunderbird-stub/
bunzip2 -c %{SOURCE0} > %{buildroot}/usr/share/thunderbird-stub/thunderbird-%{version}.tar


# Desktop launcher
install -D -m 00644 %{SOURCE2} %{buildroot}/usr/share/applications/thunderbird.desktop

# Binwrapper - extracts and sets up thunderbird, or passes through, as appropriate
install -D -m 00755 %{SOURCE3} %{buildroot}/usr/bin/thunderbird

# Ensure the versioning is consistent - centralise this stuff.
sed -i %{buildroot}/usr/bin/thunderbird -e 's/\#\#VERSION\#\#/%{version}/g'

%files
%defattr(-,root,root,-)
/usr/bin/thunderbird
/usr/share/thunderbird-stub/thunderbird-%{version}.tar
/usr/share/applications/thunderbird.desktop
