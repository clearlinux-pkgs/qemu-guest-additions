#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3353C9CEF108B584 (mdroth@utexas.edu)
#
Name     : qemu-guest-additions
Version  : 7.2.0
Release  : 137
URL      : https://download.qemu.org/qemu-7.2.0.tar.xz
Source0  : https://download.qemu.org/qemu-7.2.0.tar.xz
Source1  : qemu-guest-agent.service
Source2  : https://download.qemu.org/qemu-7.2.0.tar.xz.sig
Summary  : OpenBIOS development utilities
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-2-Clause-Patent BSD-3-Clause BSD-4-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT OpenSSL
Requires: qemu-guest-additions-autostart = %{version}-%{release}
Requires: qemu-guest-additions-bin = %{version}-%{release}
Requires: qemu-guest-additions-license = %{version}-%{release}
Requires: qemu-guest-additions-man = %{version}-%{release}
Requires: qemu-guest-additions-services = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : ceph-dev
BuildRequires : flex
BuildRequires : fuse-dev
BuildRequires : glib-dev
BuildRequires : gtk3-dev
BuildRequires : libaio-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgcrypt-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libseccomp-dev
BuildRequires : libssh-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : numactl-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(capstone)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(glusterfs-api)
BuildRequires : pkgconfig(gmp)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gvnc-1.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libbpf)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdaxctl)
BuildRequires : pkgconfig(libiscsi)
BuildRequires : pkgconfig(libkeyutils)
BuildRequires : pkgconfig(libpmem)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(liburing)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(virglrenderer)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi(wheel)
BuildRequires : pypi-sphinx
BuildRequires : snappy-dev
BuildRequires : spice
BuildRequires : spice-dev
BuildRequires : spice-protocol
BuildRequires : usbredir-dev
BuildRequires : util-linux-dev
BuildRequires : vte-dev
BuildRequires : zlib-dev
Patch1: 0001-Allow-unknown-options-in-configure-script.patch
Patch2: 0002-Set-default-number-of-sockets-to-1.patch
Patch3: 0003-Use-run-lock.patch

%description
This package contains the OpenBIOS development utilities.

There are
* toke - an IEEE 1275-1994 compliant FCode tokenizer
* detok - an IEEE 1275-1994 compliant FCode detokenizer
* paflof - a forth kernel running in user space
* an fcode bytecode evaluator running in paflof

See /usr/share/doc/packages/openbios for details and examples.

Authors:
--------
    Stefan Reinauer <stepan@openbios.net>
    Segher Boessenkool <segher@openbios.net>

%package autostart
Summary: autostart components for the qemu-guest-additions package.
Group: Default

%description autostart
autostart components for the qemu-guest-additions package.


%package bin
Summary: bin components for the qemu-guest-additions package.
Group: Binaries
Requires: qemu-guest-additions-license = %{version}-%{release}
Requires: qemu-guest-additions-services = %{version}-%{release}

%description bin
bin components for the qemu-guest-additions package.


%package license
Summary: license components for the qemu-guest-additions package.
Group: Default

%description license
license components for the qemu-guest-additions package.


%package man
Summary: man components for the qemu-guest-additions package.
Group: Default

%description man
man components for the qemu-guest-additions package.


%package services
Summary: services components for the qemu-guest-additions package.
Group: Systemd services

%description services
services components for the qemu-guest-additions package.


%prep
%setup -q -n qemu-7.2.0
cd %{_builddir}/qemu-7.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671131404
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-sdl \
--enable-vnc \
--enable-gtk \
--enable-kvm \
--disable-strip \
--target-list='i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user' \
--enable-spice \
--enable-rbd \
--extra-cflags="-O3" \
--enable-attr \
--enable-cap-ng \
--enable-virtfs \
--enable-vhost-net \
--enable-usb-redir \
--python=/usr/bin/python \
--enable-seccomp \
--enable-linux-aio
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1671131404
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qemu-guest-additions
cp %{_builddir}/qemu-%{version}/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80 || :
cp %{_builddir}/qemu-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/qemu-guest-additions/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/qemu-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c690b05ff6431c277b59784e95169e0e0528a983 || :
cp %{_builddir}/qemu-%{version}/dtc/README.license %{buildroot}/usr/share/package-licenses/qemu-guest-additions/a6759c569917866b44961c88629ae4f3f07ea686 || :
cp %{_builddir}/qemu-%{version}/meson/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/meson/packaging/License.rtf %{buildroot}/usr/share/package-licenses/qemu-guest-additions/00dcd169768382e0b6a13d0d110266754fedb62b || :
cp %{_builddir}/qemu-%{version}/meson/packaging/macpages/English.lproj/license.html %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ed59b8ab4e260b632c935598bf0d1472e4e2dbdf || :
cp %{_builddir}/qemu-%{version}/roms/QemuMacDrivers/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80 || :
cp %{_builddir}/qemu-%{version}/roms/SLOF/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e1f0ad62e4850a19b1f56b821f37fccbf84ec191 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/.pytool/Plugin/LicenseCheck/LicenseCheck_plug_in.yaml %{buildroot}/usr/share/package-licenses/qemu-guest-additions/f1a6a8f321d20cb5fbec859a848bff49ad31de69 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/BaseTools/Source/C/BrotliCompress/brotli/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c045813a6c514f2d30d60a07c6aaf3603850e608 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/607e96d7bc75d9f884a8e210d276cca4006e0753 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/external/perl/Text-Template-1.46/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ab8577d3eb0eedf3f98004e381a9cee30e7224e1 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/License-History.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/1b5c06f43bf6e2039065b681398f6b99a4d552f8 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/License.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/7fc5c71d1c403b07043376504d62f2ac73a75313 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/brotli/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c045813a6c514f2d30d60a07c6aaf3603850e608 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/MdeModulePkg/Universal/RegularExpressionDxe/oniguruma/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/fa8fca82526cc5174bb568accab23c3eb9c049ea || :
cp %{_builddir}/qemu-%{version}/roms/edk2/OvmfPkg/Bhyve/License.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/6b5c7cbcd561ea8f6bba9dd24393f995c1a006e9 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/OvmfPkg/License.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c9c057d4dc70e7a834d80b762663ca01a852ed13 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/RedfishPkg/Library/JsonLib/jansson/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/fa82ae23fff791a399cb3c72b59fe7199e989652 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/doc/that_style/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/86b52f0f7e15225010495c0b221b79ef0dc1a90d || :
cp %{_builddir}/qemu-%{version}/roms/ipxe/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/cedc99c80ddc135681756e652d55c72d89ebdfe7 || :
cp %{_builddir}/qemu-%{version}/roms/ipxe/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/qemu-guest-additions/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qemu-%{version}/roms/ipxe/src/include/ipxe/efi/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ca46b2cea92edc93654b11c06c0073ec1a2e50e8 || :
cp %{_builddir}/qemu-%{version}/roms/openbios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b || :
cp %{_builddir}/qemu-%{version}/roms/openbios/Documentation/kernel/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e9b568889ca9075b505c509f7a877a723cc9a4b0 || :
cp %{_builddir}/qemu-%{version}/roms/openbios/utils/devbios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/7475b0da13789cd598fe0703f5337d37dd8b0b95 || :
cp %{_builddir}/qemu-%{version}/roms/opensbi/COPYING.BSD %{buildroot}/usr/share/package-licenses/qemu-guest-additions/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f || :
cp %{_builddir}/qemu-%{version}/roms/qboot/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/30a6e0a424471d8ac874b5616dd5a18c45fd6046 || :
cp %{_builddir}/qemu-%{version}/roms/qemu-palcode/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80 || :
cp %{_builddir}/qemu-%{version}/roms/seabios-hppa/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qemu-%{version}/roms/seabios-hppa/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
cp %{_builddir}/qemu-%{version}/roms/seabios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qemu-%{version}/roms/seabios/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
cp %{_builddir}/qemu-%{version}/roms/sgabios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/heap/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/libstb/crypto/mbedtls/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/4d6c5af1a9cc4eaab3b93353fc166d8e29c150c6 || :
cp %{_builddir}/qemu-%{version}/roms/u-boot-sam460ex/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/11bb99995c221415712bb5a6d6c0898f02936feb || :
cp %{_builddir}/qemu-%{version}/roms/u-boot-sam460ex/board/ACube/bios_emulator/scitech/src/x86emu/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3f226d574cd9547c3e4d934bb1ac4be3601a9782 || :
cp %{_builddir}/qemu-%{version}/roms/u-boot-sam460ex/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2f02ed32418afe8cc25f30f269c63085bafe44f7 || :
cp %{_builddir}/qemu-%{version}/roms/u-boot/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2f02ed32418afe8cc25f30f269c63085bafe44f7 || :
cp %{_builddir}/qemu-%{version}/roms/vbootrom/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/subprojects/libvfio-user/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/36fb901125ffda91bbec1cab3efc5c9f8f2d15a7 || :
cp %{_builddir}/qemu-%{version}/tests/fp/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6 || :
cp %{_builddir}/qemu-%{version}/tests/fp/berkeley-testfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec || :
cp %{_builddir}/qemu-%{version}/tests/lcitool/libvirt-ci/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qemu-%{version}/tests/uefi-test-tools/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/234e74aeab28f7faad2baccf1a3f943b36ab895e || :
cp %{_builddir}/qemu-%{version}/ui/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/qemu-%{version}/ui/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qemu-guest-additions/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/qemu-guest-agent.service
## Remove excluded files
rm -f %{buildroot}*/usr/bin/elf2dmp
rm -f %{buildroot}*/usr/bin/ivshmem-client
rm -f %{buildroot}*/usr/bin/ivshmem-server
rm -f %{buildroot}*/usr/bin/qemu-edid
rm -f %{buildroot}*/usr/bin/qemu-i386
rm -f %{buildroot}*/usr/bin/qemu-img
rm -f %{buildroot}*/usr/bin/qemu-io
rm -f %{buildroot}*/usr/bin/qemu-keymap
rm -f %{buildroot}*/usr/bin/qemu-nbd
rm -f %{buildroot}*/usr/bin/qemu-pr-helper
rm -f %{buildroot}*/usr/bin/qemu-storage-daemon
rm -f %{buildroot}*/usr/bin/qemu-system-i386
rm -f %{buildroot}*/usr/bin/qemu-system-x86_64
rm -f %{buildroot}*/usr/bin/qemu-x86_64
rm -f %{buildroot}*/usr/bin/virtfs-proxy-helper
rm -f %{buildroot}*/usr/include/qemu-plugin.h
rm -f %{buildroot}*/usr/libexec/qemu-bridge-helper
rm -f %{buildroot}*/usr/libexec/qemu-pr-helper
rm -f %{buildroot}*/usr/libexec/vhost-user-gpu
rm -f %{buildroot}*/usr/libexec/virtfs-proxy-helper
rm -f %{buildroot}*/usr/libexec/virtiofsd
rm -f %{buildroot}*/usr/share/applications/qemu.desktop
rm -f %{buildroot}*/usr/share/man/man1/qemu-img.1
rm -f %{buildroot}*/usr/share/man/man1/qemu-storage-daemon.1
rm -f %{buildroot}*/usr/share/man/man7/qemu-storage-daemon-qmp-ref.7
rm -f %{buildroot}*/usr/share/man/man1/qemu.1
rm -f %{buildroot}*/usr/share/man/man1/virtfs-proxy-helper.1
rm -f %{buildroot}*/usr/share/man/man1/virtiofsd.1
rm -f %{buildroot}*/usr/share/man/man7/qemu-block-drivers.7
rm -f %{buildroot}*/usr/share/man/man7/qemu-cpu-models.7
rm -f %{buildroot}*/usr/share/man/man7/qemu-qmp-ref.7
rm -f %{buildroot}*/usr/share/man/man8/qemu-nbd.8
rm -f %{buildroot}*/usr/share/man/man8/qemu-pr-helper.8
## install_append content
rm -rvf %{buildroot}/usr/share/doc
rm -rvf %{buildroot}/usr/share/icons
rm -rvf %{buildroot}/usr/share/locale
rm -rvf %{buildroot}/usr/share/qemu
mkdir -pv %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sv ../qemu-guest-agent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/qemu-guest-agent.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/qemu-guest-agent.service

%files bin
%defattr(-,root,root,-)
/usr/bin/qemu-ga

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qemu-guest-additions/00dcd169768382e0b6a13d0d110266754fedb62b
/usr/share/package-licenses/qemu-guest-additions/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/qemu-guest-additions/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/qemu-guest-additions/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f
/usr/share/package-licenses/qemu-guest-additions/11bb99995c221415712bb5a6d6c0898f02936feb
/usr/share/package-licenses/qemu-guest-additions/1b5c06f43bf6e2039065b681398f6b99a4d552f8
/usr/share/package-licenses/qemu-guest-additions/234e74aeab28f7faad2baccf1a3f943b36ab895e
/usr/share/package-licenses/qemu-guest-additions/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80
/usr/share/package-licenses/qemu-guest-additions/2f02ed32418afe8cc25f30f269c63085bafe44f7
/usr/share/package-licenses/qemu-guest-additions/30a6e0a424471d8ac874b5616dd5a18c45fd6046
/usr/share/package-licenses/qemu-guest-additions/36fb901125ffda91bbec1cab3efc5c9f8f2d15a7
/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/qemu-guest-additions/3f226d574cd9547c3e4d934bb1ac4be3601a9782
/usr/share/package-licenses/qemu-guest-additions/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qemu-guest-additions/4d6c5af1a9cc4eaab3b93353fc166d8e29c150c6
/usr/share/package-licenses/qemu-guest-additions/607e96d7bc75d9f884a8e210d276cca4006e0753
/usr/share/package-licenses/qemu-guest-additions/6b5c7cbcd561ea8f6bba9dd24393f995c1a006e9
/usr/share/package-licenses/qemu-guest-additions/7475b0da13789cd598fe0703f5337d37dd8b0b95
/usr/share/package-licenses/qemu-guest-additions/7fc5c71d1c403b07043376504d62f2ac73a75313
/usr/share/package-licenses/qemu-guest-additions/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qemu-guest-additions/86b52f0f7e15225010495c0b221b79ef0dc1a90d
/usr/share/package-licenses/qemu-guest-additions/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b
/usr/share/package-licenses/qemu-guest-additions/a6759c569917866b44961c88629ae4f3f07ea686
/usr/share/package-licenses/qemu-guest-additions/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
/usr/share/package-licenses/qemu-guest-additions/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec
/usr/share/package-licenses/qemu-guest-additions/c045813a6c514f2d30d60a07c6aaf3603850e608
/usr/share/package-licenses/qemu-guest-additions/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
/usr/share/package-licenses/qemu-guest-additions/c690b05ff6431c277b59784e95169e0e0528a983
/usr/share/package-licenses/qemu-guest-additions/c9c057d4dc70e7a834d80b762663ca01a852ed13
/usr/share/package-licenses/qemu-guest-additions/ca46b2cea92edc93654b11c06c0073ec1a2e50e8
/usr/share/package-licenses/qemu-guest-additions/cedc99c80ddc135681756e652d55c72d89ebdfe7
/usr/share/package-licenses/qemu-guest-additions/e1f0ad62e4850a19b1f56b821f37fccbf84ec191
/usr/share/package-licenses/qemu-guest-additions/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
/usr/share/package-licenses/qemu-guest-additions/e9b568889ca9075b505c509f7a877a723cc9a4b0
/usr/share/package-licenses/qemu-guest-additions/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
/usr/share/package-licenses/qemu-guest-additions/ed59b8ab4e260b632c935598bf0d1472e4e2dbdf
/usr/share/package-licenses/qemu-guest-additions/f1a6a8f321d20cb5fbec859a848bff49ad31de69
/usr/share/package-licenses/qemu-guest-additions/fa82ae23fff791a399cb3c72b59fe7199e989652
/usr/share/package-licenses/qemu-guest-additions/fa8fca82526cc5174bb568accab23c3eb9c049ea
/usr/share/package-licenses/qemu-guest-additions/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/qemu-ga-ref.7
/usr/share/man/man8/qemu-ga.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/qemu-guest-agent.service
/usr/lib/systemd/system/qemu-guest-agent.service
