FROM alpine
# Python & pip installation:
# PYTHONUNBUFFERED=1 allows for log messages to immediately send to the stream instead of being buffered.
ENV PYTHONUNBUFFERED=1
# Using Alpine Package Keeper to install python3
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# Making sure the script executes by default when you launch the built image
ARG ws
ENV env_name $ws
CMD python /simple/simple.py
