# Weather Agent

一个不依赖 LangChain 等 Agent 框架实现的简单天气 Agent，
用于学习 Tool Calling 和 Agent 执行循环。

## 功能

支持在命令行中使用自然语言提问，例如：

- 明天北京适合穿什么？
- 上海今天需要带伞吗？
- 广州明天天气怎么样？
- 1+1 等于多少？

Agent 会自行判断是否需要天气信息。

如果需要天气数据：

用户问题
→ DeepSeek 判断
→ 调用 get_weather
→ Open-Meteo
→ 返回天气 JSON
→ DeepSeek 生成最终回答

如果不需要天气数据，则由模型直接回答。

## 技术栈

- Python
- DeepSeek
- Open-Meteo
- HTTP API
- JSON
- Tool Calling
- Agent Loop

## 安装

创建虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate