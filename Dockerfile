# FROM python:3-alpine
ARG python=python:3.7.4-slim-buster

FROM $python AS deploy

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apt-get update \
  && apt-get install -y wget unzip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744-linux.zip \
  && unzip -q sonar-scanner-cli-4.0.0.1744-linux.zip


EXPOSE 8080

CMD ["python3", "-m", "validationService"]

