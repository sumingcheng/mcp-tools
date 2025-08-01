import platform
import socket
import httpx
import subprocess
import dns.resolver
import psutil
from typing import List, Dict, Optional
from fastmcp import FastMCP


def register_system_tools(mcp: FastMCP):
    @mcp.tool(name="ping_host", description="检测与目标主机的网络连通性")
    def ping_host(host: str, count: int = 4) -> str:
        try:
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param, str(count), host]
            result = subprocess.run(command, text=True, capture_output=True, timeout=10)
            return result.stdout
        except Exception as e:
            return f"Ping失败: {str(e)}"

    @mcp.tool(name="get_local_ip", description="获取本机IP地址信息")
    def get_local_ip() -> str:
        try:
            interfaces = {}
            for interface, addrs in psutil.net_if_addrs().items():
                ip_list = []
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        ip_list.append(addr.address)
                if ip_list:
                    interfaces[interface] = ip_list
            return "\n".join(
                [
                    f"{interface}: {', '.join(ips)}"
                    for interface, ips in interfaces.items()
                ]
            )
        except Exception as e:
            return f"获取本地IP失败: {str(e)}"

    @mcp.tool(name="get_public_ip", description="获取公网IP地址")
    def get_public_ip() -> str:
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get("https://api.ipify.org")
                response.raise_for_status()
                return response.text.strip()
        except httpx.TimeoutException:
            return "获取公网IP失败: 请求超时"
        except httpx.HTTPStatusError as e:
            return f"获取公网IP失败: HTTP错误 {e.response.status_code}"
        except httpx.RequestError as e:
            return f"获取公网IP失败: 网络连接错误 {str(e)}"
        except Exception as e:
            return f"获取公网IP失败: {str(e)}"

    @mcp.tool(name="dns_lookup", description="执行DNS查询")
    def dns_lookup(domain: str, record_type: str = "A") -> str:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            return "\n".join(
                [f"{domain} {record_type} 记录: {answer}" for answer in answers]
            )
        except Exception as e:
            return f"DNS查询失败: {str(e)}"

    @mcp.tool(name="check_port", description="检查指定主机的端口是否开放")
    def check_port(host: str, port: int, timeout: float = 2.0) -> str:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            if result == 0:
                return f"端口 {port} 在主机 {host} 上是开放的"
            else:
                return f"端口 {port} 在主机 {host} 上是关闭的"
        except Exception as e:
            return f"端口检查失败: {str(e)}"

    @mcp.tool(name="http_request", description="发送HTTP请求并获取响应")
    def http_request(
        url: str,
        method: str = "GET",
        headers: Optional[Dict] = None,
        data: Optional[Dict] = None,
    ) -> str:
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.request(
                    method=method.upper(),
                    url=url,
                    headers=headers or {},
                    json=data if method.upper() in ["POST", "PUT", "PATCH"] else None,
                    params=data if method.upper() == "GET" else None,
                )
                response.raise_for_status()
                return f"状态码: {response.status_code}\n内容: {response.text[:500]}{'...' if len(response.text) > 500 else ''}"
        except httpx.TimeoutException:
            return "HTTP请求失败: 请求超时(30秒)"
        except httpx.HTTPStatusError as e:
            return f"HTTP请求失败: HTTP错误 {e.response.status_code} - {e.response.text[:100]}"
        except httpx.RequestError as e:
            return f"HTTP请求失败: 网络连接错误 {str(e)}"
        except Exception as e:
            return f"HTTP请求失败: {str(e)}"

    @mcp.tool(name="download_file", description="下载文件")
    def download_file(url: str, filename: str) -> str:
        try:
            with httpx.Client(timeout=30.0) as client:
                with client.stream("GET", url) as response:
                    response.raise_for_status()
                    with open(filename, "wb") as f:
                        for chunk in response.iter_bytes():
                            f.write(chunk)
            return f"文件已成功下载到 {filename}"
        except httpx.TimeoutException:
            return "文件下载失败: 请求超时(30秒)"
        except httpx.HTTPStatusError as e:
            return f"文件下载失败: HTTP错误 {e.response.status_code}"
        except httpx.RequestError as e:
            return f"文件下载失败: 网络连接错误 {str(e)}"
        except IOError as e:
            return f"文件下载失败: 文件写入错误 {str(e)}"
        except Exception as e:
            return f"文件下载失败: {str(e)}"
