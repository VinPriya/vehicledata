#Commands used to build and connect the Application

+This sets the local version of python to 3.7.9
  pyenv local 3.7.9 

+This creates the virtual environment for you
  python3 -m venv .venv 

+This activates the virtual environment
  source.venv/bin/activate 

+This installs pip, and upgrades it if required
  pip install --upgrade pip 

+To create web framework for the application
  pip install flask

+To create DB file
  touch eleVehicle.db

+Running this in terminal for variables
  export FLASK_APP=polar_bears.py
  export FLASK_ENV=development
  python3 -m flask run

Successfully uploaded the app to render, below is the link regarding app
  https://vehicledata2-test.onrender.com 
(Deploying app was not Successfully done,due to some errors)