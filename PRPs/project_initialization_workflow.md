# 工作流程：项目初始化 (V3 - 加入索引步骤)

本工作流程文档旨在规范新项目的初始化过程，确保所有项目在启动时都具备一致的基础结构和核心文档。

---

## 阶段零：项目前置索引 (Project Prerequisite: Indexing)

**目标**：确保项目文件已被正确索引，以便后续的开发工具（如符号查找、文件搜索）能够正常工作。**这是所有操作开始前的强制步骤。**

**工具**：Shell / Terminal

**执行步骤**：
1.  打开您的终端。
2.  执行以下命令来对项目进行索引。

    **注意**: 请根据您本地 `serena` 项目的实际路径修改 `--directory` 参数。

    ```shell
    uv run --directory /Users/laobaibai/Documents/GitHub/serena serena project index
    ```
3.  等待命令执行完成。成功后，即可开始后续阶段。

---

## 阶段一：环境检查

**目标**：确认项目是否已经初始化。

**工具**：`check_onboarding_performed`

**执行步骤**：
1. 在开始任何操作之前，首先调用 `check_onboarding_performed` 工具。
2. **判断**：
    - 如果返回 `true`：说明项目已经存在，并已完成初始化。此时应终止本流程，并向用户报告项目已存在。
    - 如果返回 `false`：说明项目是全新的，需要进行初始化。请继续执行阶段二。

---

## 阶段二：核心文档创建

**目标**：建立项目的两大核心文档 `README.md` 和 `CLAUDE.md`。

**工具**：`edit_file` (使用 `create` 模式)

### 任务 2.1：创建 `README.md`

1. **操作**：调用 `edit_file` 工具，在项目根目录创建 `README.md` 文件。
    ```json
    {
      "display_description": "Create project README file",
      "path": "pokemonBot/README.md",
      "mode": "create"
    }
    ```
2. **内容**：使用以下模板填充文件内容，确保项目有一个专业、信息丰富的门面。

    ```markdown
    # 项目标题 (Project Title)

    <!-- 简短的项目描述 -->
    <p align="center">
      一个简洁、清晰、引人注目的项目介绍。说明这个项目是做什么的，以及它解决了什么核心问题。
    </p>

    <!-- 项目状态徽章 -->
    <p align="center">
      <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status">
      <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
      <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    </p>

    <br>

    ## 目录 (Table of Contents)
    * [关于项目 (About The Project)](#关于项目)
      * [技术栈 (Built With)](#技术栈)
    * [快速上手 (Getting Started)](#快速上手)
      * [先决条件 (Prerequisites)](#先决条件)
      * [安装步骤 (Installation)](#安装步骤)
    * [使用方法 (Usage)](#使用方法)
    * [贡献指南 (Contributing)](#贡献指南)
    * [许可证 (License)](#许可证)
    * [联系我们 (Contact)](#联系我们)

    ---

    ## 关于项目 (About The Project)

    在这里详细介绍您的项目。可以讲述项目的背景、功能亮点，以及为什么您要创建这个项目。这部分是吸引用户的关键。

    ### 技术栈 (Built With)
    列出构建此项目所使用的主要框架、库和技术。
    * [Node.js](https://nodejs.org/)
    * [MongoDB](https://www.mongodb.com/)
    * [Jest](https://jestjs.io/)

    ---

    ## 快速上手 (Getting Started)
    这部分是用户的操作手册，指导他们如何在本地运行您的项目。

    ### 先决条件 (Prerequisites)
    列出运行项目所需的所有软件和工具，并提供安装命令示例。
    * npm
      ```sh
      npm install npm@latest -g
      ```

    ### 安装步骤 (Installation)
    1. 克隆仓库
        ```sh
        git clone https://github.com/your_username/project_name.git
        ```
    2. 安装 NPM 包
        ```sh
        npm install
        ```
    3. 在 `.env` 文件中配置您的环境变量
        ```
        TELEGRAM_BOT_TOKEN = 'ENTER YOUR TOKEN';
        MONGO_URI = 'ENTER YOUR CONNECTION STRING';
        ```

    ---

    ## 使用方法 (Usage)
    提供一些代码示例或操作截图，向用户展示项目的实际用途和功能。

    ---

    ## 贡献指南 (Contributing)
    1. Fork 本项目
    2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
    3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
    4. 推送到分支 (`git push origin feature/AmazingFeature`)
    5. 开启一个 Pull Request

    ---

    ## 许可证 (License)
    本项目采用 MIT 许可证。

    ---

    ## 联系我们 (Contact)
    您的名字 - @your_twitter - email@example.com
    项目链接: [https://github.com/your_username/project_name](https://github.com/your_username/project_name)
    ```

### 任务 2.2：创建 `CLAUDE.md`

1. **操作**：调用 `edit_file` 工具，在项目根目录创建 `CLAUDE.md` 文件。
    ```json
    {
      "display_description": "Create project knowledge base file CLAUDE.md",
      "path": "pokemonBot/CLAUDE.md",
      "mode": "create"
    }
    ```
2. **内容**：使用以下标准模板创建项目核心知识库，确保关键信息被系统地记录下来。

    ```markdown
    # 📖 CLAUDE.md - [项目名] 项目核心知识库

    > **最后更新**: YYYY-MM-DD
    > **维护者**: @your_username
    > **核心原则**: 本文档是 AI 工程师的事实基础 (Ground-Truth)。所有信息都应保持最新、准确、无歧义。

    ---

    ## 1. 🚀 项目速览 (Project Quick Look)

    ### 1.1. 项目使命 (Mission)
    *   **一句话概括**: [项目的一句话简介]
    *   **解决的核心问题**: [项目旨在解决什么问题]

    ### 1.2. 关键技术栈 (Core Tech Stack)
    *   **语言**: Node.js
    *   **框架 / 主要库**: node-telegram-bot-api
    *   **数据库**: MongoDB (通过 Mongoose)
    *   **测试**: Jest
    *   **其他关键依赖**: axios, pino

    ### 1.3. 核心概念与术语 (Core Concepts & Glossary)
    *   **[术语A]**: [术语A的定义和解释]
    *   **[术语B]**: [术语B的定义和解释]

    ---

    ## 2. 🏛️ 架构与设计决策 (Architecture & Design Decisions)

    ### 2.1. 核心设计模式 (Key Design Patterns)
    *   **[模式A]**: [描述该模式在项目中的应用和原因]

    ### 2.2. 重要决策日志 (Decision Log - ADR-like)
    *   **决策日期**: [YYYY-MM-DD]
    *   **决策内容**: [我们决定采用X技术，因为...]
    *   **背景**: [当时面临的问题或选项]
    *   **后果**: [这个决策带来了什么正面或负面的影响]

    ---

    ## 3. 🔧 环境与配置 (Environment & Configuration)

    ### 3.1. 环境变量 (`.env`)
    *   `TELEGRAM_BOT_TOKEN`: **(必需)** Telegram Bot 的 API Token。
    *   `MONGO_URI`: **(必需)** MongoDB 的连接字符串。

    ### 3.2. 项目启动与测试命令
    *   **启动服务**: `npm start`
    *   **运行所有测试**: `npm test`
    *   **代码格式化**: `npm run format`
    *   **代码风格检查与修复**: `npm run lint`

    ---

    ## 4. 📜 编码约定与最佳实践 (Coding Conventions & Best Practices)

    ### 4.1. 命名约定
    *   [e.g., 变量使用驼峰命名法 (camelCase)]

    ### 4.2. 日志记录 (Logging)
    *   [e.g., 使用 `pino` 记录日志，关键业务操作必须有日志]

    ### 4.3. 错误处理 (Error Handling)
    *   [e.g., 异步操作必须使用 try/catch 包裹]

    ---

    ## 5. ⚠️ 已知陷阱与“非显而易见”的知识 (Known Pitfalls & "Non-Obvious" Knowledge)

    *   **[陷阱A]**: [描述一个容易出错的地方以及如何避免]
    *   **[陷阱B]**: [描述一个配置或代码中不直观的设定]
    ```

---

## 流程结束

完成以上所有步骤后，项目初始化流程即告完成。此时，项目应具备最基本的结构和文档，可以进入后续的开发阶段。
