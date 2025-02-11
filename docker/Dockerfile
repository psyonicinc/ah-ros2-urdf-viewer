ARG ROS_DISTRO=humble
FROM osrf/ros:${ROS_DISTRO}-desktop-full
ARG USERNAME=ros
ARG USER_UID=1000
ARG USER_GID=$USER_UID

SHELL ["/bin/bash", "-c"]

# Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    # && apt-get update \
    # && apt-get install -y sudo \
    # && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    # && chmod 0440 /etc/sudoers.d/$USERNAME
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip vim tmux git ros-${ROS_DISTRO}-joint-state-publisher-gui

# Download latest AH API repo and copy urdf files
RUN git clone https://github.com/psyonicinc/ability-hand-api.git 
COPY /ws /ws/
RUN cp /ability-hand-api/URDF/*.urdf /ws/src/urdf_ah/urdf
RUN cp /ability-hand-api/URDF/models/* /ws/src/urdf_ah/models/
RUN cd /ws/src/urdf_ah/urdf && python3 convert_to_ros2_urdf.py ability_hand_left_large.urdf
RUN cd /ws/src/urdf_ah/urdf && python3 convert_to_ros2_urdf.py ability_hand_left_small.urdf
RUN cd /ws/src/urdf_ah/urdf && python3 convert_to_ros2_urdf.py ability_hand_right_large.urdf
RUN cd /ws/src/urdf_ah/urdf && python3 convert_to_ros2_urdf.py ability_hand_right_small.urdf
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && cd /ws/ && colcon build && source install/setup.bash 

ENV SHELL /bin/bash

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

# Source ROS bash
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /home/$USERNAME/.bashrc
RUN echo "source /ws/install/setup.bash" >> /home/$USERNAME/.bashrc
CMD ["bash", "-c", "source /opt/ros/${ROS_DISTRO}/setup.bash && source /ws/install/setup.bash && ros2 launch urdf_launch display.launch.py urdf_package:=urdf_ah urdf_package_path:=urdf/ability_hand_right_large.urdf"]
