Name:           ros-kinetic-mavros-msgs
Version:        0.18.5
Release:        0%{?dist}
Summary:        ROS mavros_msgs package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-std-msgs

%description
mavros_msgs defines messages for MAVROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Dec 12 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.5-0
- Autogenerated by Bloom

* Fri Nov 11 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.4-0
- Autogenerated by Bloom

* Thu Jul 07 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.3-1
- Autogenerated by Bloom

* Thu Jul 07 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.3-0
- Autogenerated by Bloom

* Thu Jun 30 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.2-0
- Autogenerated by Bloom

* Fri Jun 24 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.1-0
- Autogenerated by Bloom

* Thu Jun 23 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.18.0-0
- Autogenerated by Bloom

* Fri May 20 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.17.3-0
- Autogenerated by Bloom

* Sun May 15 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.17.2-1
- Autogenerated by Bloom

* Fri Apr 29 2016 Vladimir Ermakov <vooon341@gmail.com> - 0.17.2-0
- Autogenerated by Bloom

