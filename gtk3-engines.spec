Summary:	Default GTK+3 theme engines
Summary(pl.UTF-8):	Moduły motywów do GTK+3
Name:		gtk3-engines
Version:	2.91.1
Release:	0.2
License:	GPL v2+ and LGPL v2+
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.91/gtk-engines-%{version}.tar.bz2
# Source0-md5:	290d2fdb66743066dab92db694dd7b99
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post):	gtk+3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		_gtkconfdir	/etc/gtk%{libext}-3.0
%define		pqext		-%{libext}
%else
%define		_gtkconfdir	/etc/gtk-3.0
%define		pqext		%{nil}
%endif

%description
These are the graphical engines for the various GTK+ toolkit themes.

%description -l pl.UTF-8
Pakiet ten zawiera moduły różnych motywów do biblioteki GTK+.

%package themes
Summary:	Various GTK+ toolkit themes
Summary(pl.UTF-8):	Różne motywy do biblioteki GTK+
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description themes
Various GTK+ toolkit themes.

%description themes -l pl.UTF-8
Różne motywy do biblioteki GTK+.

%prep
%setup -q -n gtk-engines-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-animation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no .la for loadable GTK+ modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/*/engines/*.la

%find_lang gtk3-engines

%clean
rm -rf $RPM_BUILD_ROOT

#%%post
#umask 022
#gdk-pixbuf-query-loaders%{pqext} > %{_gtkconfdir}/gdk-pixbuf.loaders
#exit 0

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/*/engines/*.so
%{_pkgconfigdir}/gtk-engines-3.pc

%files themes -f gtk3-engines.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_datadir}/gtk-engines
%dir %{_datadir}/gtk-engines/3.0
%{_datadir}/gtk-engines/3.0/*.xml
%dir %{_datadir}/themes/Redmond
%{_datadir}/themes/Clearlooks
%{_datadir}/themes/Crux
%{_datadir}/themes/Industrial
%{_datadir}/themes/Mist
%{_datadir}/themes/Redmond/gtk-3.0
%{_datadir}/themes/ThinIce
%{_datadir}/themes/GNOME3
