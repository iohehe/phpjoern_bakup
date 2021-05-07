FROM openjdk:8-jre
LABEL maintainer="iohex"
RUN apt-get update && apt-get install -y
ADD joern /tmp/joern
WORKDIR /tmp/joern
RUN wget https://services.gradle.org/distributions/gradle-5.0-bin.zip -P /tmp
RUN unzip -d /opt/gradle /tmp/gradle-*.zip
RUN ls /opt/gradle/gradle-5.0
RUN export GRADLE_HOME=/opt/gradle/gradle-5.0
RUN export PATH=${GRADLE_HOME}/bin:${PATH}
RUN /opt/gradle/gradle-5.0/bin/gradle 
