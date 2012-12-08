%define	oname		goa
%define	api		1.0
%define	major		0
%define	libname		%mklibname %{oname} %{api} %{major}
%define	backendname	%mklibname %{oname}-backend %{api} %{major}
%define	girname		%mklibname %{oname}-gir %{api}
%define	develname	%mklibname -d %{oname} %{api}
%define	develbackend	%mklibname -d %{oname}-backend %{api}

Summary:	Provide online accounts information
Name:		gnome-online-accounts
Version:	3.6.2
Release:	1
Group:		Graphical desktop/GNOME
License:	LGPLv2+
URL:		http://developer.gnome.org/goa/stable/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz

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

%package -n %{backendname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries

%description -n %{backendname}
Runtime libraries for %{name}.

%package -n %{girname}
Summary:	GObject introspection interface for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject introspection interface for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
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
#%apply_patches

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
rm -f %{buildroot}/%{_libdir}/*.a

%files -f %{name}.lang
%doc NEWS COPYING
%{_libexecdir}/goa-daemon
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/icons/hicolor/*/apps/goa-*.png
%{_datadir}/%{name}/goawebview.css
%{_mandir}/man8/goa-daemon.8*

%files -n %{libname}
%{_libdir}/libgoa-%{api}.so.%{major}*

%files -n %{backendname}
%{_libdir}/libgoa-backend-%{api}.so.%{major}*

%files -n %{girname}
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

%changelog
* Fri Sep 28 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799301
- update to new version 3.4.2

* Thu Apr 26 2012 Guilherme Moro <guilherme@mandriva.com> 3.4.1-0
+ Revision: 793638
- updated to version 3.4.1

* Wed Feb 22 2012 Jon Dill <dillj@mandriva.org> 3.2.1-2
+ Revision: 779275
- rebuild against new version of libffi4

* Tue Nov 22 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 732685
- clean up spec for first build
- split out backend lib & devel pkgs
- converted BRs to pkgconfig provides
- imported package gnome-online-accounts



* Mon Oct 17 2011 wally <wally> 3.2.1-1.mga2
+ Revision: 155935
- new version 3.2.1

* Wed Sep 28 2011 ovitters <ovitters> 3.2.0.1-3.mga2
+ Revision: 149891
- new version 3.2.0.1
- drop launch goa prefs patch (merged upstream)

* Wed Sep 28 2011 ovitters <ovitters> 3.2.0-3.mga2
+ Revision: 149744
- add upstream patch to fix a crasher

* Tue Sep 27 2011 fwang <fwang> 3.2.0-2.mga2
+ Revision: 149075
- rebuild for new glib

* Mon Sep 26 2011 ovitters <ovitters> 3.2.0-1.mga2
+ Revision: 149020
- new version 3.2.0

* Tue Sep 20 2011 fwang <fwang> 3.1.91-1.mga2
+ Revision: 145886
- new version 3.1.91

* Tue Aug 30 2011 dmorgan <dmorgan> 3.1.90-1.mga2
+ Revision: 136790
- Fix sha1.lst file

  + ovitters <ovitters>
    - Update to 3.1.90

  + ahmad <ahmad>
    - Replace BR libgnome-window-settings-devel with pkgconfig(gnome-keybindings)

* Thu Jul 14 2011 cjw <cjw> 3.1.1-2.mga2
+ Revision: 124256
- fix group

* Tue Jul 05 2011 cjw <cjw> 3.1.1-1.mga2
+ Revision: 118968
- imported package gnome-online-accounts


* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-3
- Add more necessary patches

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-2
- Update with review comments from Peter Robinson

* Mon Jun 13 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-1
- First version

