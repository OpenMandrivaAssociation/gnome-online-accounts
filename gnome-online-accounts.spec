%define _disable_rebuild_configure 1
%define	api		1.0
%define	major		0
%define	libname		%mklibname goa %{api} %{major}
%define backendmajor	2
%define libbackend	%mklibname goa-backend %{api} %{backendmajor}
%define	gi_libname	%mklibname goa-gir %{api}
%define	develname	%mklibname -d goa

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:		gnome-online-accounts
Version:	3.50.0
Release:	1
Summary:	Provide online accounts information
Group:		Graphical desktop/GNOME
License:	LGPLv2+
URL:		https://developer.gnome.org/goa/stable/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(cheese-gtk)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gcr-4)
BuildRequires: pkgconfig(gio-2.0) >= 2.33.3
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.35
BuildRequires: pkgconfig(glib-2.0) >= 2.33.3
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libsecret-1) >= 0.5
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(rest-1.0)
BuildRequires: pkgconfig(telepathy-glib) >= 0.19.9
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(krb5)
BuildRequires: pkgconfig(ss)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gtk-doc
BuildRequires: gettext
BuildRequires: vala-devel
BuildRequires: meson

%description
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package -n %{libname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n %{libname}
Runtime libraries for %{name}.

%package -n %{libbackend}
Summary:        Runtime libraries for %{name}
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n %{libbackend}
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
Requires:	%{libbackend} = %{version}-%{release}
Obsoletes:	%{_lib}goa1.0-devel < 3.9.90

%description -n %{develname}
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%prep
%setup -q -n %{name}-%{version}

%build
%meson	\
	-Dgtk_doc=true
%meson_build

%install
%meson_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc NEWS
%{_libexecdir}/goa-daemon
%{_libexecdir}/goa-identity-service
%{_libexecdir}/goa-oauth2-handler
%{_datadir}/applications/org.gnome.OnlineAccounts.OAuth2.desktop
%{_datadir}/dbus-1/services/org.gnome.Identity.service
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_iconsdir}/hicolor/*/apps/*
%dir %{_libdir}/goa-%{api}
%{_datadir}/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml

%files -n %{libname}
%{_libdir}/libgoa-%{api}.so.%{major}
%{_libdir}/libgoa-%{api}.so.%{major}.*

%files -n %{libbackend}
%{_libdir}/libgoa-backend-%{api}.so.%{backendmajor}
%{_libdir}/libgoa-backend-%{api}.so.%{backendmajor}.*

%files -n %{gi_libname}
%{_libdir}/girepository-1.0/Goa-%{api}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/goa/
%{_includedir}/goa-%{api}/
%{_libdir}/goa-%{api}/include
%{_libdir}/libgoa-%{api}.so
%{_libdir}/libgoa-backend-%{api}.so
%{_datadir}/gir-1.0/Goa-%{api}.gir
%{_libdir}/pkgconfig/goa-%{api}.pc
%{_libdir}/pkgconfig/goa-backend-%{api}.pc
%{_datadir}/vala/vapi/goa-%{api}.*
%exclude %{_libexecdir}/goa-identity-service-3.28.0-1.x86_64.debug
