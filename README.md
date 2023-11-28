# python-learn
# python-learn


pip 是 Python 的包管理工具，用于安装和管理 Python 库。它可以让你轻松地从 Python Package Index (PyPI) 安装和更新库。

在 macOS 上，如果你已经安装了 Python，那么你可能已经有了 pip。你可以通过在终端中输入以下命令来检查是否已经安装了 pip：

pip --version
如果你看到了 pip 的版本信息，那么说明你已经安装了 pip。如果没有安装，你可以通过以下步骤安装 pip：

打开终端（Terminal）。
输入以下命令以安装 pip：
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
安装 pip：
python3 get-pip.py
输入以下命令删除临时文件：
rm get-pip.py
现在，你已经成功安装了 pip。你可以使用 pip 命令来安装和管理 Python 库了。例如，要安装名为 requests 的库，只需在终端中输入：
pip install requests
