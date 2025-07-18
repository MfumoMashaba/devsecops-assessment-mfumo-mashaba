#use minimal base image
FROM node:18-alpine 
#parse folder to copy as an argument
ARG FILES

WORKDIR /app

#install container dependencies .e.g. use curl to validate 
RUN apk update \
    && apk add --no-cache \
    curl \
    busybox-extras

#set correct timezone so the logs who the correct time
ENV TZ=Africa/Johannesburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#copy files
COPY ./$FILES .

#create user so it doesn't use root user 
RUN adduser --disabled-password \
    --home /home/appuser \
    --gecos '' appuser 
RUN chown -R appuser /app
RUN chown -R appuser /mnt
USER appuser

EXPOSE 3000

CMD ["node", "server.js"]