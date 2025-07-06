import requests
import os
from typing import Dict
import logging
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    # retry=retry_if_exception_type(requests.RequestException),
    # only retry on real network/connection issues
    retry=retry_if_exception_type(requests.ConnectionError),
    reraise=True,
)

def get_structured_address(partial_address: str, api_key: str) -> Dict[str, str]:
    """ 
    Given a partial address, returns the full structured address using LocationIQ API.
    """
    if not partial_address:
        logger.warning("Empty address, skipping geocode.")
        return {"full_address": None, "latitude": None, "longitude": None}

    url = "https://us1.locationiq.com/v1/search.php"
    params = {
        "key": api_key,
        "q": partial_address,
        "format": "json",
        "limit": 1
    }
    try:
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
    except requests.HTTPError as e:
        # API returned 4xx/5xx → log & return fallback (no retry)
        logger.error("Geocode HTTP error for '%s': %s", partial_address, e)
        return {"full_address": None, "latitude": None, "longitude": None}
    except requests.RequestException as e:
        # connection‐level error → bubble up so Tenacity will retry
        logger.error("Geocode connection error for '%s': %s", partial_address, e)
        raise

    try:
        data = resp.json()
    except ValueError as e:
        logger.error("Invalid JSON response for '%s': %s", partial_address, e)
        return {"full_address": None, "latitude": None, "longitude": None}

    if not isinstance(data, list) or not data:
        logger.warning("No results for '%s'", partial_address)
        return {"full_address": None, "latitude": None, "longitude": None}

    item = data[0]
    return {
        "full_address": item.get("display_name"),
        "latitude": item.get("lat"),
        "longitude": item.get("lon"),
    }