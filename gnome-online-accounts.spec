%define		api		1.0
%define		major		0
%define		libname		%mklibname goa %{api} %{major}
%define		gi_libname	%mklibname goa-gir %{api}
%define		develname	%mklibname -d goa %{api}

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:		gnome-online-accounts
Version:	3.2.1
Release:	%mkrel 1
Summary:	Provide online accounts information
Group:		Graphical desktop/GNOME
License:	LGPLv2+
URL:		http://developer.gnome.org/goa/stable/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch1:		gnome-online-accounts-3.2.0-link.patch

BuildRequires:	pkgconfig(gnome-keybindings)
BuildRequires:	glib2-devel
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libjson-glib-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	rest-devel
BuildRequires:	webkitgtk3-devel

%description
gnome-online-accounts provides interfaces so applications and 
libraries in GNOME can access the user's online accounts.

%package -n %{libname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
Runtime libraries for %{name}.

%package -n %{gi_libname}
Summary:	GObject introspection interface for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{gi_libname}
GObject introspection interface for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig
Requires:	gobject-introspection-devel
Provides:	libgoa-devel = %{version}-%{release}

%description -n %{develname}
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%prep
%setup -q
%patch1 -p1 -b.link

%build
autoreconf -fi
%configure2_5x --disable-static --enable-gtk-doc
%make

%install
%makeinstall_std
%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la

%files -f %{name}.lang
%doc NEWS COPYING
%{_libexecdir}/goa-daemon
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/icons/hicolor/*/apps/goa-*.png
%{_mandir}/man8/goa-daemon.8.*

%files -n %{libname}
%{_libdir}/libgoa-%{api}.so.%{major}
%{_libdir}/libgoa-%{api}.so.%{major}.*
%{_libdir}/libgoa-backend-%{api}.so.%{major}
%{_libdir}/libgoa-backend-%{api}.so.%{major}.*

%files -n %{gi_libname}
%{_libdir}/girepository-1.0/Goa-%{api}.typelib

%files -n %{develname}
%{_includedir}/goa-%{api}/
%{_libdir}/libgoa-%{api}.so
%{_libdir}/libgoa-backend-%{api}.so
%{_datadir}/gir-1.0/Goa-%{api}.gir
%{_libdir}/pkgconfig/goa-%{api}.pc
%{_libdir}/pkgconfig/goa-backend-%{api}.pc
%{_datadir}/gtk-doc/html/goa/



