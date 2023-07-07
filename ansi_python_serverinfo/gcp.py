from google.cloud import bigquery

def connect_to_bigquery(url, json_key_path):
    # Create a client using the URL and JSON authentication
    credentials = bigquery.Credentials.from_service_account_info(url)
    client = bigquery.Client(credentials=credentials)

    # Extract the project ID from the credentials
    project_id = credentials.project_id

    return client, project_id

def display_project_details(client):
    # Get the project details
    project = client.project

    print("Connected to project ID:", project)
    print("Datasets in the project:")

    # List datasets in the project
    datasets = client.list_datasets()

    for dataset in datasets:
        print(dataset.dataset_id)

# URL and JSON authentication path
url = {
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "your-private-key",
    "client_email": "your-client-email",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "your-client-cert-url"
}
json_key_path = 'path/to/your/json_key.json'

# Connect to BigQuery
client, project_id = connect_to_bigquery(url, json_key_path)

# Display project details
display_project_details(client)
