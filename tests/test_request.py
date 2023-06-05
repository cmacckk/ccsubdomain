from src.request import request_subdomain_http, request_subdomain_https
import pytest

@pytest.mark.parametrize("subdomain", [
    "baidu.com",
    "test.demode",
    "www.jd.com"
])
def test_request_subdomain_http(subdomain):
    # 请求成功的情况
    title, status_code = request_subdomain_http(subdomain)
    assert title is not None
    assert status_code is not None

    # 三次连续异常的情况
    title, status_code = request_subdomain_http(subdomain)
    assert title is None
    assert status_code is None

@pytest.mark.parametrize("subdomain", [
    "baidu.com",
    "test.demode",
    "www.jd.com"
])
def test_request_subdomain_https(subdomain):
    # 请求成功的情况
    title, status_code = request_subdomain_https(subdomain)
    assert title is not None
    assert status_code is not None

    # 三次连续异常的情况
    title, status_code = request_subdomain_https(subdomain)
    assert title is None
    assert status_code is None