#! /usr/bin/env bash
#patch in the batch_importer_21
python handler.py
java -classpath "lib/*" -Dfile.encoding=UTF-8 org.neo4j.batchimport.Importer graph.db nodes.csv rels.csv,cpg_edges.csv

rm -rf /tmp/graph.db
mv graph.db /tmp
echo "[+] copy right"
