import logging
from typing import Iterator, Dict, List
from src.integrations.geocode_util import get_structured_address

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def transform(
    address_iter: Iterator[Dict],
    api_key: str
) -> List[Dict]:
    """
    Take an iterator of records (each with 'project_address'),
    geocode them, and return a list of enriched records.
    """
    enriched: List[Dict] = []

    for rec in address_iter:
        addr = rec.get("project_address", "").strip()

        if not addr:
            logger.warning("No address for record, skipping geocode: %s", rec)
            rec.update({"full_address": None, "latitude": None, "longitude": None})
        else:
            try:
                geo = get_structured_address(addr, api_key)
            except Exception as e:
                logger.error("Geocode failed for '%s': %s", addr, e)
                geo = {"full_address": None, "latitude": None, "longitude": None}
            rec.update(geo)

        enriched.append(rec)

    return enriched
