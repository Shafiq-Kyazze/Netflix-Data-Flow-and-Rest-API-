#DOcker file for REST API

#Pull the latest image of python
FROM python:3

#Set present working directory in docker image to a new folder REST_API
WORKDIR /REST_API

#copy the all the contents of our current working directory into the docker image working directory i.e REST_API
COPY . /REST_API

#Install the dependencies of the res api
RUN pip install -r requirements.txt

#Command that will run the run.py module to deploy the rest api
CMD ["python", "run.py"]