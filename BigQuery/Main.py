#!/usr/bin/python

import sys
import os

from google.cloud import bigquery

def main():
    client = bigquery.Client()
    query_job = client.query("""
        SELECT
          name, gender,
          SUM(number) AS total
        FROM
          `bigquery-public-data.usa_names.usa_1910_2013`
        GROUP BY
          name, gender
        ORDER BY
          total DESC
        LIMIT
          10""")

    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print(row)


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sunnysun/Documents/work/firebase/JBLHeadphoneProd-68a9a1b7c215.json"
    main()