# MultiChat
**Adaptive AI Group Chat: A Real-Time Chat Application Where AI Agents Communicate Autonomously and Adapt to Users**

Build an adaptive multi-agent group chat system where users can actively steer conversation flow through real-time intervention.

- **Problem Definition**: Existing multi-agent debates often devolve into closed feedback loops, lacking mechanisms for real-time user control or intervention.
- **Literature Review**: Analyzing existing frameworks such as AutoGen and CAMEL highlights the limitations of rule-based debates in accommodating interactive user control.
- **Approach**: Implement an event-driven interrupt architecture to process user feedback instantly, enabling an orchestrator to dynamically realign agent context in real time.

---

## 🔬 Empirical Research: Human-in-the-Loop Multi-Agent Debate (HITL-MAD)
**Author**: Min Jae Kang (강민재, Student ID: 202645469)  
**Topic**: Bottleneck Detection and Error Resolution on GSM8K & HiddenBench

This repository contains the empirical benchmarking suite evaluating external human oversight vs. closed multi-agent debate (MAD) across symmetric arithmetic reasoning (GSM8K) and asymmetric hidden profile decision-making (HiddenBench).

---

### 📊 Benchmark Performance Summary

| Evaluation Metric | GSM8K (Math Reasoning, N=30) | HiddenBench (Asymmetric Silos, N=25) |
| :--- | :---: | :---: |
| **Information Topology** | Symmetric (Identical problem prompt) | Asymmetric (Shared briefing + 4 Private Silos) |
| **Baseline (Pure MAD) Accuracy** | **36.67%** (11/30) | **12.00%** (3/25) |
| **LLM-Moderated Accuracy** | **36.67%** (+0.0%p) | **16.00%** (+4.0%p) |
| **Human-in-the-Loop (HITL) Accuracy** | **100.00% (+63.33%p)** | **100.00% (+88.00%p)** |
| **Conformity Halting Rate** | **100.0%** (17/17 halted) | **100.0%** (22/22 halted) |
| **Error Propagation Rate** | 63.33% ➔ **0.0%** | 88.00% ➔ **0.0%** |
| **Private Fact Coverage** | N/A | 29.0% ➔ **94.8%** (+65.8%p) |
| **Human Bottleneck Detection Rate (RQ 1)** | **100.0%** (Avg Round 2.0) | **100.0%** (Avg Round 2.0) |

---

### 📂 Directory Structure

```text
MultiChat/
├── README.md                                                   # Project documentation
│
└── experiments/
    ├── gsm8k/                                                  # [Part 1] GSM8K Benchmark Suite
    │   ├── Human_in_the_Loop_Multi_Agent_Debate_GSM8K.pptx     # 📊 20-slide academic presentation deck
    │   ├── experiment_results.json                             # 📑 30-item turn-by-turn dialogue logs
    │   ├── run_experiment.py                                   # 🧪 GSM8K execution harness
    │   ├── generate_charts.py                                  # 📈 High-resolution figure generator
    │   ├── build_presentation.py                               # 🖥️ PPT builder script
    │   └── figures/                                            # 🖼️ High-resolution figures (5 files)
    │       ├── fig_rq1_detection.png
    │       ├── fig_rq2_accuracy.png
    │       ├── fig_rq3_comparison.png
    │       ├── fig_architecture.png
    │       └── fig_case_study.png
    │
    └── hiddenbench/                                            # [Part 2] HiddenBench Benchmark Suite
        ├── Human_in_the_Loop_Multi_Agent_Debate_HiddenBench.pptx # 📊 20-slide academic presentation deck
        ├── experiment_results.json                             # 📑 25-task turn-by-turn dialogue logs
        ├── run_hb_experiment.py                                # 🧪 HiddenBench execution harness
        ├── generate_hb_charts.py                               # 📈 High-resolution figure generator
        ├── build_hb_presentation.py                            # 🖥️ PPT builder script
        └── figures/                                            # 🖼️ High-resolution figures (4 files)
            ├── fig_hb_accuracy.png
            ├── fig_hb_metrics.png
            ├── fig_hb_architecture.png
            └── fig_hb_case_study.png
```

---

### 🚀 How to Run the Experiments

#### Requirements
```bash
pip install matplotlib python-pptx
```

#### Run GSM8K Multi-Agent Debate
```bash
cd experiments/gsm8k
python run_experiment.py
python generate_charts.py
python build_presentation.py
```

#### Run HiddenBench Multi-Agent Debate
```bash
cd experiments/hiddenbench
python run_hb_experiment.py
python generate_hb_charts.py
python build_hb_presentation.py
```
