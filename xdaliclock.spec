Summary:     Marc's favorite clock
Summary(de): Marcs Lieblingsuhr
Summary(fr): Marc's favorite clock.
Summary(pl): Ulubiony zegar Marca
Summary(tr): Marc'ýn gözde saati
Name:        xdaliclock
Version:     2.13
Release:     1
Group:       X11/Utilities
Copyright:   MIT
Source:      ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
URL:         http://www.jwz.org/xdaliclock/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The xdaliclock program displays a digital clock; when a digit changes, it
"melts" into its new shape.

It can display in 12 or 24 hour modes, and displays the date when a mouse
button is held down.  It has two large fonts built into it, but it can animate
other fonts.

%description -l pl
Program xdaliclock Wy¶wietla cyfrowy zegar, w którym zmieniaj±ce siê cyfry
p³ynnie przechodz± jedna w drug±,

Mo¿e on wyswietlaæ czas w uk³adzie 12 i 24 godziny. Wy¶wietla on tak¿e datê
kiedy przytci¶nie przycisk myszki maj±c kursor nad okienkiem zegarka.
W program s± wbudowane zdwa zestawy du¿ych fontów ale mo¿e on wy¶wietlaæ
inne fonty.

%prep
%setup -q

%build
xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdaliclock <<EOF
xdaliclock name "xdaliclock"
xdaliclock description "Marc's favorite clock"
xdaliclock group Amusements
xdaliclock exec "xdaliclock &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root)
%config(missingok) /etc/X11/wmconfig/xdaliclock
%attr(755, root, root) /usr/X11R6/bin/xdaliclock
/usr/X11R6/lib/X11/app-defaults/XDaliClock
%attr(755, root,  man) /usr/X11R6/man/man1/xdaliclock.1x

%changelog
* Sun Nov 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
