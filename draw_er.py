# -*- coding: utf-8 -*-
"""图书管理系统 E-R 图（陈氏表示法）绘制脚本"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, Polygon
import matplotlib.font_manager as fm

# ---------- 中文字体 ----------
def pick_cjk():
    candidates = ['SimHei', 'Microsoft YaHei', 'SimSun', 'KaiTi', 'FangSong',
                  'Noto Sans CJK SC', 'Source Han Sans SC']
    installed = {f.name for f in fm.fontManager.ttflist}
    for c in candidates:
        if c in installed:
            return c
    return None

font = pick_cjk()
if font:
    plt.rcParams['font.sans-serif'] = [font]
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(15, 10), dpi=150)
ax.set_xlim(-11, 11)
ax.set_ylim(-7.5, 7.5)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('图书管理系统 E-R 图（陈氏表示法）', fontsize=16)

# ---------- 绘图辅助 ----------
def entity(x, y, name, sub, w=2.1, h=1.0):
    ax.add_patch(Rectangle((x - w/2, y - h/2), w, h, fill=True,
                           facecolor='#EAF2FB', edgecolor='black', lw=1.3))
    ax.text(x, y + 0.18, name, ha='center', va='center', fontsize=13, fontweight='bold')
    ax.text(x, y - 0.24, sub, ha='center', va='center', fontsize=9, color='#333333')

def diamond(x, y, name, sub):
    dx, dy = 0.85, 0.55
    pts = [(x, y + dy), (x + dx, y), (x, y - dy), (x - dx, y)]
    ax.add_patch(Polygon(pts, closed=True, fill=True,
                         facecolor='#FFF4E5', edgecolor='black', lw=1.2))
    ax.text(x, y + 0.14, name, ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(x, y - 0.22, sub, ha='center', va='center', fontsize=8, color='#555555')

def attr(x, y, name, pk=False):
    n = len(name)
    w = max(1.15, 0.34 * n + 0.15)
    h = 0.62
    ax.add_patch(Ellipse((x, y), w, h, fill=False, edgecolor='black', lw=1.0))
    ax.text(x, y, name, ha='center', va='center', fontsize=10)
    if pk:
        uw = 0.30 * n * 0.5
        ax.plot([x - uw, x + uw], [y - 0.24, y - 0.24], color='black', lw=1.4)

def line(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color='black', lw=1.0, zorder=0)

def card(x, y, t):
    ax.text(x, y, t, ha='center', va='center', fontsize=12, fontweight='bold',
            color='#B00020')

# ---------- 实体 ----------
entity(0, -0.5, '图书', 'book')
entity(-6, 4.5, '图书类型', 'book_type')
entity(-6, -4.5, '出版社', 'publisher')
entity(6.5, -0.5, '读者', 'reader')

# ---------- 联系 ----------
diamond(-3, 2, '属于', 'belongs')
diamond(-3, -2.5, '出版', 'publish')
diamond(3.25, -0.5, '借阅', 'borrow')

# ---------- 实体-联系连线 + 基数 ----------
# 图书 -- 属于 -- 图书类型
line(0, -0.5, -3, 2); line(-3, 2, -6, 4.5)
card(-1.35, 0.55, 'n'); card(-4.6, 3.1, '1')
# 图书 -- 出版 -- 出版社
line(0, -0.5, -3, -2.5); line(-3, -2.5, -6, -4.5)
card(-1.35, -1.35, 'n'); card(-4.6, -3.65, '1')
# 图书 -- 借阅 -- 读者
line(0, -0.5, 3.25, -0.5); line(3.25, -0.5, 6.5, -0.5)
card(1.7, -0.25, 'n'); card(4.9, -0.25, 'm')

# ---------- 属性 ----------
# 图书类型
attr(-8.6, 5.4, '类型编号', pk=True); line(-6, 4.5, -8.6, 5.4)
attr(-8.6, 3.8, '类型名称');       line(-6, 4.5, -8.6, 3.8)

# 出版社
attr(-8.9, -2.6, '出版社编号', pk=True); line(-6, -4.5, -8.9, -2.6)
attr(-8.9, -3.7, '出版社名称');          line(-6, -4.5, -8.9, -3.7)
attr(-8.9, -4.8, '出版社地址');          line(-6, -4.5, -8.9, -4.8)
attr(-8.9, -5.9, '联系电话');            line(-6, -4.5, -8.9, -5.9)

# 读者
attr(9.4, 1.2, '读者编号', pk=True); line(6.5, -0.5, 9.4, 1.2)
attr(9.4, 0.1, '读者姓名');          line(6.5, -0.5, 9.4, 0.1)
attr(9.4, -1.0, '联系电话');         line(6.5, -0.5, 9.4, -1.0)
attr(9.4, -2.1, '读者类型');         line(6.5, -0.5, 9.4, -2.1)
attr(9.4, -3.2, '注册日期');         line(6.5, -0.5, 9.4, -3.2)

# 图书
attr(-2.6, -2.9, '书号', pk=True); line(0, -0.5, -2.6, -2.9)
attr(-1.3, -2.9, '书名');          line(0, -0.5, -1.3, -2.9)
attr(0.0, -2.9, '作者');           line(0, -0.5, 0.0, -2.9)
attr(1.3, -2.9, '单价');           line(0, -0.5, 1.3, -2.9)
attr(2.6, -2.9, '库存数量');       line(0, -0.5, 2.6, -2.9)

# 借阅联系属性
attr(3.25, 1.5, '借阅日期'); line(3.25, -0.5, 3.25, 1.5)
attr(3.25, 2.7, '归还日期'); line(3.25, -0.5, 3.25, 2.7)

fig.tight_layout()
fig.savefig('图书管理系统_ER图.png', bbox_inches='tight', facecolor='white')
print('saved 图书管理系统_ER图.png')
