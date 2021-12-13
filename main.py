from google.cloud import bigquery;
from pgsql import query
import sql
from config import pgsql_config

if __name__ == '__main__':
    client = bigquery.Client()
    run_query = client.query(
        """
        SELECT geo_id, sub_region_1 AS state, sub_region_2 AS county, AVG(retail_and_recreation_percent_change_from_baseline) AS sales_vector
        FROM bigquery-public-data.census_bureau_acs.county_2017_1yr
        INNER JOIN bigquery-public-data.covid19_google_mobility.mobility_report
        ON geo_id || '.0' = census_fips_code
        WHERE median_rent < 2000 AND median_age < 30
        GROUP BY geo_id, state, county
        HAVING sales_vector > -15
        --SELECT *
        --FROM `bigquery-public-data.stackoverflow.posts_questions`
        --ORDER BY view_count DESC
        --LIMIT 10;
        """
    )

    query(sql.create_schema, [""])

    query(sql.create_table, [""])

    for row in run_query.result():
        #dataset = []
        #dataset.append(row)
        query(sql.insert_data, row)
    #print(dataset)




