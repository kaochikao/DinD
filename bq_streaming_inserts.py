

from google.cloud import bigquery

sa_file = ''
table_id = ""

"""
Immediate after doing streaming inserts into BigQuery tables:
- the table might shows there's now rows.
- the streaming buffer might show estimated rows/bytes (still with a short delay)
"""

client = bigquery.Client.from_service_account_json(sa_file)

# TODO: add create table

rows_to_insert = [
    {u"full_name": u"Alice", u"age": 32},
    {u"full_name": u"Bob", u"age": 29},
]

errors = client.insert_rows_json(table=table_id, json_rows=rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))

# tables.get
tbl = client.get_table(table_id)

# https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource:-table
print("====Table stats====")
print("# rows in table: {}".format(tbl.num_rows))
print("# bytes in table: {}".format(tbl.num_bytes))
print()
print("====Buffer stats====")

# https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#streamingbuffer
if tbl.streaming_buffer:
    print(tbl.streaming_buffer)
    print("# rows in buffer: {}".format(tbl.streaming_buffer.estimated_rows))
    print("# bytes in buffer: {}".format(tbl.streaming_buffer.estimated_bytes))
else:
    print("No Streaming Buffer")



