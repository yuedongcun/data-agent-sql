# Data Agent SQL

最小可运行的 NL2SQL agent：用户问题 -> 读取 schema -> 生成 SQL -> 执行 -> 失败修复 -> 返回结果。

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
cp .env .env.local
# 编辑 .env.local，填入你的 OpenRouter API key

# 3. 初始化数据库
sqlite3 data/demo.db < data/schema.sql

# 4. 启动服务
uvicorn app.main:app --reload --port 8000
```

## API

**POST /api/query**

请求：
```json
{"question": "哪些客户下了已完成订单？"}
```

响应：
```json
{
  "question": "哪些客户下了已完成订单？",
  "sql": "SELECT c.name, o.status FROM customers c JOIN orders o ON c.id = o.customer_id WHERE o.status = 'completed'",
  "result": [...],
  "answer": "张三和李四下了已完成订单。",
  "repaired": false
}
```

**GET /health** — 健康检查
