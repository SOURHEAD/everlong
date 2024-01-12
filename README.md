# This is a CI/CD pipeline made using jenkins and EC2.

There is a simple flask app created (based on a song called everlong) and containerized using docker.
EC2 instance has Jenkins and docker installed, Jenkins is configured to use docker api plugin.

Jenkins has three stages in its pipeline,
First building the dockerfile which makes a python container.
It then  runs the unittests provided in the tests.py file (Although currently only checks for status code 200 from the website)
And then Jenkins has my DockerHub credentials configured so it pushes the image if everything clears.
In the end it logs out of the account as I have used the docker access token for the Jenkins.
