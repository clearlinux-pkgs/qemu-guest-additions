#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3353C9CEF108B584 (mdroth@utexas.edu)
#
Name     : qemu-guest-additions
Version  : 5.2.0
Release  : 122
URL      : https://download.qemu.org/qemu-5.2.0.tar.xz
Source0  : https://download.qemu.org/qemu-5.2.0.tar.xz
Source1  : qemu-guest-agent.service
Source2  : https://download.qemu.org/qemu-5.2.0.tar.xz.sig
Summary  : A lightweight multi-platform, multi-architecture disassembly framework
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-2-Clause-Patent BSD-3-Clause BSD-4-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT NCSA OpenSSL
Requires: qemu-guest-additions-autostart = %{version}-%{release}
Requires: qemu-guest-additions-bin = %{version}-%{release}
Requires: qemu-guest-additions-license = %{version}-%{release}
Requires: qemu-guest-additions-man = %{version}-%{release}
Requires: qemu-guest-additions-services = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : ceph-dev
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : gtk3-dev
BuildRequires : libaio-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libseccomp-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : numactl-dev
BuildRequires : pkgconfig(capstone)
BuildRequires : pkgconfig(libkeyutils)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : snappy-dev
BuildRequires : spice
BuildRequires : spice-dev
BuildRequires : spice-protocol
BuildRequires : usbredir-dev
BuildRequires : util-linux-dev
BuildRequires : zlib-dev
Patch1: 0001-Allow-unknown-options-in-configure-script.patch
Patch2: 0002-Set-default-number-of-sockets-to-1.patch
Patch3: 0003-Use-run-lock.patch
Patch4: 0004-build-no-pie-is-no-functional-linker-flag.patch

%description
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.

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
%setup -q -n qemu-5.2.0
cd %{_builddir}/qemu-5.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614636628
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
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
export SOURCE_DATE_EPOCH=1614636628
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qemu-guest-additions
cp %{_builddir}/qemu-5.2.0/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80
cp %{_builddir}/qemu-5.2.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/qemu-guest-additions/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/qemu-5.2.0/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c690b05ff6431c277b59784e95169e0e0528a983
cp %{_builddir}/qemu-5.2.0/capstone/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qemu-guest-additions/861af24907e399e873920dbbff1ea1dd73a9ba35
cp %{_builddir}/qemu-5.2.0/capstone/LICENSE_LLVM.TXT %{buildroot}/usr/share/package-licenses/qemu-guest-additions/afc034c0ae47cbd47a99c6c5992d846511bb33ad
cp %{_builddir}/qemu-5.2.0/capstone/bindings/python/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qemu-guest-additions/861af24907e399e873920dbbff1ea1dd73a9ba35
cp %{_builddir}/qemu-5.2.0/capstone/suite/regress/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/7de9d56eea42f5bbbba6fff880d912f2c9c3a45d
cp %{_builddir}/qemu-5.2.0/disas/libvixl/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/25383eb1c76eae5993e92a1cf2b75d58e599bbf5
cp %{_builddir}/qemu-5.2.0/dtc/README.license %{buildroot}/usr/share/package-licenses/qemu-guest-additions/a6759c569917866b44961c88629ae4f3f07ea686
cp %{_builddir}/qemu-5.2.0/meson/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-5.2.0/meson/msi/License.rtf %{buildroot}/usr/share/package-licenses/qemu-guest-additions/00dcd169768382e0b6a13d0d110266754fedb62b
cp %{_builddir}/qemu-5.2.0/roms/QemuMacDrivers/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80
cp %{_builddir}/qemu-5.2.0/roms/SLOF/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e1f0ad62e4850a19b1f56b821f37fccbf84ec191
cp %{_builddir}/qemu-5.2.0/roms/edk2/.pytool/Plugin/LicenseCheck/LicenseCheck_plug_in.yaml %{buildroot}/usr/share/package-licenses/qemu-guest-additions/f1a6a8f321d20cb5fbec859a848bff49ad31de69
cp %{_builddir}/qemu-5.2.0/roms/edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
cp %{_builddir}/qemu-5.2.0/roms/edk2/BaseTools/Source/C/BrotliCompress/brotli/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/qemu-5.2.0/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/607e96d7bc75d9f884a8e210d276cca4006e0753
cp %{_builddir}/qemu-5.2.0/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/external/perl/Text-Template-1.46/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
cp %{_builddir}/qemu-5.2.0/roms/edk2/License-History.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/1b5c06f43bf6e2039065b681398f6b99a4d552f8
cp %{_builddir}/qemu-5.2.0/roms/edk2/License.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/7fc5c71d1c403b07043376504d62f2ac73a75313
cp %{_builddir}/qemu-5.2.0/roms/edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/brotli/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/qemu-5.2.0/roms/edk2/MdeModulePkg/Universal/RegularExpressionDxe/oniguruma/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/fa8fca82526cc5174bb568accab23c3eb9c049ea
cp %{_builddir}/qemu-5.2.0/roms/edk2/OvmfPkg/Bhyve/License.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/6b5c7cbcd561ea8f6bba9dd24393f995c1a006e9
cp %{_builddir}/qemu-5.2.0/roms/edk2/OvmfPkg/License.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c9c057d4dc70e7a834d80b762663ca01a852ed13
cp %{_builddir}/qemu-5.2.0/roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-5.2.0/roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/qemu-5.2.0/roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/doc/that_style/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/86b52f0f7e15225010495c0b221b79ef0dc1a90d
cp %{_builddir}/qemu-5.2.0/roms/ipxe/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/cedc99c80ddc135681756e652d55c72d89ebdfe7
cp %{_builddir}/qemu-5.2.0/roms/ipxe/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/qemu-guest-additions/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qemu-5.2.0/roms/ipxe/src/include/ipxe/efi/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ca46b2cea92edc93654b11c06c0073ec1a2e50e8
cp %{_builddir}/qemu-5.2.0/roms/openbios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b
cp %{_builddir}/qemu-5.2.0/roms/openbios/Documentation/kernel/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e9b568889ca9075b505c509f7a877a723cc9a4b0
cp %{_builddir}/qemu-5.2.0/roms/openbios/utils/devbios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/7475b0da13789cd598fe0703f5337d37dd8b0b95
cp %{_builddir}/qemu-5.2.0/roms/opensbi/COPYING.BSD %{buildroot}/usr/share/package-licenses/qemu-guest-additions/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f
cp %{_builddir}/qemu-5.2.0/roms/qboot/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/30a6e0a424471d8ac874b5616dd5a18c45fd6046
cp %{_builddir}/qemu-5.2.0/roms/qemu-palcode/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80
cp %{_builddir}/qemu-5.2.0/roms/seabios-hppa/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qemu-5.2.0/roms/seabios-hppa/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/qemu-5.2.0/roms/seabios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qemu-5.2.0/roms/seabios/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu-guest-additions/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/qemu-5.2.0/roms/sgabios/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-5.2.0/roms/skiboot/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/skiboot/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-5.2.0/roms/u-boot-sam460ex/COPYING %{buildroot}/usr/share/package-licenses/qemu-guest-additions/11bb99995c221415712bb5a6d6c0898f02936feb
cp %{_builddir}/qemu-5.2.0/roms/u-boot-sam460ex/board/ACube/bios_emulator/scitech/src/x86emu/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/3f226d574cd9547c3e4d934bb1ac4be3601a9782
cp %{_builddir}/qemu-5.2.0/roms/u-boot-sam460ex/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2f02ed32418afe8cc25f30f269c63085bafe44f7
cp %{_builddir}/qemu-5.2.0/roms/u-boot/cmd/license.c %{buildroot}/usr/share/package-licenses/qemu-guest-additions/33e557c1f30d0d1f1f585cb49686b8c13e47ba83
cp %{_builddir}/qemu-5.2.0/roms/u-boot/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2f02ed32418afe8cc25f30f269c63085bafe44f7
cp %{_builddir}/qemu-5.2.0/roms/vbootrom/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-5.2.0/slirp/COPYRIGHT %{buildroot}/usr/share/package-licenses/qemu-guest-additions/051935530e6be28baed83b2aafe66ee5b347d656
cp %{_builddir}/qemu-5.2.0/tests/fp/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
cp %{_builddir}/qemu-5.2.0/tests/fp/berkeley-testfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu-guest-additions/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec
cp %{_builddir}/qemu-5.2.0/tests/uefi-test-tools/LICENSE %{buildroot}/usr/share/package-licenses/qemu-guest-additions/234e74aeab28f7faad2baccf1a3f943b36ab895e
cp %{_builddir}/qemu-5.2.0/ui/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/qemu-guest-additions/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
cp %{_builddir}/qemu-5.2.0/ui/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qemu-guest-additions/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/qemu-guest-agent.service
## Remove excluded files
rm -f %{buildroot}/usr/bin/ivshmem-client
rm -f %{buildroot}/usr/bin/ivshmem-server
rm -f %{buildroot}/usr/bin/qemu-edid
rm -f %{buildroot}/usr/bin/qemu-i386
rm -f %{buildroot}/usr/bin/qemu-img
rm -f %{buildroot}/usr/bin/qemu-io
rm -f %{buildroot}/usr/bin/qemu-keymap
rm -f %{buildroot}/usr/bin/qemu-nbd
rm -f %{buildroot}/usr/bin/qemu-pr-helper
rm -f %{buildroot}/usr/bin/qemu-storage-daemon
rm -f %{buildroot}/usr/bin/qemu-system-i386
rm -f %{buildroot}/usr/bin/qemu-system-x86_64
rm -f %{buildroot}/usr/bin/qemu-x86_64
rm -f %{buildroot}/usr/bin/virtfs-proxy-helper
rm -f %{buildroot}/usr/libexec/qemu-bridge-helper
rm -f %{buildroot}/usr/libexec/qemu-pr-helper
rm -f %{buildroot}/usr/libexec/virtfs-proxy-helper
rm -f %{buildroot}/usr/libexec/virtiofsd
rm -f %{buildroot}/usr/share/applications/qemu.desktop
rm -f %{buildroot}/usr/share/man/man1/qemu-img.1
rm -f %{buildroot}/usr/share/man/man1/qemu.1
rm -f %{buildroot}/usr/share/man/man1/virtfs-proxy-helper.1
rm -f %{buildroot}/usr/share/man/man1/virtiofsd.1
rm -f %{buildroot}/usr/share/man/man7/qemu-block-drivers.7
rm -f %{buildroot}/usr/share/man/man7/qemu-cpu-models.7
rm -f %{buildroot}/usr/share/man/man7/qemu-qmp-ref.7
rm -f %{buildroot}/usr/share/man/man8/qemu-nbd.8
rm -f %{buildroot}/usr/share/man/man8/qemu-pr-helper.8
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
/usr/share/package-licenses/qemu-guest-additions/051935530e6be28baed83b2aafe66ee5b347d656
/usr/share/package-licenses/qemu-guest-additions/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/qemu-guest-additions/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f
/usr/share/package-licenses/qemu-guest-additions/11bb99995c221415712bb5a6d6c0898f02936feb
/usr/share/package-licenses/qemu-guest-additions/1b5c06f43bf6e2039065b681398f6b99a4d552f8
/usr/share/package-licenses/qemu-guest-additions/234e74aeab28f7faad2baccf1a3f943b36ab895e
/usr/share/package-licenses/qemu-guest-additions/25383eb1c76eae5993e92a1cf2b75d58e599bbf5
/usr/share/package-licenses/qemu-guest-additions/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/qemu-guest-additions/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qemu-guest-additions/2b9d60c2972b476384af9900276837ac81954e80
/usr/share/package-licenses/qemu-guest-additions/2f02ed32418afe8cc25f30f269c63085bafe44f7
/usr/share/package-licenses/qemu-guest-additions/30a6e0a424471d8ac874b5616dd5a18c45fd6046
/usr/share/package-licenses/qemu-guest-additions/33e557c1f30d0d1f1f585cb49686b8c13e47ba83
/usr/share/package-licenses/qemu-guest-additions/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/qemu-guest-additions/3f226d574cd9547c3e4d934bb1ac4be3601a9782
/usr/share/package-licenses/qemu-guest-additions/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qemu-guest-additions/607e96d7bc75d9f884a8e210d276cca4006e0753
/usr/share/package-licenses/qemu-guest-additions/6b5c7cbcd561ea8f6bba9dd24393f995c1a006e9
/usr/share/package-licenses/qemu-guest-additions/7475b0da13789cd598fe0703f5337d37dd8b0b95
/usr/share/package-licenses/qemu-guest-additions/7de9d56eea42f5bbbba6fff880d912f2c9c3a45d
/usr/share/package-licenses/qemu-guest-additions/7fc5c71d1c403b07043376504d62f2ac73a75313
/usr/share/package-licenses/qemu-guest-additions/861af24907e399e873920dbbff1ea1dd73a9ba35
/usr/share/package-licenses/qemu-guest-additions/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qemu-guest-additions/86b52f0f7e15225010495c0b221b79ef0dc1a90d
/usr/share/package-licenses/qemu-guest-additions/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b
/usr/share/package-licenses/qemu-guest-additions/a6759c569917866b44961c88629ae4f3f07ea686
/usr/share/package-licenses/qemu-guest-additions/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
/usr/share/package-licenses/qemu-guest-additions/afc034c0ae47cbd47a99c6c5992d846511bb33ad
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
/usr/share/package-licenses/qemu-guest-additions/f1a6a8f321d20cb5fbec859a848bff49ad31de69
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
