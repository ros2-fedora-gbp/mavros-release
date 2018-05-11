Name:           ros-lunar-mavros-extras
Version:        0.25.0
Release:        0%{?dist}
Summary:        ROS mavros_extras package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-mavros
Requires:       ros-lunar-mavros-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf
Requires:       ros-lunar-urdf
Requires:       ros-lunar-visualization-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-mavros
BuildRequires:  ros-lunar-mavros-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-urdf
BuildRequires:  ros-lunar-visualization-msgs

%description
Extra nodes and plugins for MAVROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri May 11 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.0-0
- Autogenerated by Bloom

* Thu Apr 05 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.24.0-0
- Autogenerated by Bloom

* Fri Mar 09 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.23.3-0
- Autogenerated by Bloom

* Wed Mar 07 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.23.2-0
- Autogenerated by Bloom

* Tue Feb 27 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.23.1-0
- Autogenerated by Bloom

* Sat Feb 03 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.23.0-0
- Autogenerated by Bloom

* Mon Dec 11 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.22.0-0
- Autogenerated by Bloom

* Thu Nov 16 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.5-0
- Autogenerated by Bloom

* Wed Nov 01 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.4-0
- Autogenerated by Bloom

* Sat Oct 28 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.3-0
- Autogenerated by Bloom

* Mon Sep 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.2-0
- Autogenerated by Bloom

* Fri Sep 22 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.1-0
- Autogenerated by Bloom

* Thu Sep 14 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.0-0
- Autogenerated by Bloom

* Mon Aug 28 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.20.1-0
- Autogenerated by Bloom

* Wed Aug 23 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.20.0-0
- Autogenerated by Bloom

* Thu May 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.19.0-0
- Autogenerated by Bloom

