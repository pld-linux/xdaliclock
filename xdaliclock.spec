Summary:	Marc's favorite clock
Summary(de):	Marcs Lieblingsuhr
Summary(pl):	Ulubiony zegar Marca
Summary(tr):	Marc'ýn gözde saati
Name:		xdaliclock
Version:	2.19
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://www.jwz.org/xdaliclock/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-shape-cycle.patch
Patch1:		%{name}-DESTDIR.patch
Icon:		xdaliclock.xpm
URL:		http://www.jwz.org/xdaliclock/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
The xdaliclock program displays a digital clock; when a digit changes,
it "melts" into its new shape.

It can display in 12 or 24 hour modes, and displays the date when a
mouse button is held down. It has two large fonts built into it, but
it can animate other fonts.

%description -l pl
Program xdaliclock wy¶wietla cyfrowy zegar, w którym zmieniaj±ce siê
cyfry p³ynnie przechodz± jedna w drug±.

Mo¿e on wy¶wietlaæ czas w uk³adzie 12 i 24 godziny. Wy¶wietla on tak¿e
datê kiedy przyci¶nie siê przycisk myszki maj±c kursor nad okienkiem
zegarka. W program s± wbudowane dwa zestawy du¿ych fontów ale mo¿e on
wy¶wietlaæ inne czcionki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd X11
CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/ \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Amusements}

cd X11
%{__make} install install-man DESTDIR=$RPM_BUILD_ROOT

install XDaliClock.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/XDaliClock
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/X11/app-defaults/XDaliClock
%{_mandir}/man1/*
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/*
