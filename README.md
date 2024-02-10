# cdc-postgres-to-mongodb

Description: use debezium to track changes in postgresql and write to mongodb.

Run the docker-compose.yaml file to start the services. Then run the connect.sh file. This file contains commands to connect debezium to postgres.
```console
docker compose up
chmod +x connect.sh
./connect.sh
```

Open a new terminal to add data. Must add data first to create a topic for kafka before it can run consumers.
```console
docker exec -it postgres sh
#: psql -U postgres -d movies_db -a -f execute.sql
```
Go back to the original terminal, download the necessary packages and run the consumer.
```console
pip install -r requirements.txt
python app/consumer.py
```

