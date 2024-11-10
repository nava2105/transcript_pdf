# Transcriptor
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
## General Info
***
This is a project build in python whose purpose is to provide the user an easy way to extract the content of a pdf. 
## Technologies
***
A list of technologies used within the project:
using the version 3.12.0 and using flask as a web framework
* [Python](https://www.python.org): Version 3.12.0
* [Flask](https://flask.palletsprojects.com/en/stable/): Version 3.0.3
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/): Version 1.24.10
* [python-docx](https://python-docx.readthedocs.io/en/latest/): Version 1.1.2
## Installation
***
There are two methods to install this project.
### Via GitHub
There is also two ways to install this project if you want to get it via GitHub.
#### Using Docker
Verify you are running Docker or Docker Desktop and open a terminal in the folder you want to install the application.

Copy the repository
```
$ git clone https://github.com/nava2105/transcript_pdf.git
```
Enter the directory
```
$ cd ../transcriptor
```
Build and run the container
```
$ docker-compose up --build
```
Open a browser and enter to
[http://localhost:5000](http://localhost:5000)
#### Not using Docker
Verify you are python version 3.12.0
```
$ python --version
```
Copy the repository
```
$ git clone https://github.com/nava2105/transcript_pdf.git
```
Enter the directory
```
$ cd ../transcriptor
```
Create a virtual environment
```
$ python -m venv .venv
```
Activate your virtual environment
* In Windows
```
$ .venv\Scripts\activate
```
* In macOS or Linux
```
$ source .venv/bin/activate
```
Build the dependencies
```
$ pip install requirements.txt -r
```
Open a browser and enter to
[http://localhost:5000](http://localhost:5000)
### Via Docker-hub
Pull the image from Docker-hub
```
$ docker pull na4va4_transcriptor
```
Start a container from the image
```
$ docker run -d na4va4_transcriptor
```
Open a browser and enter to
[http://localhost:5000](http://localhost:5000)
