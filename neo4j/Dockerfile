FROM openjdk:8-jre
RUN apt-get update && apt-get install -y \
	net-tools \
	--no-install-recommends \
	apt-utils
ADD neo4j /usr/local/neo4j
ADD batch_importer_21  /usr/local/batch_importer_21
WORKDIR /usr/local/neo4j
