# SVG Turtle Classic

[English Version](README.md) | [中文版本](README_zh.md)

![演示](demo.jpg)

## 致谢

本项目基于 Don Kirkby 的优秀作品 [SaVaGe Turtle](https://donkirkby.github.io/svg-turtle) 构建。特别感谢原作者创建了如此有用的库来生成海龟图形的SVG图形。

**原始仓库：** https://github.com/donkirkby/svg-turtle

## 概述

SVG Turtle Classic 是 svg-turtle 库的包装器，提供了与 Python 经典 tkinter turtle 模块兼容的更熟悉的接口。这个增强版本使得从传统海龟图形过渡到 Jupyter notebook中的 SVG 生成变得更加容易，特别适合在线教学环境。

## 主要特性

- **三种使用模式**：支持程序化、模块化和面向对象的风格，就像经典的海龟模块一样
- **无缝集成**：标准海龟命令的即插即用替代品
- **Jupyter 笔记本优化**：在 Jupyter 单元格中自动显示 SVG 输出
- **增强的 `done()` 函数**：自动添加最终海龟印记并显示结果
- **教育友好**：完美适用于编程教学和创建可视化
- **在线教学支持**：特别适合 code-server 演示和远程学习环境
- **兼容性**：`speed()` 方法可用于兼容旧代码，尽管它是一个空函数，因为此模块生成静态 SVG 输出而不支持动画

## 安装

本项目需要 svg-turtle 库作为依赖：

```bash
pip install svg_turtle
```

然后只需下载或克隆此仓库并导入 `svg_turtle_classic` 模块。

## 快速开始

```python
from svg_turtle_classic import *

# 设置画布大小
setup(600, 400)

# 绘制一个简单的正方形
pencolor('blue')
pensize(3)

for _ in range(4):
    forward(100)
    right(90)

# 完成并显示
done()
```

## 使用模式

SVG Turtle Classic 支持三种不同的使用模式：

### 1. 程序化风格

```python
from svg_turtle_classic import *
setup(600, 400)
forward(100)
right(90)
done()
```

### 2. 模块风格

```python
import svg_turtle_classic as stc
stc.setup(600, 400)
stc.forward(100)
stc.right(90)
stc.done()
```

### 3. 面向对象风格

```python
from svg_turtle_classic import Turtle
t = Turtle()
t.forward(100)
t.right(90)
done(t)
```

## 重要说明

- **无绘制动画**：与传统海龟图形不同，此模块生成静态 SVG 输出，没有绘制动画。命令被执行后显示最终结果。
- **速度方法**：包含 `speed()` 方法以兼容旧的海龟代码，但它是空函数，因为此模块不支持动画速度。
- **在线教学**：此模块特别适合在线教学环境，特别是 code-server 演示，学生可以立即看到其海龟图形代码的视觉结果。

## 演示和示例

有关综合示例和详细使用说明，请查看 `demo/` 目录中的演示文件：

- `demo/svg_turtle_classic_demo.ipynb` - 包含所有功能的完整演示笔记本
- `demo/svg_turtle_classic_demo_zh.ipynb` - 演示的中文版本

**重要提示**：此模块专门设计用于 Jupyter 笔记本（.ipynb 文件），其中可以正确显示 SVG 图形，在 code-server 等在线教学环境中特别有效。

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 贡献

欢迎贡献！请随时提交问题、功能请求或拉取请求。

---

*为 Python 教育社区而构建 ❤️*
