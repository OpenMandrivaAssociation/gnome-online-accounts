%define		oname		goa
%define		api			1.0
%define		major		0
%define		libname		%mklibname %{oname} %{api} %{major}
%define		backendname	%mklibname %{oname}-backend %{api} %{major}
%define		gi_libname	%mklibname %{oname}-gir %{api}
%define		develname	%mklibname -d %{oname} %{api}
%define		develbackend %mklibname -d %{oname}-backend %{api}

Name:		gnome-online-accounts
Version:	3.4.1
Release:	%mkrel 0
Summary:	Provide online accounts information
Group:		Graphical desktop/GNOME
License:	LGPLv2+
URL:		http://developer.gnome.org/goa/stable/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch1:		gnome-online-accounts-3.2.0-link.patch

BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keybindings)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(webkitgtk-3.0)

%description
gnome-online-accounts provides interfaces so applications and 
libraries in GNOME can access the user's online accounts.

%package -n %{libname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
Runtime libraries for %{name}.

%package -n %{backendname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries

%description -n %{backendname}
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
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{develname}
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%package -n %{develbackend}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{backendname} = %{version}-%{release}
Provides:	%{oname}-backend-devel = %{version}-%{release}

%description -n %{develbackend}
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%prep
%setup -q
%patch1 -p1 -b.link

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-gtk-doc

%make LIBS='-lgmodule-2.0'

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
%{_libdir}/libgoa-%{api}.so.%{major}*

%files -n %{backendname}
%{_libdir}/libgoa-backend-%{api}.so.%{major}*

%files -n %{gi_libname}
%{_libdir}/girepository-1.0/Goa-%{api}.typelib

%files -n %{develname}
%{_includedir}/goa-%{api}/
%{_libdir}/libgoa-%{api}.so
%{_libdir}/pkgconfig/goa-%{api}.pc
%{_datadir}/gir-1.0/Goa-%{api}.gir
%{_datadir}/gtk-doc/html/goa/

%files -n %{develbackend}
%{_libdir}/libgoa-backend-%{api}.so
%{_libdir}/pkgconfig/goa-backend-%{api}.pc

