Name:       qt5-plugin-geoservices-osm 
Summary:    Qt Geoservices plugin for OpenStreetMaps
Version:    5.4.3
Release:    1%{?dist}
License:    (LGPLv2 or LGPLv3) with exception or GPLv3 or Qt Commercial
URL:        https://github.com/sailfishos/qtlocation
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtnetwork
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-tools

Requires:   qt5-qtlocation = %{version}-%{release}
Obsoletes:  qt5-qtlocation-plugin-geoservices-osm <= 5.1.0+git7
Provides:   qt5-qtlocation-plugin-geoservices-osm > 5.1.0+git7

%description -n qt5-plugin-geoservices-osm
This package contains the geoservices plugin for OpenStreetMaps


%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
%make_build


%install
rm -rf %{buildroot}
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

#install docs

# files
%files -n qt5-plugin-geoservices-osm
%defattr(-,root,root,-)
%{_datadir}/qt5/mkspecs/modules/qt_lib_location.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_location_private.pri
%{_libdir}/cmake/Qt5Location/
%{_libdir}/qt5/plugins/geoservices/*osm*

