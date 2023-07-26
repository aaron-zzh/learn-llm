# 《AI 大模型应用开发实战营》学习笔记

> 极客时间 彭靖田

课程内容包含理论基础、开发基础、应用实战、开源生态

- 技术栈：
  ![stack](./docs/img/stack.png)

本项目旨在指导你进行使用 OpenAI API 的应用开发的初始步骤。它将帮助你设置开发环境，理解如何使用API，并为你提供一个用于交互式开发的Jupyter Lab记事本。

## 快速开始

### 设置环境变量

为了使用 OpenAI API，你需要从 OpenAI 控制台获取一个 API 密钥, 为防止密钥泄露建议将其设置为环境变量使用：

方式 1. 通过 .env 文件设置

在 JupyterLab 启动目录下创建一个 .env 文件，内容：

```ini
MY_VAR=hello
OPENAI_API_KEY=your_api_key
```

a. 在 JupyterLab 中可以自动读取 .env 文件中的环境变量（变更需要重启 JupyterLab）。

```python
import os
print(os.getenv('MY_VAR')) # 输出 hello
```

b. 也可通过代码加载环境变量

```python
from dotenv import load_dotenv
load_dotenv()
print(os.getenv('MY_VAR')) # 输出 hello
```

方式 2. 在终端中临时设置

对于基于Unix的系统（如Ubuntu或MacOS），你可以在终端中运行以下命令：

```bash
export OPENAI_API_KEY='your_api_key'
```

对于Windows，你可以在命令提示符中使用以下命令：

```bash
# cmd
set OPENAI_API_KEY=your_api_key

# powershell
$env:OPENAI_API_KEY = "your_api_key"
```

请确保将`your_api_key`替换为你的实际 OpenAI API 密钥。

### 创建虚拟环境

```bash
python -m venv .venv
```

### 安装Jupyter Lab

我们将使用Jupyter Lab作为我们的交互式开发环境。你可以使用pip进行安装：

```bash
pip install jupyterlab
```

### 启动Jupyter Lab

切换到本项目录并通过运行以下命令启动Jupyter Lab：

```bash
cd openai-quickstart
jupyter-lab
```

这将启动 Jupyter Lab 并在你的默认网络浏览器中打开它。
