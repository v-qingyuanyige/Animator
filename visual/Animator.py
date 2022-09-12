import matplotlib.pyplot as plt


class Animator:
    '''
    用于在1个figure画布上动态绘制最多4条折线

    xlable: str             X轴的标签
    ylable: str             Y轴的标签
    xlim: tuple(2)          X轴坐标范围
    ylim: tuple(2)          Y轴坐标范围
    legend: list            折线的图例，有几条折线就需要几个图例
    fmts: tuple of str      每条折线的样式

    self.X: list            axes中每个节点的X坐标
    self.Y: list of lists   N个列表存储axes中N条折线的Y坐标
    '''

    def __init__(self, xlabel=None, ylabel=None, xlim=None, ylim=None,
                 xscale='linear', yscale='linear', legend=None, fmts=('go-', 'r+--', 'b.-.', '^:'),
                 nrows=1, ncols=1):
        self.fig, self.axes = plt.subplots(nrows, ncols)
        # 默认只支持1个axes
        if nrows * ncols == 1:
            self.axes = [self.axes, ]
        # 使用lambda为axes设置参数
        self.set_axes_config = lambda: set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.fmts = fmts
        self.X = None
        self.Y = None

    def show(self):
        self.fig.show()

    '''
    向axes里的每一条折线动态添加一个节点

    x: scalar
    y: tuple of scalar          有几条折线，y里就有几个元素
    '''

    def add(self, x, y):
        n = len(y)
        # 第一次调用时初始化X和Y列表
        if not self.X:
            self.X = []
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        if x is not None and y is not None:
            self.X.append(x)
            count = 0
            for item in y:
                self.Y[count].append(item)
                count = count + 1

        axes_plot(self.axes[0], self.X, self.Y, self.fmts)
        self.set_axes_config()
        self.show()


def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()


'''
x是列表，Y是列表的列表（4个列表，每个列表存储一条折线的全部节点）
'''


def axes_plot(axes, X, Y, fmts):
    axes.cla()
    n = len(Y)
    # 绘制N条折线
    for i in range(n):
        axes.plot(X, Y[i], fmts[i])
