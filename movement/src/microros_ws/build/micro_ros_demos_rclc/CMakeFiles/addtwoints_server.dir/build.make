# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/abdelrhaman/microros_ws/src/uros/micro-ROS-demos/rclc

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc

# Utility rule file for addtwoints_server.

# Include any custom commands dependencies for this target.
include CMakeFiles/addtwoints_server.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/addtwoints_server.dir/progress.make

CMakeFiles/addtwoints_server: CMakeFiles/addtwoints_server-complete

CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-install
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-mkdir
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-download
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-update
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-patch
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-build
CMakeFiles/addtwoints_server-complete: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-install
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Completed 'addtwoints_server'"
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles
	/usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles/addtwoints_server-complete
	/usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-done

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-build: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Performing build step for 'addtwoints_server'"
	cd /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-build && $(MAKE)

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure: addtwoints_server/tmp/addtwoints_server-cfgcmd.txt
addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure: addtwoints_server/tmp/addtwoints_server-cache-.cmake
addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-patch
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Performing configure step for 'addtwoints_server'"
	cd /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-build && /usr/bin/cmake "-GUnix Makefiles" -C/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/tmp/addtwoints_server-cache-.cmake /home/abdelrhaman/microros_ws/src/uros/micro-ROS-demos/rclc/addtwoints_server
	cd /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-build && /usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-download: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-mkdir
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "No download step for 'addtwoints_server'"
	/usr/bin/cmake -E echo_append
	/usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-download

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-install: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-build
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Performing install step for 'addtwoints_server'"
	cd /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-build && $(MAKE) install
	cd /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-build && /usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-install

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-mkdir:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Creating directories for 'addtwoints_server'"
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/src/uros/micro-ROS-demos/rclc/addtwoints_server
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-build
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/temp_install
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/tmp
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src
	/usr/bin/cmake -E make_directory /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp
	/usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-mkdir

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-patch: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-update
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "No patch step for 'addtwoints_server'"
	/usr/bin/cmake -E echo_append
	/usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-patch

addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-update: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "No update step for 'addtwoints_server'"
	/usr/bin/cmake -E echo_append
	/usr/bin/cmake -E touch /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-update

addtwoints_server: CMakeFiles/addtwoints_server
addtwoints_server: CMakeFiles/addtwoints_server-complete
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-build
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-configure
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-download
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-install
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-mkdir
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-patch
addtwoints_server: addtwoints_server/src/addtwoints_server-stamp/addtwoints_server-update
addtwoints_server: CMakeFiles/addtwoints_server.dir/build.make
.PHONY : addtwoints_server

# Rule to build all files generated by this target.
CMakeFiles/addtwoints_server.dir/build: addtwoints_server
.PHONY : CMakeFiles/addtwoints_server.dir/build

CMakeFiles/addtwoints_server.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/addtwoints_server.dir/cmake_clean.cmake
.PHONY : CMakeFiles/addtwoints_server.dir/clean

CMakeFiles/addtwoints_server.dir/depend:
	cd /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/abdelrhaman/microros_ws/src/uros/micro-ROS-demos/rclc /home/abdelrhaman/microros_ws/src/uros/micro-ROS-demos/rclc /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc /home/abdelrhaman/microros_ws/build/micro_ros_demos_rclc/CMakeFiles/addtwoints_server.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/addtwoints_server.dir/depend

