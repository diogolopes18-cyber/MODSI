# ACADEMIC PAPER MANAGEMENT PLATFORM

**MODSI** is a web app built using Flask, PostgreSQL and HTML which allows students, conselours and public to publish academic papers and also consult their work.
The database schema was built taking into account three main actors: students, teachers and conselours.
At the time, it still needs improvement such as session implementation, project approval and deletion and more secure authentication.

![](https://img.shields.io/github/languages/count/diogolopes18-cyber/MODSI)
![](https://img.shields.io/github/repo-size/diogolopes18-cyber/MODSI)
![](https://img.shields.io/github/license/diogolopes18-cyber/MODSI)

# Installation

## Docker Image

By cloning the repository, you have already the necessary tools to run the application. To do so:

1. `cd docker_dev`
1. `docker-compose up` for running all services

## Database Service

To make alterations into the database schema you need to run the database service separately by doing:

`docker-compose run database bash`

# Docker Hub

For those who are not interested in improving the app or get to know its architecture, just pull the official Docker image by doing:

`docker pull cyberking18/modsi`

# Contributing

Pull requests are welcome. Please open a issue first to discuss the changes, and then open a pull request.
