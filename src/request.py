import requests
from src.config import REQUEST_MAX_ATTEMPTS
from src.log import logger
from requests import Timeout, RequestException
from src.domain2ip import get_ip_address
from bs4 import BeautifulSoup
from src.ip_info import ip_data


def get_page_title(url):
    # 发送HTTP请求
    attempts = 0
    while attempts < REQUEST_MAX_ATTEMPTS:
        try:
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
            # 解析HTML内容
            soup = BeautifulSoup(response.content, 'html.parser')
            # 获取标题
            title = soup.title.text
            return title.strip()
        except AttributeError as attribute_error:
            logger.debug(f"Request {url} attribute error")
            logger.debug(f"error info is: {attribute_error}")
            return None
        except Timeout as timeout_error:
            # 超时异常
            attempts += 1
            logger.debug(f"Request {url} Timeout!")
            logger.debug(f"error info is: {timeout_error}",)
            attempts += 1
        except RequestException as request_error:
            # 处理请求异常
            attempts += 1
            logger.debug(f"Request {url} failed!")
            logger.debug(f"error info is: {request_error}",)
    return ""


def request_subdomain_http(subdomain):
    attempts = 0
    while attempts < REQUEST_MAX_ATTEMPTS:
        try:
            url = f"http://{subdomain}"  # 使用HTTP协议
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
            title = get_page_title(url)  # 假设标题在响应文本中
            status_code = response.status_code
            ip = get_ip_address(subdomain)
            return title, status_code, url, subdomain, ip,
        except Timeout as timeout_error:
            # 超时异常
            logger.error(f"Request {url} Timeout!")
            logger.error(f"error info is: {timeout_error}",)
            attempts += 1
        except RequestException as request_error:
            # 处理请求异常
            logger.error(f"Request {url} failed!")
            logger.debug(f"error info is: {request_error}",)
            attempts += 1
    return None, None, None, None, None

def request_subdomain_https(subdomain):
    attempts = 0
    while attempts < REQUEST_MAX_ATTEMPTS:
        try:
            url = f"https://{subdomain}"  # 使用HTTPS协议
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
            title = get_page_title(url)  # 假设标题在响应文本中
            status_code = response.status_code
            ip = get_ip_address(subdomain)
            return title, status_code, url, subdomain, ip
        except Timeout as timeout_error:
            # 超时异常
            logger.error(f"Request {url} Timeout!")
            logger.error(f"error info is: {timeout_error}")
            attempts += 1
        except RequestException as request_error:
            logger.error(f"Request {url} failed!")
            logger.error(f"error info is: {request_error}")
            attempts += 1
            # 处理请求异常
    return None, None, None, None, None