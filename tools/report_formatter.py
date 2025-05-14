from typing import Any
from langchain.tools import BaseTool

class ReportFormatterTool(BaseTool):
    name = "ReportFormatter"
    description = "Formats the vulnerability analysis results into a readable Markdown report."

    def _run(self, state: dict) -> str:
        static_results = state.get("static_results", [])
        gpt_response = state.get("gpt_response", "")

        markdown = "# SecureShift.AI Code Review Report\n\n"

        markdown += "## 🔍 Static Scan Results\n"
        if static_results:
            markdown += "| Rule | Match | Risk Level | Description |\n"
            markdown += "|------|-------|------------|-------------|\n"
            for r in static_results:
                markdown += f"| {r['rule']} | `{r['matched_text']}` | {r['risk_level']} | {r['description']} |\n"
        else:
            markdown += "No static rule violations found.\n"

        markdown += "\n## 🧠 GPT Vulnerability Analysis\n"
        if gpt_response:
            markdown += f"{gpt_response}\n"
        else:
            markdown += "GPT analysis not available.\n"

        return markdown

    def _arun(self, state: dict) -> Any:
        raise NotImplementedError("Async not supported.")