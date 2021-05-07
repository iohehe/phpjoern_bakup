#! /bin/bash

_path='neo4j-community-2.1.8/bin/neo4j';
_command='start-no-wait';

${_path} stop
${_path} ${_command}
