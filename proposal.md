# Final Project Proposal

## Repository
https://github.com/tejasvig123/final-project.git

## Description
My final project is Glitch Art, and I want it to take an image and intentionally break it into random pixels. This would be useful to make unique drawings or artwork because each iteration would be different, and some artists might want that.1-2 sentence description of what it will do and how it relevant to media and digital arts.

## Features
- -RGB channel shifting
	-I will use Pillow for this to separate the image into red, green and blue layers.
- Datamoshing effect
	- Loop that generates random coordinates and cuts out parts of the image in rectangles, and pastes them back to different positions.
- Pixel sorting
	- Put pixel data into an array, and sort from darkest to lightest.

## Challenges
- I need to get a basic understanding of color theory in order to do this.
- I need to make sure to learn image boundaries as well so code doesn't give errors.
- I also need to understand color theory mathematically to calculate the luminance from the rgb values the code will input.

## Outcomes
Ideal Outcome:
- A simple program that allows a user to input any image of their choice and the output would be gltiches stacked on top of each other making a unique artwork.

Minimal Viable Outcome:
- It would be working code that applies basic RGB shift and saves the new image to the folder.

## Milestones

- Week 1
  1. Set up python environment and all files needed.
  2. Add RGB feature and make sure it works properly.

- Week 2
  1. Build the block displacement feature.
  2. Do the math for pixel sorting and put in a basic function to calculate the brightness.

- Week N (Final)
  1. Add final touches to pixel sorting algorithm.
  2. Test it out and create glitched artworks.


