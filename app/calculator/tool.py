import ast
import math
import operator
from app.common.mcp import mcp


@mcp.tool(name="calculate", description="执行基本的数学计算，支持加减乘除和幂运算")
def calculate(expression: str) -> str:
    """
    执行基本的数学计算

    参数:
        expression: 数学表达式字符串，例如 "1 + 2", "3 * 4", "10 / 2", "2 ^ 3"

    返回:
        计算结果或错误信息
    """
    try:
        # 移除所有空格
        expression = expression.replace(" ", "")

        # 检查是否包含加法
        if "+" in expression:
            parts = expression.split("+")
            if len(parts) != 2:
                return "错误：只支持两个操作数的加法"
            return str(float(parts[0]) + float(parts[1]))

        # 检查是否包含减法
        elif "-" in expression and expression.count("-") == 1:
            parts = expression.split("-")
            if len(parts) != 2:
                return "错误：只支持两个操作数的减法"
            return str(float(parts[0]) - float(parts[1]))

        # 检查是否包含乘法
        elif "*" in expression:
            parts = expression.split("*")
            if len(parts) != 2:
                return "错误：只支持两个操作数的乘法"
            return str(float(parts[0]) * float(parts[1]))

        # 检查是否包含除法
        elif "/" in expression:
            parts = expression.split("/")
            if len(parts) != 2:
                return "错误：只支持两个操作数的除法"
            if float(parts[1]) == 0:
                return "错误：除数不能为零"
            return str(float(parts[0]) / float(parts[1]))

        # 检查是否包含幂运算
        elif "^" in expression:
            parts = expression.split("^")
            if len(parts) != 2:
                return "错误：只支持两个操作数的幂运算"
            return str(float(parts[0]) ** float(parts[1]))

        else:
            return "错误：不支持的运算。支持的运算符有：+, -, *, /, ^"

    except ValueError:
        return "错误：输入包含无效数字"
    except Exception as e:
        return f"计算错误：{str(e)}"


@mcp.tool(name="advanced_calculate", description="执行高级数学计算，支持多步骤运算")
def advanced_calculate(expression: str) -> str:
    """
    执行高级数学计算，支持多步骤运算

    参数:
        expression: 数学表达式字符串，例如 "(1 + 2) * 3", "sin(30)", "sqrt(16)"

    返回:
        计算结果或错误信息
    """
    # 定义允许的数学函数
    math_functions = {
        "abs": abs,
        "round": round,
        "min": min,
        "max": max,
        "pow": pow,
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "log10": math.log10,
        "exp": math.exp,
        "floor": math.floor,
        "ceil": math.ceil,
    }

    # 定义允许的常量
    constants = {
        "pi": math.pi,
        "e": math.e,
    }

    # 定义允许的运算符
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,  # 支持负号
    }

    def eval_node(node):
        """递归评估 AST 节点"""
        if isinstance(node, ast.Num):  # 数字
            return node.n
        elif isinstance(node, ast.BinOp):  # 二元运算
            left = eval_node(node.left)
            right = eval_node(node.right)
            op = operators[type(node.op)]
            return op(left, right)
        elif isinstance(node, ast.UnaryOp):  # 一元运算（如负号）
            operand = eval_node(node.operand)
            op = operators[type(node.op)]
            return op(operand)
        elif isinstance(node, ast.Name):  # 常量
            if node.id in constants:
                return constants[node.id]
            raise NameError(f"未定义的常量: {node.id}")
        elif isinstance(node, ast.Call):  # 函数调用
            if isinstance(node.func, ast.Name) and node.func.id in math_functions:
                args = [eval_node(arg) for arg in node.args]
                func = math_functions[node.func.id]
                return func(*args)
            raise NameError(f"未定义的函数: {node.func.id}")
        else:
            raise TypeError("不支持的语法")

    try:
        # 替换 ^ 为 **，支持幂运算
        expression = expression.replace("^", "**")
        # 解析表达式为 AST
        tree = ast.parse(expression, mode="eval")
        # 计算结果
        result = eval_node(tree.body)
        return str(result)
    except SyntaxError:
        return "错误：表达式语法错误"
    except NameError as e:
        return f"错误：{str(e)}"
    except TypeError:
        return "错误：不支持的语法"
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except Exception as e:
        return f"计算错误：{str(e)}"
