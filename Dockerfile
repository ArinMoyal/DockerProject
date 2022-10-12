FROM alpine
# Python & pip installation:
# PYTHONUNBUFFERED=1 allows for log messages to immediately send to the stream instead of being buffered.
ENV PYTHONUNBUFFERED=1
# Using Alpine Package Keeper to install python3
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# Making sure pip is installed
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
CMD python /cubecalculation/cube.py >> /results
