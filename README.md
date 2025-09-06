# 智能绘画角色推荐系统-CharacterDrawingRecommender

一个帮助画师根据多种因素智能推荐每日绘画角色的Windows桌面应用程序。

## 功能特性

- 🎨 智能角色推荐算法
- 📊 多维度评分系统（喜爱度、稀缺性、人气等）
- 📅 特殊日期加成（生日、作品发布日）
- 🎯 月度目标管理
- 📈 创作数据统计和可视化
- 💾 SQLite数据库存储

## 技术栈

- Python 3.8+
- PyQt5 (GUI框架)
- SQLite (数据存储)
- Matplotlib (数据可视化)
- PyInstaller (打包工具)

## 安装和运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 生成演示数据（可选）：
```bash
python demo_data.py
```

3. 运行程序：
```bash
python main.py
```

## 项目结构

```
CDR/
├── main.py                 # 程序入口
├── database/
│   ├── __init__.py
│   └── database_manager.py # 数据库管理
├── models/
│   ├── __init__.py
│   └── character.py        # 角色模型
├── algorithms/
│   ├── __init__.py
│   └── recommendation.py   # 推荐算法
├── ui/
│   ├── __init__.py
│   ├── main_window.py      # 主界面
│   ├── character_management.py # 角色管理界面
│   ├── history_view.py     # 历史记录界面
│   └── statistics_view.py  # 统计界面
├── utils/
│   ├── __init__.py
│   └── helpers.py          # 工具函数
├── data/
│   └── characters.db       # SQLite数据库
└── requirements.txt        # 依赖文件
```

## 推荐算法

系统使用多维度评分算法，考虑以下因素：

- 基础喜爱度 (30%)
- 作品喜爱度 (25%)
- 创作稀缺性 (20%)
- 社区人气 (15%)
- 时间衰减因子 (10%)
- 特殊日期加成
- 鸽了补偿
- 月度目标加成

## 许可证

MIT License
