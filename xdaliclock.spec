Summary:	Marc's favorite clock
Summary(de):	Marcs Lieblingsuhr
Summary(pl):	Ulubiony zegar Marca
Summary(tr):	Marc'ýn gözde saati
Name:		xdaliclock
Version:	2.20
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://www.jwz.org/xdaliclock/%{name}-%{version}.tar.gz
# Source0-md5:	be9642cc711a8d93ff13faac0cf4f306
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-shape-cycle.patch
Patch1:		%{name}-DESTDIR.patch
Icon:		xdaliclock.xpm
URL:		http://www.jwz.org/xdaliclock/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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
cp -f /usr/share/automake/config.sub .
cd X11
CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdefsdir},%{_pixmapsdir},%{_desktopdir}}

cd X11
%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

install XDaliClock.ad $RPM_BUILD_ROOT%{_appdefsdir}/XDaliClock
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_appdefsdir}/XDaliClock
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
