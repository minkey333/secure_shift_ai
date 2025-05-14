import re
from typing import Any, Dict, List
from langchain.tools import BaseTool

RISK_PATTERNS = {
    "eval_usage": {
        "pattern": r"\beval\s*\(",
        "description": "Use of eval() can lead to code injection vulnerabilities.",
        "risk_level": "High"
    },
    "exec_usage": {
        "pattern": r"\bexec\s*\(",
        "description": "Use of exec() can execute arbitrary code.",
        "risk_level": "High"
    },
    "pickle_load": {
        "pattern": r"pickle\.load\s*\(",
        "description": "pickle.load() is unsafe if used with untrusted input.",
        "risk_level": "Medium"
    },
    "os_system": {
        "pattern": r"os\.system\s*\(",
        "description": "os.system() may allow command injection.",
        "risk_level": "Medium"
    },
    "sql_concat": {
        "pattern": r"(SELECT|UPDATE|INSERT|DELETE).+\+.+",
        "description": "SQL query concatenation with user input may lead to SQL injection.",
        "risk_level": "High"
    }
}

def static_rule_check(code: str) -> List[Dict[str, Any]]:
    results = []
    for rule_name, rule_info in RISK_PATTERNS.items():
        matches = re.finditer(rule_info["pattern"], code, re.IGNORECASE)
        for match in matches:
            results.append({
                "rule": rule_name,
                "matched_text": match.group(),
                "start": match.start(),
                "end": match.end(),
                "description": rule_info["description"],
                "risk_level": rule_info["risk_level"]
            })
    return results

class StaticRuleScannerTool(BaseTool):
    name = "StaticRuleScanner"
    description = "Scans a code snippet for known static security risks using pattern matching."

    def _run(self, code: str) -> List[Dict[str, Any]]:
        return static_rule_check(code)

    def _arun(self, code: str) -> Any:
        raise NotImplementedError("Async not supported.")