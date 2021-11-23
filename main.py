import argparse
import os

# from google.cloud import bigquery
# from google.oauth2 import service_account

environment = os.environ.get("ENVIRONMENT")

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str)

args = parser.parse_args()
filename = args.filename

# retrieve secret value her


def create_or_update_view(filename):
    with open(filename) as f:
        query = f.read().format(ENVIRONMENT=environment)

    # credentials = service_account.Credentials.from_service_account_info(bq_credentials)
    # bq_client = bigquery.Client(
    #     credentials=credentials, project=f"data-{environment}-warehouse"
    # )

    # query_job = bq_client.query(query)
    # query_job.result()
    # create view here
    print(query)


if __name__ == "__main__":
    create_or_update_view(str(filename))
