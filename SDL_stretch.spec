Summary: SDL_stretch - Stretch Functions For The Simple DirectMedia Layer
Name: SDL_stretch
Version: 0.3.1
Release: 1.02
Source0: %{name}-%{version}.tar.bz2
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot

URL: http://sdl-stretch.sf.net
Distribution: Original
Packager:  "Guido U. Draheim" <guidod@gmx.de>

Provides: SDL_stretch = %version
Provides: SDL_stretch0 = %version
Provides: SDL_stretch0.3 = %version
Provides: libSDL_stretch = %version
Requires: SDL >= 1.2
BuildRequires: SDL-devel >= 1.2

%description
Providing stretch and blit routines for SDL surfaces.

These are optimized for speed including lots of assembler parts
in the general routines and dynamic cpu native code generation
for applications to compile specialized stretch-and-blit routines
at runtime.

%package devel
Summary: SDL_stretch - Stretch Functions For SDL - Headers and Manpages
Group: Development/Libraries
Provides: SDL_stretch-devel = %version
Provides: SDL_stretch0-devel = %version
Provides: SDL_stretch0.3-devel = %version
Provides: libSDL_stretch-devel = %version
Requires: SDL_stretch = %version
Requires: SDL-devel >= 1.2

%description devel
While hacking on UAE (the unix amiga emulator) I did develop a few
stretching routines. I have been asking on the SDL mailing list for any
prior art but it seems that no one did wrap such routines into a
library part that can be reused everywhere. Other projects are
just game SDKs which tend to wrap such routines it into their
own framework - instead of using vanilla SDL surface. Also, there
are only rare pieces of assembler optimized routines. I took some
of these as hints and created my own set of highly optimized routines
pumped up with assembler - stretch-and-blit routines for SDL on steroids.

%package doc
Summary: SDL_stretch - Stretch Functions For SDL - Html Pages
Group: Development/Libraries
BuildRequires: python
BuildRequires: xmlto

%description doc
Providing stretch and blit routines for SDL surfaces.
Here are the Html Pages as they can be seen on %URL

%prep
%setup -q
CFLAGS="$RPM_OPT_CFLAGS" \
sh configure \
--prefix=%_prefix \
--libdir=%_libdir

%build
make
make docs

%install
rm -rf %buildroot
mkdir %buildroot
make install DESTDIR=%buildroot
make install-docs DESTDIR=%buildroot

%if %{_vendor} == suse
(cd %buildroot%_libdir/%name; for i in *.so*; do mv $i ..; ln -s ../$i .; done)
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
 %_libdir/*.so.*

%files devel
%defattr(-,root,root)
 %_libdir/*.so
 %_libdir/*.a
 %_libdir/*.la
 %_libdir/pkgconfig/*
 %_includedir/*
 %_datadir/man/man3/*
%dir %_libdir/%name
 %_libdir/%name/*

%files doc
%defattr(-,root,root)
 %_datadir/doc/*

%changelog

# end of file
* Sun Feb 22 2009 Guido Draheim <guidod-2003-@gmx.de> 1.02
+ fixing stuff for opensuse policies - e.g. introducing secondary library
  to defeat the "shlib-policy-name-error (Badness: 10000)" failure; and
  introducing post/postun with the usual ldconfig call for library install.
* Sat Feb 21 2009 Guido Draheim <guidod-2003-@gmx.de> 1.01
+ rename BuildRequires to opensuse 11.0 "SDL" for buildserver usage
