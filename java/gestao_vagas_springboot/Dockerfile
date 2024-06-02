FROM maven:3.9.6-sapmachine-17

WORKDIR /usr/src/app

RUN apt-get update
# RUN apt-get install -y wget

# ENV DOCKERIZE_VERSION v0.7.0

COPY * .

EXPOSE 8080

RUN mvn spring-boot:run
# RUN mvn clean spring-boot:start

# RUN wget -O - https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | \
#     tar xzf - -C /usr/local/bin \
#     && apt autoremove -yqq --purge wget && \
#     rm -rf /var/lib/apt/lists/