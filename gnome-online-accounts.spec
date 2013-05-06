%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	oname	goa
%define	api	1.0
%define	major	0
%define	libname		%mklibname %{oname} %{api} %{major}
%define	libbackend	%mklibname %{oname}-backend %{api} %{major}
%define	girname		%mklibname %{oname}-gir %{api}
%define	devname		%mklibname -d %{oname} %{api}
%define	devbackend	%mklibname -d %{oname}-backend %{api}

Summary:	Provide online accounts information
Name:		gnome-online-accounts
Version:	3.8.1
Release:	1
Group:		Graphical desktop/GNOME
License:	LGPLv2+
Url:		http://developer.gnome.org/goa/stable/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-online-accounts/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(webkitgtk-3.0)
BuildRequires:  pkgconfig(libsecret-1)

%description
gnome-online-accounts provides interfaces so applications and 
libraries in GNOME can access the user's online accounts.

%package -n %{libname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
Runtime libraries for %{name}.

%package -n %{libbackend}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries

%description -n %{libbackend}
Runtime libraries for %{name}.

%package -n %{girname}
Summary:	GObject introspection interface for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject introspection interface for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{devname}
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%package -n %{devbackend}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libbackend} = %{version}-%{release}
Provides:	%{oname}-backend-devel = %{version}-%{release}

%description -n %{devbackend}
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS COPYING
%{_libexecdir}/goa-daemon
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/%{name}/goawebview.css
%{_iconsdir}/hicolor/*/apps/goa-*.png
%{_mandir}/man8/goa-daemon.8*

%files -n %{libname}
%{_libdir}/libgoa-%{api}.so.%{major}*

%files -n %{libbackend}
%{_libdir}/libgoa-backend-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Goa-%{api}.typelib

%files -n %{devname}
%{_includedir}/goa-%{api}/
%{_libdir}/libgoa-%{api}.so
%{_libdir}/pkgconfig/goa-%{api}.pc
%{_libdir}/goa-%{api}/include/goaconfig.h
%{_datadir}/gir-1.0/Goa-%{api}.gir
%{_datadir}/gtk-doc/html/goa/

%files -n %{devbackend}
%{_libdir}/libgoa-backend-%{api}.so
%{_libdir}/pkgconfig/goa-backend-%{api}.pc

