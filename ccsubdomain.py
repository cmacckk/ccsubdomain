from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from src.request import request_subdomain_http, request_subdomain_https
from src.protocol import determine_protocol
from src.log import logger
from src.banner import output_banner
import pandas as pd


def determine_request(subdomain):
    protocol = determine_protocol(subdomain)
    if protocol == 'http':
        return request_subdomain_http(subdomain)
    else:
        return request_subdomain_https(subdomain)

# 主函数
def subdomain_info(subdomains, pool=5, output_xlsx = 'output.xlsx'):
    # 创建线程池
    results = []
    logger.info(f"启用{pool}个线程")
    with ThreadPoolExecutor(max_workers=pool) as executor:
        # 提交任务到线程池并获取Future对象列表
        futures = [executor.submit(determine_request, subdomain) for subdomain in subdomains]

        # 使用tqdm创建命令行进度条，并迭代Future对象列表
        for future in tqdm(futures, total=len(subdomains), desc="Testing alive"):
            # 获取每个任务的结果（这里假设任务都能正常完成）
            result = future.result()
            # 这里可以根据需要处理每个任务的结果
            results.append(result)
    df = pd.DataFrame(results)
    df.to_excel(output_xlsx, index=False, header=['标题', '状态码', 'URL', '子域名', 'ip地址'])
    logger.info(f"文件已保存到 ---> {output_xlsx}")


if __name__ == "__main__":
    output_banner()
    logger.info("get urls from urls.txt")
    with open('urls.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        subdomains = [line.strip() for line in lines if line.strip()]
        logger.info("读取urls.txt完成,开始爬取")
        subdomain_info(subdomains)