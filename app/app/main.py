from functools import lru_cache

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.responses import RedirectResponse

from .config import Config
from .utils import getRedirectUrl

app = FastAPI()


# Last read cache to ensure config is only loaded one
@lru_cache()
def get_config():
    return Config()


@app.get("/{url_id}")
def redirect(
    url_id: str,
    config: Config = Depends(get_config),  # type: ignore
):
    url = getRedirectUrl(url_id, config=config)
    if url is None:
        return HTTPException(404, "URL not found")
    return RedirectResponse(url)
