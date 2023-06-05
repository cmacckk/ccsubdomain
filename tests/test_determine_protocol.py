import pytest
from src.protocol import determine_protocol


def test_determine_protocol():
    # 子域名使用HTTPS协议
    assert determine_protocol("www.baidu.com") == "https"

    # 子域名使用HTTP协议
    assert determine_protocol("www.example.com") == "http"