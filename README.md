# DockerProject
### My RT-ED Docker project

In this project, the script runs every time a commit is made.

It first builds the AlpCon image from the Dockerfile.

Then, the script checks to see whether it is already running or not. If it's running, it prints the error and exits, and if not, it starts an AlpCon container and waits 10 seconds.

If after 10 seconds the container has been stopped, it considers the process a success, and if it's still running it considers it a failure. In both cases the container and image are deleted, and the activity of the container is logged.

The relevant files in this repository are "JenkinsfileSimple", "Dockerfile" and the "simple" folder. The rest were all much more complicated attempts that were unnecessary, and you may browse them if you wish.


#### Thanks for reading me! ;)
