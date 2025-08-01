from pytz import all_timezones, timezone
from datetime import datetime
from fastmcp import FastMCP


def register_time_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_current_time_for_timezone", description="获取指定时区的当前时间"
    )
    def get_current_time_for_timezone(tz_name: str = "UTC") -> str:
        """获取指定时区的当前时间"""
        try:
            # 验证时区是否有效
            if tz_name not in all_timezones:
                return (
                    f"无效的时区：{tz_name}。请使用 pytz.all_timezones 中的有效时区。"
                )
            # 获取时区对象
            tz = timezone(tz_name)
            # 获取指定时区的当前时间
            current_time = datetime.now(tz)
            # 格式化时间为字符串
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            return f"{tz_name} 的当前时间：{formatted_time}"

        except Exception as e:
            return f"获取 {tz_name} 时区时间出错：{str(e)}"

    @mcp.tool(
        name="convert_time_between_timezones",
        description="将一个时区的时间转换为另一个时区的时间",
    )
    def convert_time_between_timezones(time_str: str, from_tz: str, to_tz: str) -> str:
        try:
            if from_tz not in all_timezones or to_tz not in all_timezones:
                return f"无效的时区：{from_tz} 或 {to_tz}。"
            from_tz_obj = timezone(from_tz)
            to_tz_obj = timezone(to_tz)
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=from_tz_obj
            )
            converted_dt = dt.astimezone(to_tz_obj)
            formatted_time = converted_dt.strftime("%Y-%m-%d %H:%M:%S")
            return f"{time_str} ({from_tz}) 转换为 {to_tz} 时间：{formatted_time}"
        except Exception as e:
            return f"时区转换出错：{str(e)}"

    @mcp.tool(
        name="time_difference_between_timezones",
        description="计算两个时区中指定时间的时间差",
    )
    def time_difference_between_timezones(
        start_time: str, end_time: str, start_tz: str, end_tz: str
    ) -> str:
        try:
            if start_tz not in all_timezones or end_tz not in all_timezones:
                return f"无效的时区：{start_tz} 或 {end_tz}。"
            start_tz_obj = timezone(start_tz)
            end_tz_obj = timezone(end_tz)
            start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=start_tz_obj
            )
            end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=end_tz_obj
            )
            diff = (end_dt - start_dt).total_seconds()
            return f"时间差：{diff} 秒 ({start_tz} 到 {end_tz})"
        except Exception as e:
            return f"计算时间差出错：{str(e)}"

    @mcp.tool(name="is_leap_year", description="判断指定年份是否为闰年")
    def is_leap_year(year: str) -> str:
        try:
            y = int(year)
            is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            return f"{year} {'是' if is_leap else '不是'}闰年"
        except Exception as e:
            return f"判断闰年出错：{str(e)}"
