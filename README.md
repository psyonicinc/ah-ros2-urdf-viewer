# Ability Hand ROS2 URDF Viewer

This repo has a Docker Compose / Dockerfile which pulls the latest URDF from the 
ability-hand-api repository and converts it to a ROS2 friendly format, and 
launches it using RVIZ.

## Installing docker

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

`docker compose build`

Followed by:

`docker compose up`

### Linux

Navigate to the docker directory and enter the following command

`xhost + && docker compose build && docker compose up`

