<p align="center" style="text-align:center">
  <img src="resources/serena-logo.svg#gh-light-mode-only" style="width:500px">
  <img src="resources/serena-logo-dark-mode.svg#gh-dark-mode-only" style="width:500px">
</p>

* :rocket: Serena是一个强大的**编码代理工具包**，能够将LLM转变为一个功能齐全的代理，**直接在您的代码库上工作**。
* :wrench: Serena提供必要的**语义代码检索和编辑工具**，类似于IDE的功能，可以在符号级别提取代码实体并利用关系结构。当与现有编码代理结合使用时，这些工具大大提高了（令牌）效率。
* :free: Serena是**免费且开源的**，免费增强了您已有的LLM的能力。

### 演示

以下是Serena使用Claude Desktop为其自身实现一个小功能（一个更好的日志GUI）的演示。
请注意Serena的工具如何让Claude找到并编辑正确的符号。

https://github.com/user-attachments/assets/6eaa9aa1-610d-4723-a2d6-bf1e487ba753

<p align="center">
  <em>Serena正在积极开发中！查看最新更新、即将推出的功能和经验教训以保持同步。</em>
</p>

<p align="center">
  <a href="CHANGELOG.md">
    <img src="https://img.shields.io/badge/Updates-1e293b?style=flat&logo=rss&logoColor=white&labelColor=1e293b" alt="Changelog" />
  </a>
  <a href="roadmap.md">
    <img src="https://img.shields.io/badge/Roadmap-14532d?style=flat&logo=target&logoColor=white&labelColor=14532d" alt="Roadmap" />
  </a>
  <a href="lessons_learned.md">
    <img src="https://img.shields.io/badge/Lessons-Learned-7c4700?style=flat&logo=readthedocs&logoColor=white&labelColor=7c4700" alt="Lessons Learned" />
  </a>
</p>



### LLM集成

Serena为编码工作流程提供了必要的[工具](#full-list-of-tools)，但实际工作需要LLM来协调工具的使用。

例如，通过[一行shell命令](#claude-code)**增强Claude Code的性能**。

Serena可以通过多种方式与LLM集成：
 * 通过使用**模型上下文协议 (MCP)**。
   Serena提供了一个MCP服务器，可与以下工具集成：
     * Claude Code 和 Claude Desktop，
     * IDEs，如 VSCode、Cursor 或 IntelliJ，
     * 扩展，如 Cline 或 Roo Code
     * 以及许多其他，包括[即将推出的 ChatGPT 应用](https://x.com/OpenAIDevs/status/1904957755829481737)
 * 通过使用**Agno – 模型无关代理框架**。
   Serena基于Agno的代理允许您将几乎任何LLM转变为编码代理，无论是Google、OpenAI还是Anthropic（需付费API密钥）提供的模型，
   还是Ollama、Together或Anyscale提供的免费模型。
 * 通过将Serena的工具整合到您选择的代理框架中。
   Serena的工具实现与框架特定的代码解耦，因此可以轻松适应任何代理框架。

### 编程语言支持与语义分析能力

Serena的语义代码分析能力建立在广泛实现的语言服务器协议 (LSP) 基础之上。LSP提供了一套基于代码符号理解的通用代码查询和编辑功能。凭借这些能力，Serena能够像经验丰富的开发人员利用IDE功能一样，发现和编辑代码。即使在非常庞大和复杂的项目中，Serena也能高效地找到正确的上下文并执行正确的操作！因此，它不仅免费且开源，而且经常比现有收费解决方案取得更好的结果。

语言服务器支持多种编程语言。
Serena提供：
 * 直接、开箱即用的支持：
     * Python
     * TypeScript/Javascript（目前存在一些不稳定问题，我们正在努力解决）
     * PHP
     * Go（需要先安装go和gopls）
     * Rust
     * C#（需要安装dotnet。我们最近切换了底层语言服务器，请报告您遇到的任何问题）
     * Java（_注意_：启动缓慢，尤其是首次启动。Java在macOS和Linux上可能存在问题，我们正在努力解决。）
     * Elixir（需要安装NextLS和Elixir；**不支持Windows** - Next LS不提供Windows二进制文件）
     * Clojure
     * C/C++（您可能会遇到查找引用问题，我们正在努力解决）
 * 间接支持（可能需要一些代码更改/手动安装）：
     * Ruby（未经测试）
     * Kotlin（未经测试）
     * Dart（未经测试）

   这些语言受语言服务器库支持，但
   我们尚未明确测试对这些语言的支持是否确实完美无缺。

原则上，通过为新的语言服务器实现提供一个简单的适配器，可以轻松支持更多语言。


## 目录

<!-- Created with markdown-toc -i README.md -->
<!-- Install it with npm install -g markdown-toc -->

<!-- toc -->

- [Serena 的用途](#what-can-i-use-serena-for)
- [使用 Serena 的免费编码代理](#free-coding-agents-with-serena)
- [快速入门](#quick-start)
  * [运行 Serena MCP 服务器](#running-the-serena-mcp-server)
    + [用法](#usage)
        * [本地安装](#local-installation)
      - [使用 uvx](#using-uvx)
      - [使用 Docker（实验性）](#using-docker-experimental)
    + [SSE 模式](#sse-mode)
    + [命令行参数](#command-line-arguments)
  * [配置](#configuration)
  * [项目激活与索引](#project-activation--indexing)
  * [Claude Code](#claude-code)
  * [Claude Desktop](#claude-desktop)
  * [其他 MCP 客户端（Cline、Roo-Code、Cursor、Windsurf 等）](#other-mcp-clients-cline-roo-code-cursor-windsurf-etc)
  * [Agno 代理](#agno-agent)
  * [其他代理框架](#other-agent-frameworks)
- [详细用法和建议](#detailed-usage-and-recommendations)
  * [工具执行](#tool-execution)
    + [Shell 执行和编辑工具](#shell-execution-and-editing-tools)
  * [模式和上下文](#modes-and-contexts)
    + [上下文](#contexts)
    + [模式](#modes)
    + [自定义](#customization)
  * [入门和记忆](#onboarding-and-memories)
  * [准备您的项目](#prepare-your-project)
    + [组织您的代码库](#structure-your-codebase)
    + [从干净状态开始](#start-from-a-clean-state)
    + [日志、Linter 和自动化测试](#logging-linting-and-automated-tests)
  * [提示策略](#prompting-strategies)
  * [代码编辑中的潜在问题](#potential-issues-in-code-editing)
  * [上下文耗尽](#running-out-of-context)
  * [将 Serena 与其他 MCP 服务器结合使用](#combining-serena-with-other-mcp-servers)
  * [Serena 的日志：仪表盘和 GUI 工具](#serenas-logs-the-dashboard-and-gui-tool)
  * [故障排除](#troubleshooting)
- [与其他编码代理的比较](#comparison-with-other-coding-agents)
  * [基于订阅的编码代理](#subscription-based-coding-agents)
  * [基于 API 的编码代理](#api-based-coding-agents)
  * [其他基于 MCP 的编码代理](#other-mcp-based-coding-agents)
- [致谢](#acknowledgements)
- [自定义和扩展 Serena](#customizing-and-extending-serena)
- [工具完整列表](#full-list-of-tools)

<!-- tocstop -->

## Serena 的用途

Serena 可用于任何编码任务——无论是侧重于分析、规划、设计新组件还是重构现有组件。
由于 Serena 的工具允许 LLM 关闭认知感知-行动循环，基于 Serena 的代理可以自主地完成从初始分析到实现、测试，最后到版本控制系统提交的编码任务。

Serena 可以读、写和执行代码，读取日志和终端输出。
虽然我们不一定鼓励，但“随性编码”肯定是可能的，如果您想几乎感觉“代码不再存在”，
您可能会发现 Serena 比 IDE 中的代理更适合随性编码
（因为您将拥有一个独立的 GUI，让您真正忘却一切）。

## 使用 Serena 的免费编码代理

即使是 Anthropic 的 Claude 的免费层也支持 MCP 服务器，因此您可以免费使用 Serena 和 Claude。
大概，一旦添加对 MCP 服务器的支持，ChatGPT Desktop 很快也将实现同样的功能。
通过 Agno，您还可以选择使用 Serena 和免费/开源模型。

Serena 是 [Oraios AI](https://oraios-ai.de/) 对开发者社区的贡献。
我们自己也经常使用它。

我们厌倦了不得不支付多个基于 IDE 的订阅（例如 Windsurf 或 Cursor），这些订阅迫使我们在已有的聊天订阅费用之上继续购买令牌。
Claude Code、Cline、Aider 和其他基于 API 的工具所产生的巨额 API 成本同样没有吸引力。
因此，我们构建了 Serena，希望能取消大部分其他订阅。

## 快速入门

Serena 可以通过多种方式使用，以下是针对选定集成的说明。

- 如果您只是想将 Claude 变成一个免费的编码代理，我们建议通过 [Claude Code](#claude-code) 或 [Claude Desktop](#claude-desktop) 使用 Serena。
- 如果您想使用 Gemini 或任何其他模型，并且想要一个 GUI 体验，您可以使用 [Agno](#agno-agent) 或许多其他支持 MCP 服务器的 GUI。
- 如果您想将 Serena 集成到您的 IDE 中，请参阅[其他 MCP 客户端](#other-mcp-clients---cline-roo-code-cursor-windsurf-etc)部分。

Serena 由 `uv` 管理，因此您需要[安装它](https://docs.astral.sh/uv/getting-started/installation/)。

### 运行 Serena MCP 服务器

您有多种选项来运行 MCP 服务器，具体说明如下：

#### 用法

典型用法涉及客户端（Claude Code、Claude Desktop 等）作为子进程运行 MCP 服务器（使用标准输入输出通信），
因此需要向客户端提供运行 MCP 服务器的命令。
（或者，您可以在 SSE 模式下运行 MCP 服务器，并告知您的客户端如何连接。）

请注意，无论您如何运行 MCP 服务器，Serena 默认会在 localhost 上启动一个小型基于 Web 的仪表板，用于显示日志并允许关闭 MCP 服务器（因为许多客户端无法正确清理进程）。
此功能及其他设置可在[配置](#configuration)中调整和/或通过提供[命令行参数](#command-line-arguments)进行调整。

##### 使用 uvx

`uvx` 可以直接从仓库运行最新版本的 Serena，无需显式本地安装。

```shell
uvx --from git+https://github.com/oraios/serena serena start-mcp-server
```

探索 CLI 以查看 Serena 提供的一些自定义选项（更多信息见下文）。

###### 本地安装

1. 克隆仓库并进入其中。
   ```shell
   git clone https://github.com/oraios/serena
   cd serena
   ```
2. （可选）使用以下命令编辑您主目录中的配置文件：
   ```shell
   uv run serena config edit
   ```
   如果您只想要默认配置，可以跳过此部分，Serena 首次运行时将自动创建配置文件。
3. 使用 `uv` 运行服务器：
   ```shell
   uv run serena start-mcp-server
   ```
   如果从 Serena 安装目录外部运行，请务必传入目录，即使用：
   ```shell
    uv run --directory /abs/path/to/serena serena start-mcp-server
   ```

##### 使用 Docker（实验性）

⚠️ Docker 支持目前处于实验阶段，存在一些限制。在使用前，请务必阅读 [Docker 文档](DOCKER.md)以了解重要注意事项。

您可以直接通过 Docker 运行 Serena MCP 服务器，如下所示，
假设您要处理的所有项目都位于 `/path/to/your/projects` 中：

```shell
docker run --rm -i --network host -v /path/to/your/projects:/workspaces/projects ghcr.io/oraios/serena:latest serena start-mcp-server --transport stdio
```

将 `/path/to/your/projects` 替换为您项目目录的绝对路径。Docker 方法提供：
- 更好的 shell 命令执行安全隔离
- 无需在本地安装语言服务器和依赖项
- 跨不同系统的一致环境

有关详细设置说明、配置选项和已知限制，请参阅 [Docker 文档](DOCKER.md)。

#### SSE 模式

ℹ️ 请注意，使用 stdio 作为协议的 MCP 服务器在客户端/服务器架构方面有些不寻常，因为服务器必须由客户端启动才能通过服务器的标准输入/输出流进行通信。
换句话说，您不需要自己启动服务器。客户端应用程序（例如 Claude Desktop）会负责此事，因此需要配置启动命令。

当使用 SSE 模式时，它使用基于 HTTP 的通信，您自己控制服务器生命周期，
即您启动服务器并向客户端提供连接 URL。

只需为 `start-mcp-server` 提供 `--transport sse` 选项，并可选择提供端口。
例如，要在端口 9121 上以 SSE 模式运行本地安装的 Serena MCP 服务器，
您将在 Serena 目录中运行此命令，

```shell
uv run serena start-mcp-server --transport sse --port 9121
```

然后配置您的客户端连接到 `http://localhost:9121/sse`。


#### 命令行参数

Serena MCP 服务器支持广泛的附加命令行选项，包括在 SSE 模式下运行以及使 Serena 适应各种[操作上下文和模式](#modes-and-contexts)的选项。

运行参数 `--help` 以获取可用选项列表。


### 配置

Serena 的行为（活动工具和提示以及日志配置等）在四个地方进行配置：

1. `serena_config.yml` 用于适用于所有客户端和项目的通用设置。
   它位于您的用户目录下的 `.serena/serena_config.yml` 中。
   如果您没有显式创建此文件，Serena 首次运行时将自动生成。
   您可以直接编辑它，或使用
   ```shell
   uvx --from git+https://github.com/oraios/serena serena config edit
   ```
   （或使用 `--directory` 命令版本）。
2. 在传递给客户端配置中 `start-mcp-server` 的参数中（见下文），
   这将应用于相应客户端启动的所有会话。特别是，应适当设置 [context](#contexts) 参数，
   以便 Serena 最佳地适应客户端的现有工具和功能。
   有关详细说明，请参阅。您可以通过命令行参数覆盖 `serena_config.yml` 中的所有条目。
3. 在您的项目内的 `.serena/project.yml` 文件中。此文件将保存项目级别的配置，每当
   该项目被激活时都会使用。此文件将在您首次在该项目上使用 Serena 时自动生成，但您也可以
   使用以下命令显式生成它：
   ```shell
   uvx --from git+https://github.com/oraios/serena serena project generate-yml
   ```
   （或使用 `--directory` 命令版本）。
4. 通过当前活动的 [modes](#modes) 集。


> ⚠️ **注意：**Serena 正在积极开发中。我们正在不断添加新功能，提高稳定性和用户体验。
> 因此，配置可能会发生破坏性更改。如果您的配置无效，
> MCP 服务器或基于 Serena 的代理可能无法启动（在前一种情况下，请检查 MCP 日志）。
> 更新 Serena 时，请检查 [更新日志](CHANGELOG.md)
> 和配置模板，并相应地调整您的配置。

初始设置完成后，根据您希望如何使用 Serena，继续阅读以下部分之一。

您可以直接要求 LLM 显示您的会话配置，Serena 有一个工具可以实现此功能。

### 项目激活与索引

推荐的方法是直接让 LLM 激活一个项目，可以通过提供其绝对路径，或者，如果项目过去曾被激活过，则通过其名称。默认的项目名称是目录名。

  * "激活项目 /path/to/my_project"
  * "激活项目 my_project"

所有已激活的项目将自动添加到您的 `serena_config.yml` 中，并且每个项目都会生成一个 `.serena/project.yml` 文件。您可以调整后者，例如更改名称（您在激活时引用的名称）或其他选项。请确保不要有两个不同但同名的项目。

如果您主要处理同一个项目，您也可以配置在启动时始终激活一个项目，方法是向客户端的 MCP 配置中的 `start-mcp-server` 命令传递 `--project <path_or_name>`。

ℹ️ 对于大型项目，我们建议您索引项目以加速 Serena 的工具；否则首次工具应用可能会非常慢。
为此，请在项目目录中运行以下命令（或将项目路径作为参数传递）：

```shell
uv run --directory /Users/laobaibai/Documents/GitHub/serena serena project index
```

（或使用 `--directory` 命令版本）。

### Claude Code

Serena 是让 Claude Code 更便宜、更强大的绝佳方式！

在您的项目目录中，使用如下命令添加 serena：

```shell
claude mcp add serena -- <serena-mcp-server> --context ide-assistant --project $(pwd)
```

其中 `<serena-mcp-server>` 是您[运行 Serena MCP 服务器](#running-the-serena-mcp-server)的方式。
例如，当使用 `uvx` 时，您将运行：
```shell
claude mcp add serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project $(pwd)
```

ℹ️ Serena 附带一份说明文本，Claude 需要阅读它才能正确使用 Serena 的工具。
  从 `v1.0.52` 版本开始，claude code 会读取 MCP 服务器的说明，因此这**是自动处理的**。
  如果您使用的是旧版本，或者 Claude 未能读取说明，您可以明确要求它“阅读 Serena 的初始说明”或运行 `/mcp__serena__initial_instructions` 来加载说明文本。
  如果您想利用此功能，您必须通过在配置中将 `initial_instructions` 添加到 `included_optional_tools` 中来明确启用相应的工具。
  请注意，您可能需要在开始新对话和任何压缩操作后让 Claude 读取说明，以确保 Claude 保持正确配置以使用 Serena 的工具。


### Claude Desktop

对于 [Claude Desktop](https://claude.ai/download)（适用于 Windows 和 macOS），请转到文件 / 设置 / 开发者 / MCP 服务器 / 编辑配置，
这将允许您打开 JSON 文件 `claude_desktop_config.json`。
根据您的设置，使用[运行命令](#running-the-serena-mcp-server)添加 `serena` MCP 服务器配置。

* 本地安装：
   ```json
   {
       "mcpServers": {
           "serena": {
               "command": "/abs/path/to/uv",
               "args": ["run", "--directory", "/abs/path/to/serena", "serena", "start-mcp-server"]
           }
       }
   }
   ```
* uvx：
   ```json
   {
       "mcpServers": {
           "serena": {
               "command": "/abs/path/to/uvx",
               "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server"]
           }
       }
  }
  ```
* docker：
  ```json
   {
       "mcpServers": {
           "serena": {
               "command": "docker",
               "args": ["run", "--rm", "-i", "--network", "host", "-v", "/path/to/your/projects:/workspaces/projects", "ghcr.io/oraios/serena:latest", "serena", "start-mcp-server", "--transport", "stdio"]
           }
       }
   }
   ```

如果您在 Windows 上使用包含反斜杠的路径
（请注意您也可以直接使用正斜杠），请务必正确转义它们 (`\\`)。

就是这样！保存配置，然后重启 Claude Desktop。您已准备好激活您的第一个项目。

ℹ️ 您可以使用附加参数进一步自定义运行命令（参见[上文](#command-line-arguments)）。

注意：Windows 和 macOS 上有 Anthropic 官方的 Claude Desktop 应用程序，Linux 上有一个[开源社区版本](https://github.com/aaddrick/claude-desktop-debian)。

⚠️ 请务必完全退出 Claude Desktop 应用程序，因为关闭 Claude 只会将其最小化到系统托盘——至少在 Windows 上是这样。

⚠️ 某些客户端，目前包括 Claude Desktop，可能会留下僵尸进程。您需要手动查找并终止它们。
    使用 Serena，您可以激活[仪表板](#serenas-logs-the-dashboard-and-gui-tool)以防止未被注意的进程，并可以使用仪表板关闭 Serena。

重启后，您应该在聊天界面中看到 Serena 的工具（注意小锤子图标）。

有关 Claude Desktop 中 MCP 服务器的更多信息，请参阅[官方快速入门指南](https://modelcontextprotocol.io/quickstart/user)。

### 其他 MCP 客户端（Cline、Roo-Code、Cursor、Windsurf 等）

作为 MCP 服务器，Serena 可以包含在任何 MCP 客户端中。上述配置，
可能只需进行一些客户端特定的微小修改，即可正常工作。大多数流行的
现有编码助手（IDE 扩展或类似 VSCode 的 IDE）都支持连接
到 MCP 服务器。**建议将 `ide-assistant` 上下文用于这些集成**，方法是在 MCP 客户端的配置中将 `"--context", "ide-assistant"` 添加到 `args` 中。包含 Serena 通常会通过为它们提供符号操作工具来提高其性能。

在这种情况下，使用费用的计费将继续由您选择的客户端控制
（与 Claude Desktop 客户端不同）。但您可能仍然希望通过这种方法使用 Serena，
例如，出于以下原因之一：

1. 您已经在使用编码助手（例如 Cline 或 Cursor），只是想让它更强大。
2. 您在 Linux 上，不想使用[社区创建的 Claude Desktop](https://github.com/aaddrick/claude-desktop-debian)。
3. 您希望 Serena 更紧密地集成到您的 IDE 中，并且不介意为此付费。

### Agno 代理

Agno 是一个模型无关的代理框架，它允许您将 Serena 转换为一个代理
（独立于 MCP 技术），并支持大量底层 LLM。Agno 目前是
在聊天 GUI 中使用您选择的 LLM 运行 Serena 的最简单方式。

虽然 Agno 尚未完全稳定，但我们选择它是因为它自带开源 UI，
使得直接通过聊天界面使用代理变得容易。通过 Agno，Serena 被转换为一个代理
（因此不再是 MCP 服务器），因此它可以以编程方式使用（例如用于基准测试或在您的应用程序中）。

工作原理如下（另请参阅 [Agno 文档](https://docs.agno.com/introduction/playground)）：

1. 使用 npx 下载 agent-ui 代码
   ```shell
   npx create-agent-ui@latest
   ```
   或者，手动克隆：
   ```shell
   git clone https://github.com/agno-agi/agent-ui.git
   cd agent-ui
   pnpm install
   pnpm dev
   ```

2. 安装 Serena 及可选要求：
   ```shell
   # 您也可以只选择 agno,google 或 agno,anthropic，而不是 all-extras
   uv pip install --all-extras -r pyproject.toml -e .
   ```

3. 将 `.env.example` 复制到 `.env` 并填写您打算使用的提供商的 API 密钥。

4. 启动 agno 代理应用：
   ```shell
   uv run python scripts/agno_agent.py
   ```
   默认情况下，脚本使用 Claude 作为模型，但您可以选择 Agno 支持的任何模型
   （本质上是任何现有模型）。

5. 在新终端中，启动 agno UI：
   ```shell
   cd agent-ui
   pnpm dev
   ```
   将 UI 连接到您上面启动的代理并开始聊天。您将拥有与 MCP 服务器版本相同的工具。


以下是 Serena 使用最新的 Gemini 模型执行一个小分析任务的简短演示：

https://github.com/user-attachments/assets/ccfcb968-277d-4ca9-af7f-b84578858c62


⚠️ 重要提示：与 MCP 服务器方法不同，Agno UI 中的工具执行不会征求用户的许可。shell 工具尤其关键，因为它可能执行任意代码。虽然我们在使用 Claude 进行测试时从未遇到过任何问题，但允许这样做可能并不完全安全。您可以选择在 Serena 项目的配置文件 (`.yml`) 中禁用某些工具。

### 其他代理框架

将 Serena 集成到任何代理框架（如 [pydantic-ai](https://ai.pydantic.dev/)、[langgraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/) 或其他）中应该很简单。
通常，您只需要为 Serena 的工具编写一个适配器，以适应您选择的框架中的工具表示形式，
就像我们为 Agno 与 [SerenaAgnoToolkit](/src/serena/agno.py) 所做的那样。


## 详细用法和建议

### 工具执行

Serena 将语义代码检索工具与编辑功能和 shell 执行相结合。
Serena 的行为可以通过[模式和上下文](#modes-and-contexts)进一步定制。
工具的完整列表请参见[下方](#full-list-of-tools)。

通常建议使用所有工具，因为这能让 Serena 提供最大价值：
只有通过执行 shell 命令（特别是测试），Serena 才能自主识别并纠正错误。

#### Shell 执行和编辑工具

然而，需要注意的是，`execute_shell_command` 工具允许任意代码执行。
当 Serena 作为 MCP 服务器使用时，客户端通常会在执行工具之前请求用户许可，
因此只要用户事先检查执行参数，这应该不是问题。
但是，如果您有疑虑，可以选择在项目的 .yml 配置文件中禁用某些命令。
如果您只想纯粹使用 Serena 进行代码分析和实现建议，而不修改代码库，
您可以在项目配置文件中设置 `read_only: true` 以启用只读模式。
这将自动禁用所有编辑工具，并防止对代码库进行任何修改，同时仍允许所有分析和探索功能。

通常，请务必备份您的工作并使用版本控制系统，以避免丢失任何工作。


### 模式和上下文

Serena 的行为和工具集可以通过上下文和模式进行调整。
这些允许高度定制，以最佳地适应您的工作流程和 Serena 运行的环境。

#### 上下文

上下文定义了 Serena 运行的通用环境。
它影响初始系统提示和可用工具集。
上下文在 Serena 启动时设置（例如，通过 MCP 服务器的 CLI 选项或在代理脚本中），并且在活动会话期间不能更改。

Serena 预定义了以下上下文：
*   `desktop-app`：专为 Claude Desktop 等桌面应用程序设计。这是默认设置。
*   `agent`：专为 Serena 作为更自主的代理（例如，与 Agno 结合使用时）的场景设计。
*   `ide-assistant`：针对与 VSCode、Cursor 或 Cline 等 IDE 的集成进行了优化，侧重于编辑器内编码辅助。
选择最符合您正在使用的集成类型的上下文。

启动 Serena 时，使用 `--context <context-name>` 指定上下文。
请注意，对于指定参数列表的情况（例如 Claude Desktop），您必须向列表中添加两个参数。

#### 模式

模式进一步细化了 Serena 针对特定任务类型或交互风格的行为。多个模式可以同时激活，允许您组合它们的效果。模式会影响系统提示，并且还可以通过排除某些工具来更改可用工具集。

内置模式示例包括：
*   `planning`：将 Serena 的重点放在规划和分析任务上。
*   `editing`：优化 Serena 以进行直接代码修改任务。
*   `interactive`：适用于对话式的、来回交互的风格。
*   `one-shot`：将 Serena 配置为在单个响应中完成任务，通常与 `planning` 结合使用以生成报告或初始计划。
*   `no-onboarding`：如果特定会话不需要初始入职流程，则跳过。
*   `onboarding`：（通常自动触发）专注于项目入职流程。

模式可以在启动时设置（类似于上下文），但也可以在会话期间**动态切换**。您可以指示 LLM 使用 `switch_modes` 工具激活一组不同的模式（例如，“切换到规划和一次性模式”）。

启动 Serena 时，使用 `--mode <mode-name>` 指定模式；可以指定多个模式，例如 `--mode planning --mode no-onboarding`。

:warning: **模式兼容性**：虽然您可以组合模式，但有些模式可能在语义上不兼容（例如，`interactive` 和 `one-shot`）。Serena 目前不阻止不兼容的组合；由用户选择合理的模式配置。

#### 自定义

您可以通过两种方式创建自己的上下文和模式，以精确地根据您的需求定制 Serena：
*   您可以使用 Serena 的 CLI 来管理模式和上下文。请查看
    ```shell
    uvx --from git+https://https://github.com/oraios/serena serena mode --help
    uvx --from git+https://https://github.com/oraios/serena serena context --help
    ```
    *注意*：自定义上下文/模式只是 `<home>/.serena` 中的 YAML 文件，它们会自动注册并可按其名称（不带 `.yml` 扩展名的文件名）使用。如果您不想使用 Serena 的 CLI，您可以以任何您认为合适的方式创建和管理它们。
*  **使用外部 YAML 文件**：启动 Serena 时，您还可以提供自定义 `.yml` 文件的绝对路径作为上下文或模式。

上下文或模式 YAML 文件通常定义：
*   `name`：（可选，如果使用文件名）上下文/模式的名称。
*   `prompt`：将合并到 Serena 系统提示中的字符串。
*   `description`：（可选）简要描述，不传递给 LLM。
*   `excluded_tools`：当此上下文/模式处于活动状态时要禁用的工具名称（字符串）列表。
*   `included_optional_tools`：默认禁用并必须由用户显式启用的工具名称列表。

这种自定义允许深度集成和 Serena 对特定项目要求或个人偏好的适应。


### 入门和记忆

默认情况下，Serena 在项目首次启动时会执行**入门过程**。
入门的目标是让 Serena 熟悉项目并存储记忆，以便在未来的交互中利用。
如果 LLM 未能完成入门过程且未将相关记忆实际写入磁盘，您可能需要明确要求它这样做。

入门通常会从项目中读取大量内容，从而填充上下文。因此，在入门完成后切换到另一个对话可能是明智之举。
入门完成后，我们建议您快速查看记忆，并在必要时编辑或添加更多记忆。

**记忆**是存储在项目目录 `.serena/memories/` 中的文件，代理可以选择在后续交互中读取它们。
您可以随意阅读和调整它们；您也可以手动添加新的记忆。
`.serena/memories/` 目录中的每个文件都是一个记忆文件。
每当 Serena 开始处理一个项目时，都会提供记忆列表，代理可以决定是否读取它们。
我们发现记忆可以显著改善 Serena 的用户体验。


### 准备您的项目

#### 组织您的代码库

Serena 使用代码结构来查找、读取和编辑代码。这意味着它将
与结构良好的代码配合良好，但在完全非结构化的代码（例如包含巨大、非模块化函数的“上帝类”）上可能表现不佳。
此外，对于非静态类型语言，类型注解非常有益。

#### 从干净状态开始

最好从一个干净的 git 状态开始代码生成任务。这不仅会让您更容易检查更改，而且模型本身也有机会通过调用 `git diff` 来查看它所做的更改，从而纠正自己或在后续对话中继续工作（如果需要）。

:warning: **重要提示**：由于 Serena 将使用系统原生的行尾写入文件，并且它可能需要查看 git diff，因此在 Windows 上将 `git config core.autocrlf` 设置为 `true` 非常重要。
如果 Windows 上 `git config core.autocrlf` 设置为 `false`，您可能会因为行尾而导致巨大的 diff。通常，在 Windows 上全局启用此 git 设置是一个好主意：

```shell
git config --global core.autocrlf true
```

#### 日志、Linter 和自动化测试

Serena 可以在一个**代理循环**中成功完成任务，它在这个循环中迭代地获取信息、执行操作并反思结果。
然而，Serena 无法使用调试器；它必须依赖程序执行结果、linting 结果和测试结果来评估其操作的正确性。
因此，设计用于生成有意义的可解释输出（例如日志消息）且具有良好测试覆盖率的软件，Serena 处理起来会容易得多。

我们通常建议从所有 linting 检查和测试都通过的状态开始编辑任务。

### 提示策略

我们发现，对于非平凡的任务，通常最好花一些时间进行任务的概念化和规划，然后再实际实施。这有助于获得更好的结果，并增加控制感和保持在循环中的感觉。您可以在一个会话中制定详细计划，Serena 可能会阅读您的许多代码来构建上下文，然后（可能在创建合适的记忆后）在另一个会话中继续实施。

### 代码编辑中的潜在问题

根据我们的经验，LLM 不擅长计数，即它们在
将代码块插入到正确位置时存在问题。大多数编辑操作都可以在符号级别执行，从而克服这个问题。然而，有时
行级插入很有用。

Serena 被指示仔细检查它将编辑的行号和任何代码块，但如果您遇到问题，您可能会发现明确告诉它如何编辑代码很有用。
我们正在努力使 Serena 的编辑能力更加健壮。

### 上下文耗尽

对于漫长而复杂的任务，或者 Serena 阅读了大量内容的任务，您可能会接近上下文令牌的限制。在这种情况下，最好继续一个新的对话。Serena 有一个专门的工具，可以创建当前进度和所有相关信息的摘要，以便继续。您可以请求创建此摘要并将其写入记忆。然后，在一个新的对话中，您可以直接要求 Serena 读取记忆并继续执行任务。根据我们的经验，这非常有效。从好的方面看，由于在单个会话中不涉及摘要，Serena 通常不会迷失（不像一些在后台进行摘要的其他代理），并且它还被指示偶尔检查是否在正确的轨道上。

此外，Serena 被指示要节约使用上下文
（例如，不要不必要地读取代码符号的主体），
但我们发现 Claude 在节约方面并不总是很好（Gemini 似乎更好）。
如果您知道不需要，可以明确指示它不要读取主体。

### 将 Serena 与其他 MCP 服务器结合使用

当通过 MCP 客户端使用 Serena 时，您可以将其与其他 MCP 服务器一起使用。
但是，请注意工具名称冲突！有关信息请参阅上文。

目前，与流行的文件系统 MCP 服务器存在冲突。由于 Serena 也提供文件系统操作，因此可能没有必要同时启用这两个服务器。

### Serena 的日志：仪表盘和 GUI 工具

Serena 提供了两种方便的方式来访问当前会话的日志：

  * 通过**基于网络的仪表盘**（默认启用）

    所有平台都支持此功能。
    默认情况下，它将在 `http://localhost:24282/dashboard/index.html` 可访问，
    但如果默认端口不可用/有多个实例正在运行，可能会使用更高的端口。

  * 通过**GUI 工具**（默认禁用）

    此功能主要在 Windows 上受支持，但也可能在 Linux 上工作；macOS 不受支持。

两者都可以在 Serena 的配置文件 (`serena_config.yml`，见上文) 中启用、配置或禁用。
如果启用，它们将在 Serena 代理/MCP 服务器启动后自动打开。
如果您在配置中设置 `record_tool_usage_stats: True`，则网络仪表盘将显示 Serena 工具的使用统计信息。

除了查看日志，这两个工具都允许关闭 Serena 代理。
提供此功能是因为像 Claude Desktop 这样的客户端在自身关闭时可能无法终止 MCP 服务器子进程。

### 故障排除

Claude Desktop 中对 MCP 服务器的支持以及各种 MCP 服务器 SDK 都是相对较新的发展，可能会出现不稳定。

MCP 服务器的工作配置可能因平台和客户端而异。我们建议始终使用绝对路径，因为相对路径可能是错误的来源。语言服务器在单独的子进程中运行，并使用 asyncio 调用——有时客户端可能会导致其崩溃。如果您启用了 Serena 的日志窗口，并且它消失了，您就会知道发生了什么。

某些客户端可能无法正确终止 MCP 服务器，请注意挂起的 python 进程并在需要时手动终止它们。

## 与其他编码代理的比较

据我们所知，Serena 是第一个功能齐全的编码代理，其
所有功能都通过 MCP 服务器提供，因此不需要 API 密钥或
订阅。

### 基于订阅的编码代理

许多著名的基于订阅的编码代理都是 IDE 的一部分，例如
Windsurf、Cursor 和 VSCode。
Serena 的功能与 Cursor 的 Agent、Windsurf 的 Cascade 或
VSCode 的代理模式类似。

Serena 的优势在于无需订阅。
一个潜在的缺点是它
不直接集成到 IDE 中，因此检查新编写的代码
不够无缝。

更多技术差异包括：
* Serena 不受特定 IDE 或 CLI 的限制。
  Serena 的 MCP 服务器可与任何 MCP 客户端（包括某些 IDE）一起使用，
  而基于 Agno 的代理提供了应用其功能的其他方式。
* Serena 不受特定大型语言模型或 API 的限制。
* Serena 使用语言服务器导航和编辑代码，因此它对代码具有符号
  理解。
  基于 IDE 的工具通常使用基于 RAG 或纯文本的方法，这通常
  功能较弱，特别是对于大型代码库。
* Serena 是开源的，代码库小，因此可以轻松扩展
  和修改。

### 基于 API 的编码代理

订阅型代理的替代方案是基于 API 的代理，如 Claude
Code、Cline、Aider、Roo Code 等，其使用成本直接
与底层 LLM 的 API 成本挂钩。
其中一些（如 Cline）甚至可以作为扩展集成到 IDE 中。
它们通常非常强大，主要缺点是（可能非常高昂的）API 成本。

Serena 本身可以作为基于 API 的代理使用（参见上文关于 Agno 的部分）。
我们尚未为 Serena 编写 CLI 工具或
专用 IDE 扩展（而且可能也不需要后者，因为
Serena 已经可以与任何支持 MCP 服务器的 IDE 一起使用）。
如果市场对 Serena 作为类似 Claude Code 的 CLI 工具存在需求，我们将
考虑编写一个。

Serena 与其他基于 API 的代理的主要区别在于，Serena 可以
也用作 MCP 服务器，从而无需
API 密钥并绕过 API 成本。这是 Serena 的独特功能。

### 其他基于 MCP 的编码代理

还有其他专为编码设计的 MCP 服务器，如 [DesktopCommander](https://github.com/wonderwhy-er/DesktopCommanderMCP) 和
[codemcp](https://github.com/ezyang/codemcp)。
然而，据我们所知，它们都没有提供语义代码
检索和编辑工具；它们纯粹依赖于基于文本的分析。
正是语言服务器和 MCP 的集成使得 Serena 独一无二，
并且在处理具有挑战性的编码任务时（尤其是在大型代码库的上下文中）如此强大。


## 致谢

我们基于多个现有开源技术构建了 Serena，其中最重要的包括：

1. [multilspy](https://github.com/microsoft/multilspy)。
   一个库，它封装了语言服务器实现并使其适应通过 Python 进行交互，
   并为我们的 Solid-LSP 库 (src/solidlsp) 提供了基础。
   Solid-LSP 提供了纯同步 LSP 调用，并用 Serena 所需的符号逻辑扩展了原始库。
2. [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
3. [Agno](https://github.com/agno-agi/agno) 和
   相关的 [agent-ui](https://github.com/agno-agi/agent-ui)，
   我们使用它们来让 Serena 与任何模型（超越 MCP 支持的模型）一起工作。
4. 我们通过 Solid-LSP 使用的所有语言服务器。

没有这些项目，Serena 将不可能实现（或者构建起来会困难得多）。


## 自定义和扩展 Serena

扩展 Serena 的 AI 功能以实现您自己的想法非常简单。
只需通过继承 `serena.agent.Tool` 来实现一个新的工具，并实现一个与工具要求匹配的 `apply` 方法。
一旦实现，`SerenaAgent` 将自动访问新工具。

添加对新编程语言的支持也相对简单（[请参阅此处](/CONTRIBUTING.md#adding-a-new-supported-language)）。

我们期待看到社区能带来什么！
有关贡献的详细信息，请参阅[此处](/CONTRIBUTING.md)。

## 工具完整列表

以下是 Serena 工具的完整列表及其简短描述（`uv run serena tools list` 的输出）：

 * `activate_project`: 按名称激活项目。
 * `check_onboarding_performed`: 检查项目入门流程是否已完成。
 * `create_text_file`: 在项目目录中创建/覆盖文件。
 * `delete_lines`: 删除文件中指定范围的行。
 * `delete_memory`: 从 Serena 的项目特定内存存储中删除记忆。
 * `execute_shell_command`: 执行 shell 命令。
 * `find_referencing_code_snippets`: 查找指定位置符号被引用的代码片段。
 * `find_referencing_symbols`: 查找引用指定位置符号的符号（可选按类型筛选）。
 * `find_symbol`: 对给定名称/子字符串的符号进行全局（或局部）搜索（可选按类型筛选）。
 * `get_active_project`: 获取当前活动项目的名称（如果有）并列出现有项目。
 * `get_current_config`: 打印代理的当前配置，包括活动模式、工具和上下文。
 * `get_symbols_overview`: 获取给定文件或目录中定义的顶级符号概览。
 * `initial_instructions`: 获取当前项目的初始说明。默认禁用，必须通过使用 `included_optional_tools` 显式启用。
 * `insert_after_symbol`: 在给定符号定义结束之后插入内容。
 * `insert_at_line`: 在文件的给定行插入内容。
 * `insert_before_symbol`: 在给定符号定义开始之前插入内容。
 * `list_dir`: 列出给定目录中的文件和目录（可选递归）。
 * `list_memories`: 列出 Serena 的项目特定内存存储中的记忆。
 * `onboarding`: 执行入门流程（识别项目结构和基本任务，例如测试或构建）。
 * `prepare_for_new_conversation`: 提供准备新对话的说明（以便在必要的上下文下继续）。
 * `read_file`: 读取项目目录中的文件。
 * `read_memory`: 从 Serena 的项目特定内存存储中读取给定名称的记忆。
 * `replace_lines`: 用新内容替换文件中指定范围的行。
 * `replace_symbol_body`: 替换符号的完整定义。
 * `restart_language_server`: 重启语言服务器，当非 Serena 进行编辑时可能需要。
 * `search_for_pattern`: 在项目中搜索模式。
 * `summarize_changes`: 提供总结代码库更改的说明。
 * `switch_modes`: 通过提供模式名称列表来激活模式。
 * `think_about_collected_information`: 用于思考收集信息完整性的思考工具。
 * `think_about_task_adherence`: 用于确定代理是否仍在当前任务轨道上的思考工具。
 * `think_about_whether_you_are_done`: 用于确定任务是否真正完成的思考工具。
 * `write_memory`: 将命名记忆（供将来参考）写入 Serena 的项目特定内存存储。
