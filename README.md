# 📚 ReadSite - 在线小说阅读系统

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Django](https://img.shields.io/badge/Django-6.x-092E20.svg)
![DRF](https://img.shields.io/badge/DRF-3.14+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

基于 Django + Django REST Framework 开发的轻量级在线小说阅读平台。支持小说阅读、分卷管理、插图画廊、积分签到系统，并提供完善的后台 RESTful API 与 Swagger 交互文档。

## ✨ 核心特性

- **📖 沉浸式阅读体验**：支持章节按分卷展示，自动记录用户阅读进度，支持章节书签。
- **📦 完善的下载系统**：按字数和插图数计算积分，支持打包下载纯文本 (TXT) 或 图文混合包 (ZIP)。
- **🎮 用户中心与积分机制**：内置每日签到、经验值与会员等级（LV0-LV6）系统。下载小说消耗积分。
- **🖼️ 插图画廊模式**：支持为特定分卷上传插图，并提供独立的画廊模式沉浸浏览。
- **⚙️ 全局系统控制**：基于单例模式的系统设置，支持后台一键切换注册模式（完全开放 / 邀请码注册 / 关闭注册）。
- **🛠️ 后台管理 API**：普通管理员可管理自己上传的书籍，超级管理员掌控全局，支持封禁/解封用户。
- **🔍 智能检索**：支持对书名、作者、标签的多维度搜索。

---

## 🛠️ 技术栈

- **后端框架**: Django 6.x
- **API 框架**: Django REST Framework (DRF)
- **数据库**: SQLite (默认，可轻松迁移至 MySQL/PostgreSQL)
- **API 文档**: `drf-spectacular` (Swagger UI & Redoc)
- **环境变量**: `python-dotenv`

---

## 📁 核心数据模型与逻辑

- **Book / Chapter / Illustration**: 书籍元数据、章节内容与插图，利用 Django Signals 自动统计总字数与插图总数。
- **UserProgress / Bookshelf / Bookmark**: 记录用户当前阅读到了哪一章，以及用户的个人书架和收藏夹。
- **UserPoints**: 扩展内置 User，管理用户的积分 (Point)、经验值 (Exp) 和等级。
- **GlobalSettings**: 全局设置，保证数据库中只有一条记录，控制整站级别的开关。

---

## 🚀 本地开发与快速开始

### 1. 克隆项目
```bash
git clone https://github.com/你的用户名/novel-reader.git
cd novel-reader
```

### 2. 创建并激活虚拟环境
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置环境变量
在项目根目录创建一个 `.env` 文件，填入以下内容：
```env
# --- 安全配置 ---
SECRET_KEY=填入一个复杂的随机字符串，不要外泄
# 开发时填 True，上线时填 False
DEBUG=True

# --- 允许访问的主机 ---
# 多个域名用逗号分隔，本地开发写 * 或者 127.0.0.1
# CSRF_TRUSTED_ORIGINS本地开发时可不写，settings.py会自动处理默认值
# 上线后，这两处都应该填写为你的域名，127.0.0.1应当被删除
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1,http://localhost,http://127.0.0.1:8000,http://localhost:8000
```

### 5. 初始化数据库与静态文件
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### 6. 创建超级管理员 (用于测试 API 和后台系统设置)
```bash
python manage.py createsuperuser
```

### 7. 启动服务
```bash
python manage.py runserver
```
现在，你可以访问 `http://127.0.0.1:8000` 浏览前台页面！

---

## 📖 API 文档

项目集成了 `drf-spectacular`，启动服务后，管理员/开发者可通过以下地址查看和调试 API：

- **Swagger UI (交互式文档)**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema 下载**: `http://127.0.0.1:8000/api/schema/`

---

## 🚢 部署建议 (生产环境)

准备将项目部署到服务器时，请注意以下几点：

1. **修改环境变量**：将 `.env` 中的 `DEBUG` 修改为 `False`。
2. **配置 ALLOWED_HOSTS**：将你的服务器 IP 或域名加入 `ALLOWED_HOSTS` 和 `CSRF_TRUSTED_ORIGINS`。
3. **更换数据库**：虽然 SQLite 适合轻量级使用，但在高并发下，建议在 `settings.py` 中更换为 **PostgreSQL** 或 **MySQL**。
4. **使用 WSGI 服务器**：不要使用 `runserver` 运行生产环境。推荐使用 **Gunicorn** 作为应用服务器，并使用 **Nginx** 作为反向代理并处理 `/static/` 和 `/media/` 静态资源目录。

```bash
# Gunicorn 启动示例
pip install gunicorn
gunicorn novel_proj.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！
1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 协议开源。
