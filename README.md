# iReporter-api

[![Build Status](https://travis-ci.org/lizz24/iReporter-api.svg?branch=develop)](https://travis-ci.org/lizz24/iReporter-api)
[![Coverage Status](https://coveralls.io/repos/github/lizz24/iReporter-api/badge.svg)](https://coveralls.io/github/lizz24/iReporter-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/d74c2d36c966d197aec2/maintainability)](https://codeclimate.com/github/lizz24/iReporter-api/maintainability)
 > iReporter enables any/every citizen to bring any form of corruption to the notice
 
 ## Functionality
 
 
| Endpoint  | Fuctionality |
| ------------- | ------------- |
| POST /api/v1/red-flags  | Create a red-flag record  |
| GET /api/v1/red-flags  | Get all red-flag records  |
| GET /api/v1/red-flags/<int:redflag_id>  | Get a specific red-flag record |
| PATCH /api/v1/red-flags/<int:redflag_id>/comment  | Edit comment red-flag record|
| PATCH /api/v1/red-flags/<int:redflag_id>/location  | Edit location red-flag record|
| DELETE /api/v1/red-flags/<int:redflag_id>  | Delete a red-flag record  |


## How to Test Manually
1. Clone the project to your local machine 
- https://github.com/lizz24/iReporter-api.git
 
2 . Create Virtual Environment 
 -  virtualenv venv
  
3. Activate Virtual ENvironment
-  source venv/bin/activate
   
4. Install Dependencies
 - (venv)$ pip3 install -r requirements.txt 
  
5. Run the app 
- python3 run.py
   
6. Run tests 
- python -m pytest 

## HEROKU LINK
YOU CAN USE THE HEROKU LINK TO TEST THE ENDPOINTS USING POST MAN [HERE](https://i-reporter-live.herokuapp.com)
