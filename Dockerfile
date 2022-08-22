FROM python:3.9-slim-bullseye

# set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# user uid and gid
ARG UID=999
ARG GID=999

# creating and changing to non-root user. (-mr: creating a HOME directory)
RUN groupadd -g $GID -o app  && \
    useradd -g $GID -u $UID  -mr -d /home/app -o -s /bin/bash app && \
    mkdir /home/app/staticfiles && \
    chown -R app:app /home/app/staticfiles

# changing user to "app"
USER app

# set work directory.
WORKDIR /home/app

# add /home/app/.local/bin to PATH
ENV PATH "$PATH:/home/app/.local/bin"

# upgrading pip and installing dependencies.
RUN pip install --upgrade pip 
COPY --chown=app:app requirements.txt .
RUN pip install -r /home/app/requirements.txt 

# copy project
COPY --chown=app:app . .

# application port
EXPOSE 8000

# adding exec permission to entypoint.sh
RUN chmod +x /home/app/entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]

