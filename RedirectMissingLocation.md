
- purpose: reproduce & solve bq load's RedirectMissingLocation issue
- bq cli version: 2.0.66


Step 1: create a table 
```
CREATE TABLE `<project_name>.<dataset_name>.games_post_wide`
AS SELECT * FROM `bigquery-public-data.baseball.games_post_wide` LIMIT 0
```

Step 2: export `bigquery-public-data.baseball.games_post_wide` data to GCS 

Step 3: download the csv file to local

Step 4: test to confirm the load succeed (this file is ~18MB)

```
bq --location=US load \
--source_format=CSV \
xxx:xxx.xxx \
xxx.csv
```

Step 5: make this file bigger than 100MB (run this multiple times)

```
cat tmp.csv >> large.csv
```

Step 6: Run `bq load` again, the below error will show

```
BigQuery error in load operation: Could not connect with BigQuery server due to: RedirectMissingLocation('Redirected but the response is missing a Location: header.')
```

Step 7: compress the file
```
gzip -k filename.csv
```

Step 8: run `bq load` again, if the compressed size is small enough, the load should succeed.