FROM node:18-alpine
ARG FILES

WORKDIR /app

RUN apk update \
    && apk add --no-cache \
    curl \
    busybox-extras

ENV TZ=Africa/Johannesburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./$FILES .

RUN adduser --disabled-password \
    --home /home/appuser \
    --gecos '' appuser \
RUN chown -R appuser /app
RUN chown -R appuser /mnt
USER appuser

EXPOSE 3000

CMD ["node", "server.js"]