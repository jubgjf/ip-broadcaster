import re
import subprocess


def get_ip() -> str:
    """获取通过 PPPoE 分配的 ip"""

    # 执行 `ip a` 结果
    ip_a = subprocess.check_output(["ip", "a"]).decode("utf-8")

    # pppoe 获得的 ip 所在的一行
    ip_line = re.search(r"inet .* ppp0", ip_a).group()

    # pppoe 获得的 ip
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_line).group()

    return ip
