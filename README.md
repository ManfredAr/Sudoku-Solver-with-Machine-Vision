About:
This repository contains my Final Year project. The project is about implementing a Sudoku and Killer Sudoku using AI. I have used
constraint programming with optimization techniques to implement the solver and from testing it can solver all diffficulty of puzzles
within 0.2 seconds.In addition I have also developed a machine vision algorithm which accepts an image from the user and convert the image to a 2d array which can be processed by the solver to find a solution. I built the application in python and used django to setup the website, in
addition it uses OpenCV for image processing, keras and tensorflow for machine learning.

Features:

- A website to access the features
- Sudoku and Killer Sudoku Game playing
- A Sudoku and Killer Sudoku Solver
- Machine Vision to enter puzzles

Specification:
The project is developed using Python 3.8.5 so please make sure that is the version you are running the code with.

How to run

- First make sure to install all the packages required for the project. The requirements.txt file contains all the required
  packages. Simply use this command "pip install -r requirements".
- Onces the environment is setup, to run the website first make sure you are in the top level FinalYearProject directory, then run
  the command py manage.py runserver. Now to view the website go to this link "http://127.0.0.1:8000/".

- to run the TTD tests use this command "py -m unittest discover -s "./test" -p "test*.py"".
- to run the frontend testing use this command. Note to run the frontend testing the website should already be running first.
