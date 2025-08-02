## MCP Tools Introduction

This project is an MCP tools sample project. After starting, you can directly configure it on tools or models that support the MCP protocol, such as Cursor, Cherry-Studio, etc.
In the future, it will be developed in the direction of Dify MCP toolset.

### Cursor Configuration Example

```
{
  "mcpServers": {
    "MCP Tools": {
      "name": "MCP Tools",
      "type": "url",
      "description": "MCP Tools",
      "isActive": true,
      "url": "http://127.0.0.1:33669/sse/"
    }
  }
}
```

### Demo

<img width="976" height="709" alt="image" src="https://github.com/user-attachments/assets/fc9f469f-0a10-44a2-82e3-9f561b2aace8" />


### Time-related Tools
- **get_current_time_for_timezone**: Get current time for a specified timezone
- **convert_time_between_timezones**: Convert time from one timezone to another
- **time_difference_between_timezones**: Calculate time difference between two timezones
- **is_leap_year**: Determine if a specified year is a leap year

### Network-related Tools
- **ping_host**: Check network connectivity with target host
- **get_local_ip**: Get local IP address information
- **get_public_ip**: Get public IP address
- **dns_lookup**: Perform DNS lookup
- **check_port**: Check if a port on a specified host is open
- **http_request**: Send HTTP requests and get responses
- **download_file**: Download files

### Math Calculation Tools
- **calculate**: Perform basic math calculations
- **advanced_calculate**: Perform advanced math calculations

## Local Development

```
uv sync
python main.py
```

## Local Build

```
# Build image
make build 
# Start
make up 
```

## Contribution

Any form of PR is welcome