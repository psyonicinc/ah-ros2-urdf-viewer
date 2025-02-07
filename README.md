# Ability Hand ROS2 URDF Viewer

This repo has a Docker Compose / Dockerfile which pulls the latest URDF from the 
ability-hand-api repository and converts it to a ROS2 friendly format, and 
launches it using RViz.

## Installing Requirements

### Windows

- Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Install [XLaunch](https://sourceforge.net/projects/vcxsrv/)
- Launch Docker Desktop
- Launch XLaunch program select Multiple windows, Next, Start no client, Next, Un-Select Native opengl, Next, Finish

### Linux

Docker installation instructions for various linux distributions can be found
[here](https://docs.docker.com/engine/install/). Ensure you do the 
[post installation instructions](https://docs.docker.com/engine/install/linux-postinstall/)


## Launch

### Windows

- Open a power shell
- Enter `$env:DISPLAY="host.docker.internal:0.0"`
- Navigate to the docker directory and enter the following command

Launch using:

`docker compose up`

### Linux

Navigate to the docker directory and enter the following command

`xhost + && docker compose up`

## Usage

RViz allows you to visualize all transforms (TF) from the hand or attach the 
base_link of the hand to other frame TF topics.  You can also find the location
of TF's relative to other TF's using tf2_echo.  For example to get the 
transform from the base_link to pinky tip you can use.

`ros2 run tf2_ros tf2_echo base_link pinky_anchor`

or you can do this within your code using the TransformListener class
