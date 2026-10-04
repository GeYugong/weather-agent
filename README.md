# Weather Agent

一个用于学习 Agent 原理的简单天气助手。

## 功能

用户可以通过自然语言提问，例如：

- 明天北京适合穿什么？
- 上海今天需要带伞吗？
- 广州明天天气怎么样？

Agent 会自行判断是否需要查询天气。

如果需要，会自动调用 Open-Meteo 获取天气数据，
然后由大模型根据天气结果生成最终回答。

## 技术栈

- Python
- Open-Meteo
- DeepSeek
- Tool Calling
- Agent Loop