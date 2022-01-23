# AutoPlanner [![python 3.9.9](https://img.shields.io/badge/python-3.9-green.svg)](https://www.python.org/downloads/release/python-399/) [![Node.js](https://img.shields.io/badge/Node.js-16.13.1-green)](https://nodejs.org/en/download/) [![Django](https://img.shields.io/badge/Django-3.1.7-green)](https://www.djangoproject.com/download/)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
<!-- * [License](#license) -->


## General Information
AutoPlanner is a web application with view to planners in all type of schools up to highschool.
Let's say on the begining, it isn't generating optimal plans but decent ones with which creation planner would not be ashamed of.
The purpouse of creating this app was to make planners job easier and as overhelming as it is now.


## Technologies Used
- Frontend
  - Vue.js
- Backend
  - Django  
  - AWS RDS
- Algorithm
  - Python
- CI/CD
  - circleci
  - AWS EC2
  - 


## Features
- Sign up & Sign in
- Add/rm subjects to data base
- Add/rm teachers to data base
- Set preferred subjects for teacher
- Add/rm classrooms to data base
- Set preferred subjcets for classroom
- Add/rm Groups to data base
- Setup each group subject per week count 
  and preffered teachers
- Generate schedule
- Display school schedule
- Display techaer schedule
- Display group schedule
- Display classroom schedule
- #### More features will be added soon...


## Setup
Project requirements can be found in requirements.txt file.
### To setup project to run locally:
 - #### Frontend:
    - To run frontend server Node.js is needed. 
    - Preferred and checked version of Node.js is LTS one.
    - Step-by-step setup of installation Node.js with [nvm](https://gist.github.com/d2s/372b5943bce17b964a79)
    - When Node.js up and working, install dependencies like:
      - ``` cd {pathtorepo}/AutoPlanner/Frontend ```
      - ``` npm install ```
    - To run server:
      - ``` npm run serve ```
 - #### Backend/Algorithm:
    - Python 3.9.9 is checked and recommended.
    - Preferred and checked version of django is 3.1.7.
    - To install requirements wen in repo root, run:
      - ``` python -m pip install -r requiements.txt ```
    - To run django server locally: 
      - ``` cd {pathtorepo}/AutoPlanner/Backend ```
      - ``` python -m manage.py runserver ```


## Project Status
Project is: _in progress_


## Room for Improvement
Room for improvement:
- Possibility of spliting groups to subject groups. (e2e)
- Possibility of providing manual changes in generated schedule. (e2e) 
- Statistics of generated schedule. (Frontend)
