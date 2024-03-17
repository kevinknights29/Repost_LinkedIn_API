# Using a Dev Container in VS Code

The Visual Studio Code Dev Containers extension lets you use a container as a full-featured development environment.
It allows you to open any folder inside (or mounted into) a container and take advantage of Visual Studio Code's full feature set.

![image](https://code.visualstudio.com/assets/docs/devcontainers/containers/architecture-containers.png)

## Requirements

- [ ] Docker installed locally.
- [ ] VS Code Dev Containers Extension.

        Name: Dev Containers
        Id: ms-vscode-remote.remote-containers
        Description: Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's full feature set.
        Version: 0.347.0
        Publisher: Microsoft
        VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

For more, please refer to: [System Requirements](https://code.visualstudio.com/docs/devcontainers/containers#_system-requirements)

## Usage

If you meet the requirements, you can get started by just opening this project in VS Code, and selecting `Open in Dev Container`.

If the message above doesn't appear, you can press: `ctrl + shift + p` in your keyboard and type: `dev container`.
Select: `Open in Dev Container`.

This should display a status bar like example below:
![image](https://code.visualstudio.com/assets/docs/devcontainers/containers/dev-container-progress.png)

After the container starts successfully, you are ready to use and add features to the code.
