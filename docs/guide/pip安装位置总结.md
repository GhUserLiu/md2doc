# pip 安装位置总结（简明版）

## 回答你的问题

### Q1: `pip install -r requirements.txt` 会把包安装在哪里？

**答案**：取决于你使用的是哪个 Python。

**当前你的情况：**
```bash
# 你正在使用的Python
C:\Users\liuzh\miniconda3\python.exe

# 包会安装到
C:\Users\liuzh\miniconda3\Lib\site-packages\
```

### Q2: 会与其他项目混合吗？

**答案**：**会的！** 除非你使用虚拟环境。

```
全局环境（混合在一起）：
miniconda3\Lib\site-packages\
├─ python-docx        ← md2doc项目用的
├─ requests           ← 其他项目A用的
├─ numpy              ← 其他项目B用的
└─ ... (所有项目的包混在一起)
```

## 解决方案：使用虚拟环境

```bash
# 创建虚拟环境（只在项目中）
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 安装包（现在会安装到项目内）
pip install -r requirements.txt
```

**现在的包位置：**
```
项目A/
└─ venv/Lib/site-packages/   ← 项目A的包

项目B/
└─ venv/Lib/site-packages/   ← 项目B的包
```

## 推荐做法

### ✅ 使用虚拟环境（推荐）
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
- ✅ 每个项目独立
- ✅ 不会冲突
- ✅ 易于管理

### ❌ 直接安装（不推荐）
```bash
pip install -r requirements.txt
```
- ❌ 所有项目混合
- ❌ 可能冲突
- ❌ 难以管理

## 详细说明

查看完整说明：[pip安装说明.md](./pip安装说明.md)

## 快速验证

```bash
# 查看当前Python路径
where python

# 查看包安装位置
pip show python-docx
# 看 "Location:" 字段
```

## 总结

| 安装方式 | 包位置 | 是否混合 |
|---------|--------|---------|
| 直接pip | `miniconda3\Lib\site-packages\` | ❌ 是 |
| 使用venv | `项目目录\venv\Lib\site-packages\` | ✅ 否 |

**推荐：使用虚拟环境！**
