Summary:	Marc's favorite clock
Summary(de):	Marcs Lieblingsuhr
Summary(fr):	Marc's favorite clock.
Summary(pl):	Ulubiony zegar Marca
Summary(tr):	Marc'�n g�zde saati
Name:		xdaliclock
Version:	2.18
Release:	3
Copyright:	MIT
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Source0:	http://www.jwz.org/xdaliclock/%{name}-%{version}.tar.gz
Patch0:		xdaliclock-shape-cycle.patch
Patch1:		xdaliclock-DESTDIR.patch
URL:		http://www.jwz.org/xdaliclock/
BuildRequires:	XFree86-devel
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
Program xdaliclock wy�wietla cyfrowy zegar, w kt�rym zmieniaj�ce si�
cyfry p�ynnie przechodz� jedna w drug�.

Mo�e on wyswietla� czas w uk�adzie 12 i 24 godziny. Wy�wietla on tak�e
dat� kiedy przyci�nie si� przycisk myszki maj�c kursor nad okienkiem
zegarka. W program s� wbudowane dwa zestawy du�ych font�w ale mo�e on
wy�wietla� inne czcionki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd X11
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/

cd X11
%{__make} install install-man DESTDIR=$RPM_BUILD_ROOT

install XDaliClock.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/XDaliClock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/X11/app-defaults/XDaliClock
%{_mandir}/man1/*
