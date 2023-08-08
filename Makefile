TOPIC := nlp
PARTITIONS := 1
REPLICATION_FACTOR := 1


create-topic:
	docker compose exec broker \
	  kafka-topics --create \
		--topic $(TOPIC) \
		--bootstrap-server localhost:9092 \
		--replication-factor $(REPLICATION_FACTOR) \
		--partitions $(PARTITIONS)

producer:
	docker exec --interactive --tty broker \
		kafka-console-producer --bootstrap-server broker:9092 \
	   	--topic $(TOPIC)

consumer:
	docker exec --interactive --tty broker \
		kafka-console-consumer --bootstrap-server broker:9092 \
        --topic $(TOPIC) \
        --from-beginning

#docker exec --interactive --tty broker \
#	kafka-console-consumer --bootstrap-server broker:9092 \
#	--topic nlp \
#	--from-beginning

run-kafka:
	docker-compose -f docker-compose-zoo-broker.yaml up -d broker
