Name:           ros-kinetic-urdf
Version:        1.12.12
Release:        0%{?dist}
Summary:        ROS urdf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-rosconsole-bridge
Requires:       ros-kinetic-roscpp
Requires:       tinyxml-devel
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-rosconsole-bridge
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-urdf-parser-plugin
BuildRequires:  tinyxml-devel
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel

%description
This package contains a C++ parser for the Unified Robot Description Format
(URDF), which is an XML format for representing a robot model. The code API of
the parser has been through our review process and will remain backwards
compatible in future releases.

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
* Wed Nov 08 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.12-0
- Autogenerated by Bloom

