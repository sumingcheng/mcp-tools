## MCP 工具简介

该项目是 MCP 工具示例项目，启动后你可以直接配置在 Cursor、Cherry-Studio 等支持 MCP 协议的工具或者模型上~

### Cursor 配置示例

```
{
  "mcpServers": {
    "MCP Tools": {
      "name": "MCP Tools",
      "type": "url",
      "description": "MCP 工具",
      "isActive": true,
      "url": "http://127.0.0.1:33669/sse/"
    }
  }
}
```

### 效果展示



### 时间相关工具
- **get_current_time_for_timezone**：获取指定时区的当前时间
- **convert_time_between_timezones**：将一个时区的时间转换为另一个时区
- **time_difference_between_timezones**：计算两个时区的时间差
- **is_leap_year**：判断指定年份是否为闰年

### 网络相关工具
- **ping_host**：检测与目标主机的网络连通性
- **get_local_ip**：获取本机 IP 地址信息
- **get_public_ip**：获取公网 IP 地址
- **dns_lookup**：执行 DNS 查询
- **check_port**：检查指定主机的端口是否开放
- **http_request**：发送 HTTP 请求并获取响应
- **download_file**：下载文件

### 数学计算工具
- **calculate**：执行基本的数学计算
- **advanced_calculate**：执行高级数学计算

