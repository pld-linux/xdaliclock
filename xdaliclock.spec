Summary:	Marc's favorite clock
Summary(de.UTF-8):   Marcs Lieblingsuhr
Summary(pl.UTF-8):   Ulubiony zegar Marca
Summary(tr.UTF-8):   Marc'ın gözde saati
Name:		xdaliclock
Version:	2.23
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://www.jwz.org/xdaliclock/%{name}-%{version}.tar.gz
# Source0-md5:	1c16ce93d8da5c1f10d462108695042c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-shape-cycle.patch
Patch1:		%{name}-DESTDIR.patch
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

%description -l pl.UTF-8
Program xdaliclock wyświetla cyfrowy zegar, w którym zmieniające się
cyfry płynnie przechodzą jedna w drugą.

Może on wyświetlać czas w układzie 12 i 24 godziny. Wyświetla on także
datę kiedy przyciśnie się przycisk myszki mając kursor nad okienkiem
zegarka. W program są wbudowane dwa zestawy dużych fontów ale może on
wyświetlać inne czcionki.

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
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_appdefsdir}/XDaliClock
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
