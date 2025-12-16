# Steps to creating a Docker image and container from this very project:

## Step 1: Dockerfile
- should just sit in the root directory relative to this project (along with requirements.txt)
- Make absolutely sure all the details in the Dockerfile is correct
- REMEMBER TO ADD ALL THE REQUIRED DEPENDENCIES IN REQUIREMENTS.TXT!
- The CMD layer should point to an entry point in our app, so as soon as the container using this image starts, the app itself starts

##  Step 2: Build image (in CLI)
- in CLI, cd to the current project, then run:
```
docker build -t deeplearning-20251-demo:1.0.0 .
```
The `-t` tag specifies, well, the tag for the image u tryna build (shocking)

verify that our image has been built and tagged correctly with `docker image ps`

## Step 3: Portainer can handle the rest!
In Portainer (obviously connect to our local Docker engine first), we can now just create a container with the newly built image!
