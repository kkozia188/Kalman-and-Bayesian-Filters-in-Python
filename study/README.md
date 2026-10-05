# 卡尔曼滤波学习记录

本仓库是 Roger R. Labbe 的 [Kalman and Bayesian Filters in Python](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) 的 fork。原书正文位于根目录的 Jupyter Notebook 中；我们的中文笔记和学习进度放在 `study/` 中。

## 第一轮学习路线

按 **1 → 2 → 3 → 4 → 5 → 6 → 8** 的顺序学习。第 7 章按需查阅，完成第 8 章后再回头补推导。

| 章节 | 本轮目标 | 状态 |
|---|---|---|
| 1：g-h 滤波 | 用自己的话解释预测、残差和修正；观察 g、h 的影响 | 待开始 |
| 2：离散贝叶斯滤波 | 手算一次测量更新和运动预测 | 待开始 |
| 3：高斯分布 | 理解均值、方差及高斯分布的乘积 | 待开始 |
| 4：一维卡尔曼滤波 | 实现一维预测与更新，解释增益的含义 | 待开始 |
| 5：多元高斯分布 | 理解协方差，以及位置和速度之间的相关性 | 待开始 |
| 6：多维卡尔曼滤波 | 建立位置—速度模型，解释 F、H、P、Q、R | 待开始 |
| 8：滤波器设计 | 完成一个模拟跟踪案例，比较不同噪声参数的结果 | 待开始 |

完成第一轮后，再按兴趣学习第 9～12 章的非线性滤波，以及第 13～14 章的平滑和自适应滤波。

## 每次学习的方式

1. 阅读一小节，用自己的话解释它解决的问题。
2. 运行对应代码，先看默认结果。
3. 一次只修改一个参数；运行前写下预期，运行后记录观察。
4. 尝试练习，再对照原书答案。
5. 记录尚未理解的问题，下次从这些问题继续。

读过、运行过和能独立解释是不同的进度。只有完成章节目标后，才将状态改为“完成”。

## 学习入口

- [第 1 章原文](../01-g-h-filter.ipynb)
- [第 1 章笔记与实验记录](notes/01-g-h-filter.md)
- [原书目录](../table_of_contents.ipynb)
- [原书运行与安装说明](../README.md#downloading-and-running-the-book)

## 在 JupyterLab 中学习

使用独立的 `.venv` 环境。依赖的精确版本保存在 [requirements.lock](requirements.lock) 中；依赖选择保存在 [requirements.in](requirements.in) 中。

首次安装或重建环境（需要 Python 3.10 和 `uv`）：

```bash
cd ~/Kalman-and-Bayesian-Filters-in-Python
uv venv --python python3.10 .venv
uv pip sync study/requirements.lock --python .venv/bin/python
.venv/bin/python -m ipykernel install --prefix "$PWD/.venv" --name python3 --display-name 'Python (Kalman Study)'
```

启动：

```bash
./study/start-lab.sh
```

打开终端输出的带 token 的链接。服务默认使用本机端口 `8888`，打开后进入第一章。若端口已被占用，可使用 `KALMAN_JUPYTER_PORT=8889 ./study/start-lab.sh`。

在 WSL 中运行时，可以从 Windows 浏览器打开 `localhost` 链接。

Notebook 右上角的内核应为 **Python (Kalman Study)**。选中代码单元后按 **Shift+Enter**，执行代码并移动到下一格。建议按原书顺序执行；重新开始实验时，使用 **Kernel → Restart Kernel and Clear Outputs of All Cells**。

左侧文件列表可以打开 `study/notes/01-g-h-filter.md`，用于记录自己的解释和实验结果。修改实验代码前，可以用 **File → Save Notebook As** 将副本保存到仓库根目录，命名为 `01-g-h-filter-practice.ipynb`。放在根目录可以直接使用原书的绘图模块和样式文件。

环境验证：第一章的 52 个代码单元已通过完整执行，包括绘图和交互控件代码。验证输出保存在本地 `study/.runtime/`，不提交到 Git。其他章节将在学习时逐章验证。

如果使用当前机器上已配置的后台服务，可用下面的命令管理：

```bash
systemctl --user status kalman-study-jupyter
systemctl --user stop kalman-study-jupyter
```

该后台服务不会在重启机器后自动启动。重启后可以用 `./study/start-lab.sh` 在终端启动。
