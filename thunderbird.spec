Name     : thunderbird
Version  : 140.0
Release  : 120
URL      : https://archive.mozilla.org/pub/thunderbird/releases/140.0/linux-x86_64/en-US/thunderbird-140.0.tar.xz
Source0  : https://archive.mozilla.org/pub/thunderbird/releases/140.0/linux-x86_64/en-US/thunderbird-140.0.tar.xz
Source1  : https://archive.mozilla.org/pub/thunderbird/releases/140.0/source/thunderbird-140.0.source.tar.xz
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

# Install icons
tar xf %{SOURCE0} thunderbird/chrome/icons/default/default16.png --xform='s,^.+/,,x'
install -D -m 0644 default16.png %{buildroot}/usr/share/icons/hicolor/16x16/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default22.png --xform='s,^.+/,,x'
install -D -m 0644 default16.png %{buildroot}/usr/share/icons/hicolor/22x22/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default24.png --xform='s,^.+/,,x'
install -D -m 0644 default16.png %{buildroot}/usr/share/icons/hicolor/24x24/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default32.png --xform='s,^.+/,,x'
install -D -m 0644 default32.png %{buildroot}/usr/share/icons/hicolor/32x32/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default48.png --xform='s,^.+/,,x'
install -D -m 0644 default48.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default64.png --xform='s,^.+/,,x'
install -D -m 0644 default64.png %{buildroot}/usr/share/icons/hicolor/64x64/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default128.png --xform='s,^.+/,,x'
install -D -m 0644 default128.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/thunderbird.png

tar xf %{SOURCE0} thunderbird/chrome/icons/default/default256.png --xform='s,^.+/,,x'
install -D -m 0644 default128.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/thunderbird.png

# Install stub
mkdir -p  %{buildroot}/usr/share/thunderbird-stub/
case %{SOURCE0} in
  *.tar.bz2)
    bunzip2 -c %{SOURCE0} > %{buildroot}/usr/share/thunderbird-stub/thunderbird-%{version}.tar
    ;;
  *.tar.xz)
    xz -d -c %{SOURCE0} > %{buildroot}/usr/share/thunderbird-stub/thunderbird-%{version}.tar
    ;;
esac
zstd -z --rm -19 --rsyncable %{buildroot}/usr/share/thunderbird-stub/thunderbird-%{version}.tar

# Desktop launcher
install -D -m 00644 %{SOURCE2} %{buildroot}/usr/share/applications/thunderbird.desktop

# Binwrapper - extracts and sets up thunderbird, or passes through, as appropriate
install -D -m 00755 %{SOURCE3} %{buildroot}/usr/bin/thunderbird

# Ensure the versioning is consistent - centralise this stuff.
sed -i %{buildroot}/usr/bin/thunderbird -e 's/\#\#VERSION\#\#/%{version}/g'

%files
%defattr(-,root,root,-)
/usr/bin/thunderbird
/usr/share/thunderbird-stub/thunderbird-%{version}.tar.zst
/usr/share/applications/thunderbird.desktop
/usr/share/icons/hicolor/16x16/apps/thunderbird.png
/usr/share/icons/hicolor/22x22/apps/thunderbird.png
/usr/share/icons/hicolor/24x24/apps/thunderbird.png
/usr/share/icons/hicolor/32x32/apps/thunderbird.png
/usr/share/icons/hicolor/48x48/apps/thunderbird.png
/usr/share/icons/hicolor/64x64/apps/thunderbird.png
/usr/share/icons/hicolor/128x128/apps/thunderbird.png
/usr/share/icons/hicolor/256x256/apps/thunderbird.png
