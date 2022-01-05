from datetime import datetime
from elasticsearch import Elasticsearch


def insertRedirectEvent(
    url_id: str,
    target_url: str,
    es_host: str,
    es_port: int,
    es_index: str,
) -> bool:

    es = Elasticsearch([f"http://{es_host}:{es_port}"])
    data = {"url_id": url_id, "target_url": target_url, "timestamp": datetime.now()}

    try:
        es.index(index=es_index, document=data)
    except Exception:
        return False
    return True
