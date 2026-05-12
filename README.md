# Glitch Art

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <URL>

## Description
This project is an interactive tool that combines both pygame and pillow to generate digital glitch art. Instead of the program automatically making an image for you, this program lets you control how exactly it glitches in several different ways. Requirements.txt contains the 3rd party libraries that were needed for this program, and test.jpg is the test image I used to show you guys the output. Project.py is where all the code is, and the functions to create rgb color shift, datamoshing, and sorting pixels randomly. A problem that I faced was image resolution, because making it 4k would be too draining on the system, so in the initialization step I made it check the image dimensions and have it automatically scale down to fit a standard 1200 x 1800 pixels.

A future improvement I would consider is making the controls better, because right now they are all only accessible through keyboard shortcuts. If I have the time, I would want to make an actual interface with sliders to increase or decrease intensity for each control. I also want this to be able to corrupt gifs as well and not just images.
