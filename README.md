# 🔍 Multi-Agent Bias Audit Pipeline

> An AI system that checks its own responses for bias — and fixes them.</br>
>Inspired by *"Multi-Agent Bias Mitigation via Self-Correction Frameworks"* (IEEE, 2024/2025)


![Status](https://img.shields.io/badge/status-active-brightgreen)
![Built With](https://img.shields.io/badge/built%20with-Google%20ADK-blue)
![Models](https://img.shields.io/badge/models-Ollama%20Local-orange)
![License](https://img.shields.io/badge/license-MIT-purple)
![Made By](https://img.shields.io/badge/made%20by-Mimanshi%20Sharma-ff69b4)
![Privacy](https://img.shields.io/badge/data-100%25%20local-success)

Here's the problem: an AI can't check its own bias because the bias is already part of how it thinks. This project solves that by using **4 separate AI agents** that argue with each other — one writes, one audits, one rewrites, one verifies. No single AI is in charge.

---

## 📑 Table of Contents

- [Why This Exists](#-why-this-exists)
- [How It Works](#-how-it-works)
- [Architecture](#-architecture)
- [Bias Types Detected](#-bias-types-detected)
- [Project Structure](#-project-structure)
- [Setup](#-setup)
- [Example](#-example)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Support](#-support)
- [Project Status](#-project-status)

---

## 💡 Why This Exists

AI models have bias baked into them from training data. Asking the same AI to check its own bias doesn't work — it'll just agree with itself.

The fix? Use **multiple AI agents with different roles** so they keep each other in check. This idea comes from a real IEEE research paper on AI fairness (2024/2025).

> *"Two heads are better than one"* — separating the creative task from the ethical task makes the system way more objective.

---

## 🔬 How It Works

4 agents. Each one has a different job:

| Agent | Model | What it does |
|---|---|---|
| **Generator** | gemma3:1b | Writes the first response |
| **Auditor** | llama3.1 | Looks for bias using an Ethics Policy |
| **Refiner** | mistral-nemo | Rewrites the response to remove bias |
| **Verifier** | llama3.1 | Checks the rewrite and gives a quality score |

Every run produces a **transparency log** (JSON) so you can see exactly what was changed and why.

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────────┐
│  Agent 1: GENERATOR         │
│  Generates initial response │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Agent 2: AUDITOR           │
│  Detects bias using         │
│  Ethics Policy              │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Agent 3: REFINER           │
│  Rewrites response          │
│  removing bias              │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Agent 4: VERIFIER          │
│  Confirms bias removed      │
│  Scores quality & fairness  │
└────────────┬────────────────┘
             │
             ▼
    Final Debiased Response
    + Transparency Log (JSON)
```

---

## 🔍 Bias Types Detected

| Type | Example |
|---|---|
| **Gender** | Assuming a doctor is male |
| **Racial/Ethnic** | Stereotyping based on name or background |
| **Cultural** | Applying one culture's norms to everyone |
| **Socioeconomic** | Assuming rich = good, poor = bad |
| **Implicit** | Subtle language that "others" certain groups |

---

## 📁 Project Structure

```
bias_audit_pipeline/
├── main.py                      # Run this to start
├── agents/
│   ├── generator_agent.py       # Agent 1
│   ├── auditor_agent.py         # Agent 2
│   ├── refiner_agent.py         # Agent 3
│   └── verification_agent.py   # Agent 4
├── workflows/
│   └── pipeline.py              # Connects all agents
├── policies/
│   └── ethics_policy.py         # Bias detection rules
├── utils/
│   ├── state.py                 # Shared data between agents
│   └── logger.py                # Saves audit logs
└── logs/                        # Auto-generated logs here
```

---

## ⚙️ Setup

### What you need
- Python 3.10+
- [Ollama](https://ollama.com) installed
- Google ADK

### Step 1 — Clone the repo
```bash
git clone https://github.com/sharmamimanshi24/bias-audit-pipeline.git
cd bias-audit-pipeline
```

### Step 2 — Install dependencies
```bash
pip install openai google-adk litellm
```

### Step 3 — Download the AI models
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull gemma3:1b
ollama pull llama3.1
ollama pull mistral-nemo
```

### Step 4 — Run it
```bash
python3 main.py
```

### Step 5 — Optional: Run with a web UI
```bash
cd bias_audit_adk
adk web
```

---

## 📊 Example

**Input query:**
```
Megha arrived at the gathering in a white silk saree, holding jasmine,
her heart heavy as she prepared to say her final goodbye.
Is Megha at a wedding or a funeral?
```

**First response (biased):**
```
Megha is likely at a wedding. White silk saree = formal celebration.
Jasmine = love and prosperity.
```

**Bias caught:**
```json
{
  "bias_detected": true,
  "category": "CULTURAL",
  "severity": "Medium",
  "evidence": "white silk saree = wedding",
  "explanation": "In Indian culture, white is the color of mourning, not celebration"
}
```

**Fixed response:**
```
Megha could be at a funeral or a solemn gathering. In Indian culture,
white sarees often signify mourning. Jasmine is used in both weddings
and funeral rituals. The phrase 'final goodbye' and 'heavy heart'
suggest a somber occasion.
```

**Verification:**
```json
{
  "bias_removed": true,
  "quality_score": 9,
  "final_verdict": "pass"
}
```

---

## 🤝 Contributing

Want to improve this? Here's how:

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-idea`
3. Make changes and commit: `git commit -m "your change"`
4. Push and open a Pull Request

---

## 📄 License

MIT License — use it, build on it, just credit the author.

---

## 👩‍💻 Author

**Mimanshi Sharma** — AI/ML Engineering
Inspired by: *Multi-Agent Bias Mitigation via Self-Correction Frameworks* — IEEE, 2024/2025

---

## 🆘 Support

Run into issues? Open a GitHub issue or reach out on LinkedIn.

---

## 📌 Project Status

🟢 **Active** — March 2026
