AUTOMAKE_OPTIONS = 1.6 foreign dist-bzip2
AUTOTOOL_VERSION=autoconf-2.52 automake-1.5 libtool-1.4.2

SUBDIRS = src
DIST_SUBDIRS = $(SUBDIRS) doc win32

EXTRA_DIST = $(PACKAGE).spec

rpm : dist-bzip2 $(PACKAGE).spec
	rpmbuild -ta $(PACKAGE)-$(VERSION).tar.bz2

upload www docs install-docs install-man3 \
manpages.ar htmpages.ar doc/manpages.ar doc/htmpages.ar :
	(cd doc && $(MAKE) `basename $@`)
