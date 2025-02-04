#Base image
FROM python:3.12

#Install pandas
RUN pip install pandas

#set the working dir
WORKDIR /test-setup/

#Copy the file from local to docker file and set destination in docker file
#In this case local and docker paths are same (file)
COPY test-pipeline.py test-pipeline.py

#Overwrite the entrypoint to install pandas
# the syntax is the exec form using JSON array syntax where each of "elements" form one part of the command
ENTRYPOINT [ "python", "test-pipeline.py" ]

#Docker is built using docker build -t setup:pandas .
#-t is the tag, name of the file is setup and tag is pandas,
# . is the current directory to search for docker files
#Any change to this dockerfile, docker must be rebuilt.