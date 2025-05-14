# SecureShift.AI 🔐

SecureShift.AI is an AI-powered code review agent that analyzes Java, Python, SQL, and more for security vulnerabilities. It combines static rule-based analysis with GPT-powered reasoning to produce readable and actionable security reports.

## Features
- ✅ Multi-language support (Java, Python, SQL)
- ✅ Static rule scan (eval, exec, SQL concat, etc.)
- ✅ GPT vulnerability explanation and fix recommendation
- ✅ Markdown report generation
- ✅ Streamlit-based UI

## ⚙️ Architecture
1. **StaticRuleScannerTool** – Detects basic risky patterns
2. **GPTExplainerTool** – GPT-4 explains and suggests fixes
3. **ReportFormatterTool** – Generates markdown report
4. **LangGraph Agent** – Manages the execution flow
5. **Streamlit App** – Frontend for interactive use

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
