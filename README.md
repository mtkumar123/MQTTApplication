# MQTTApplication

## Launching Application ##

In order to launch application follow these steps:
  - Make sure Docker is running, and then from the root directory of the project run **docker-compose build** in the terminal
  - After build process is completed run **docker-compose up** in the terminal
  - Application should be launched.

## Viewing Messages Published ##

In order to use the REST API endpoint to view messages published and stored in MongoDB follow these steps:
  - Navigate to **[localhost/docs](http://localhost/docs)** in a browser to view the FastAPI Swagger docs
  - Try out the GET /messages endpoint
  - You can also use the following command ```curl -X GET http://localhost/messages```

## Viewing MQTT Client Logs ##

In order to view the MQTT Client Logs either docker attach to the mqtt_client service or view them through Docker Desktop console, or [lazydocker](https://github.com/jesseduffield/lazydocker)

## Overview ##

### Services ###

**api_service**

FastAPI service with the GET /messages endpoint. The endpoint reads all the published messages for the topic which is stored in MongoDB and returns those messages to the user

**mqtt_client**

The client application which subscribes to the topic charger/1/connector/1/session/1, and publishes messages to that topic as well. Messages are published every 2 seconds. The on_message callback is used in the application to receive a published message and store it in MongoDB.

**mongodb**

Database service to store the published messages

**mosquitto**

MQTT Broker service
