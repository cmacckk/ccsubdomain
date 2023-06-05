import requests
from src.log import logger

def determine_protocol(subdomain):
    url_http = f"http://{subdomain}"
    url_https = f"https://{subdomain}"

    try:
        response = requests.head(url_https, allow_redirects=True, timeout=10)
        if response.status_code < 400:
            return "https"
    except requests.RequestException as request_exception:
        logger.debug("Determine protocol %s", request_exception)

    try:
        response = requests.head(url_http, allow_redirects=True, timeout=10)
        if response.status_code < 400:
            return "http"
    except requests.RequestException as request_exception:
        logger.debug("Determine protocol %s", request_exception)

    return "http"