Summary:	Marc's favorite clock
Summary(de):	Marcs Lieblingsuhr
Summary(fr):	Marc's favorite clock.
Summary(pl):	Ulubiony zegar Marca
Summary(tr):	Marc'�n g�zde saati
Name:		xdaliclock
Version:	2.14
Release:	3
Copyright:      MIT
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
URL:            http://www.jwz.org/xdaliclock/
Source:		ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Patch:		xdaliclock-shape-cycle.patch
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix		/usr/X11R6

%description
The xdaliclock program displays a digital clock; when a digit changes, it
"melts" into its new shape.

It can display in 12 or 24 hour modes, and displays the date when a mouse
button is held down.  It has two large fonts built into it, but it can animate
other fonts.

%description -l pl
Program xdaliclock wy�wietla cyfrowy zegar, w kt�rym zmieniaj�ce si� cyfry
p�ynnie przechodz� jedna w drug�.

Mo�e on wyswietla� czas w uk�adzie 12 i 24 godziny. Wy�wietla on tak�e dat�
kiedy przyci�nie si� przycisk myszki maj�c kursor nad okienkiem zegarka.
W program s� wbudowane dwa zestawy du�ych font�w ale mo�e on wy�wietla�
inne fonty.

%prep
%setup -q
%patch -p1

%build
xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir} \
	install install.man

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/X11/app-defaults/XDaliClock
%{_mandir}/man1/*

%changelog
* Sun Nov 15 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.13-1]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added pl translation,
- added URL field,
- added full %attr description in %files.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
