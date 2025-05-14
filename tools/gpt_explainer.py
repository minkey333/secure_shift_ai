from typing import Any
from langchain.tools import BaseTool
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

class GPTExplainerTool(BaseTool):
    name = "GPTExplainer"
    description = "Analyzes a code snippet with GPT and returns vulnerability explanation and fix recommendation."

    def _run(self, code: str) -> str:
        prompt = f"""
You are a senior security expert.

Analyze the following code and answer:
1. What vulnerabilities are present?
2. What type is it?
3. Why is it risky?
4. Severity level (High / Medium / Low)?
5. Fix recommendation?

Code:
```python
{code}
```
"""
        llm = ChatOpenai(temperature=0)
        response = llm([HumanMessage(content=prompt)])
        return response.content

    def _arun(self, code: str) -> Any:
        raise NotImplementedError("Async not supported.")