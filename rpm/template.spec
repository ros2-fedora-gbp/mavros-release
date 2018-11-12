Name:           ros-melodic-mavros-msgs
Version:        0.27.0
Release:        0%{?dist}
Summary:        ROS mavros_msgs package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-geographic-msgs
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-geographic-msgs
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs

%description
mavros_msgs defines messages for MAVROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Nov 12 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.27.0-0
- Autogenerated by Bloom

* Sat Nov 10 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.3-1
- Autogenerated by Bloom

* Tue Aug 21 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.3-0
- Autogenerated by Bloom

* Wed Aug 08 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.2-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.1-0
- Autogenerated by Bloom

* Wed Jun 06 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.0-0
- Autogenerated by Bloom

* Mon May 14 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.1-0
- Autogenerated by Bloom

* Fri May 11 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.0-0
- Autogenerated by Bloom

* Mon May 07 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.24.0-0
- Autogenerated by Bloom

