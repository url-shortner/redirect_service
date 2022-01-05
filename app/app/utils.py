from typing import Union

from .config import Config
from .elasticsearch import insertRedirectEvent
from .redis import fetchTargetUrl


def getRedirectUrl(url_id: str, config: Config) -> Union[str, None]:
    url = fetchTargetUrl(url_id, config.redis_host)
    if url is None:
        return None
    if not insertRedirectEvent(
        url_id=url_id,
        target_url=url,
        es_host=config.es_host,
        es_port=config.es_port,
        es_index=config.es_index,
    ):
        # TODO: Log this event as Critical
        return url
    return url
