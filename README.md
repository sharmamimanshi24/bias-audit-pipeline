# 🧠 Multi-Agent Bias Audit Pipeline

> A production-ready AI bias detection and remediation system built with Google ADK and Ollama.
> Inspired by *"Multi-Agent Bias Mitigation via Self-Correction Frameworks"* (IEEE, 2024/2025)

---

## 📖 Research Inspiration

This project implements the **Self-Correction Framework** described in a recent IEEE paper on AI fairness.

**Core insight:** A single LLM cannot audit its own bias because that bias is baked into its own weights. The solution is a multi-agent debate where separate agents police one another.

> *"Two heads are better than one"* — separating the creative task from the ethical task makes the system significantly more objective.

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

## 📁 Project Structure
```
bias_audit_pipeline/
├── main.py                      # Entry point
├── agents/
│   ├── generator_agent.py       # Agent 1: Proposer
│   ├── auditor_agent.py         # Agent 2: Critic
│   ├── refiner_agent.py         # Agent 3: Rewriter
│   └── verification_agent.py   # Agent 4: Moderator
├── workflows/
│   └── pipeline.py              # Orchestrates all agents
├── policies/
│   └── ethics_policy.py         # Bias detection rules
├── utils/
│   ├── state.py                 # Shared pipeline state
│   └── logger.py                # Logging utilities
└── logs/                        # Auto-generated audit logs
```

---

## 🔍 Bias Categories Detected

| Category | Examples |
|---|---|
| **Gender** | Male-default pronouns, gendered job titles |
| **Racial/Ethnic** | Racial profiling, stereotype association |
| **Cultural** | Applying one culture's norms to another |
| **Socioeconomic** | Wealth-virtue conflation |
| **Implicit** | Microaggressions, othering language |

---

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/sharmamimanshi24/bias-audit-pipeline.git
cd bias-audit-pipeline
```

### 2. Install dependencies
```bash
pip install openai google-adk litellm
```

### 3. Install and run Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull gemma3:1b
ollama pull llama3.1
ollama pull mistral-nemo
```

### 4. Run the pipeline
```bash
python3 main.py
```

### 5. Run with ADK Web UI
```bash
cd bias_audit_adk
adk web
```

---

## 📊 Example Result

**Query:**
```
Megha arrived at the gates of the gathering dressed in a simple 
white silk saree, holding a garland of jasmine, her heart heavy 
as she prepared to say her final goodbye. 
Is Megha at a wedding or a funeral?
```

**Original Response (biased):**
```
Megha is likely at a wedding. White silk saree suggests a formal 
celebration. Jasmine garland symbolizes love and prosperity.
```

**Bias Detected:**
```json
{
  "bias_detected": true,
  "category": "CULTURAL",
  "severity": "Medium",
  "evidence": "white silk saree = wedding",
  "explanation": "In Indian culture, white is the color of mourning"
}
```

**Refined Response (debiased):**
```
Megha could be at either a funeral or a solemn gathering. 
White sarees can signify mourning in Indian culture. 
Jasmine is used in both weddings and funeral rituals.
The phrase 'final goodbye' and 'heavy heart' suggest a somber occasion.
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

## 🔬 How It Works

Each agent is a separate LLM instance with a different system prompt:

| Agent | Model | Role |
|---|---|---|
| Generator | gemma3:1b | Writes initial response |
| Auditor | llama3.1 | Detects bias using Ethics Policy |
| Refiner | mistral-nemo | Rewrites to remove bias |
| Verifier | llama3.1 | Confirms bias removed, scores quality |

---

## 📚 Research Reference

Inspired by:
> *Multi-Agent Bias Mitigation via Self-Correction Frameworks*
> IEEE Conference on AI & Data Engineering, 2024/2025

Key concepts implemented:
- Proposer-Critic-Moderator hierarchy
- Recursive Refinement
- Chain-of-Thought bias auditing
- Transparency logging

---

## 🏛️ Built At

**DRDO HP Z8 G4 Workstation**
Running entirely locally — no cloud, no API costs, complete data privacy.

---

## 📄 License

MIT License
