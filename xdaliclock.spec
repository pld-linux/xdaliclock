Summary:	Marc's favorite clock
Summary(de):	Marcs Lieblingsuhr
Summary(fr):	Marc's favorite clock.
Summary(pl):	Ulubiony zegar Marca
Summary(tr):	Marc'ýn gözde saati
Name:		xdaliclock
Version:	2.14
Release:	3
Copyright:      MIT
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
URL:            http://www.jwz.org/xdaliclock/
Source:		ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Patch:		xdaliclock-shape-cycle.patch
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description
The xdaliclock program displays a digital clock; when a digit changes, it
"melts" into its new shape.

It can display in 12 or 24 hour modes, and displays the date when a mouse
button is held down.  It has two large fonts built into it, but it can animate
other fonts.

%description -l pl
Program xdaliclock wy¶wietla cyfrowy zegar, w którym zmieniaj±ce siê cyfry
p³ynnie przechodz± jedna w drug±.

Mo¿e on wyswietlaæ czas w uk³adzie 12 i 24 godziny. Wy¶wietla on tak¿e datê
kiedy przyci¶nie siê przycisk myszki maj±c kursor nad okienkiem zegarka.
W program s± wbudowane dwa zestawy du¿ych fontów ale mo¿e on wy¶wietlaæ
inne czcionki.

%prep
%setup -q
%patch -p1

%build
xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir} 

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/X11/app-defaults/XDaliClock
%{_mandir}/man1/*
