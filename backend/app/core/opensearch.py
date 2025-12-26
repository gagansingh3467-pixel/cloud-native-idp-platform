import os
from opensearchpy import OpenSearch

OPENSEARCH_URL = os.getenv("LOG_STORE_URL", "http://opensearch:9200")

client = OpenSearch(
    hosts=[OPENSEARCH_URL],
    http_compress=True,
    use_ssl=False,
    verify_certs=False
)
