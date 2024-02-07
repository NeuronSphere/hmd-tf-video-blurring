hmd-tf-video-blurring
=========================

NeuronSphere Container Transform to anonymize faces in a video.
It uses the ``deface`` library found at `https://github.com/ORB-HD/deface`.

Building and Testing
--------------------

Install NeuronSphere Tools
++++++++++++++++++++++++++

The Transform Image can be built using free NeuronSphere CLI Tools. 
Run ``pip install neuronsphere`` in a Python3.9+ environment to install the NeuronSphere CLI.
After installing the CLI, you need to setup and configure an ``HMD_HOME`` directory.
Run ``hmd configure`` and answer the prompts. It will first ask for a directory to act as you ``HMD_HOME``.
The directory must be at a valid path and will be created if it doesn't already exist.
Within the ``HMD_HOME`` directory, there is an ``HMD_REPO_HOME`` directory located at ``$HMD_HOME/projects`` by default. 
You should clone this repo into there, as a lot of NeuronSphere tools assume all your NeuronSphere projects are located here.

Building the Image
+++++++++++++++++++++++++++++

Once the repo is cloned to ``HMD_REPO_HOME``, you can build the Python library and the Docker Image that uses it by running ``hmd build`` in the repo root.
By default the Docker image will be tagged as ``$HMD_CONTAINER_REGISTRY/hmd-tf-video-blurring:0.1``.

Testing the Image
+++++++++++++++++++++++++++++

This repo comes with working RobotFramework tests in the ``./test/`` directory.
The NeuronSphere CLI includes a tool to run the test suite in a standardized manner.
Before running the test suite, you need to supply a video file to run against in ``./test/videos``.
To run the test suite, run ``hmd bender`` in the repo root.