import json
from typing import Union

import redis as Redis


def fetchTargetUrl(url_id: str, redis_host: str) -> Union[str, None]:
    redis = Redis.Redis(host=redis_host)
    data = redis.get(url_id)
    if data is None:
        return None
    data_d = json.loads(data)
    return data_d["target_url"]
