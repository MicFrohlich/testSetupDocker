# python:3 image is very old use python:3.6
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /code/
# Use ENTRYPOINT to tell your container what it needs to run as the command
# to start it, in our case we need to run multiple commands, hence using an
# sh file works best here
ENTRYPOINT ["sh", "/code/entrypoint.sh"]