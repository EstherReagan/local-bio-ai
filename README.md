# 🧬 Local Bio-AI Page Assistant

A privacy-first, client-side repository template designed for biochemistry, genomics, and bioinformatics research workflows. This configuration framework facilitates fully local, secure analytical tasks on contextual text frames and proprietary research files entirely offline.

---

## 🎯 Architectural Intent
High-value biological datasets and genomic records are heavily protected under compliance frameworks like HIPAA and GDPR. Relaying unpublished technical data to cloud endpoints presents clear intellectual property vulnerabilities. This configuration project bridges browser environments with localized inference platforms to process data entirely within local host structures.

---

## 🏗️ System Architecture
```text
[ Browser Tab ] ──> ( Extracts DNA Sequences / Biotech PDF Data )
                           │
                           ▼
[ Extension Engine ] ──> ( Client-side DOM parsing & Text Chunking )
                           │
                           ▼
[ Local Host (127.0.0.1) ] ──> ( REST API call to Ollama Engine )
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────┐
│              YOUR LOCAL HARDWARE (Offline)               │
│  [Ollama Server] ──> [Llama 3 / BioMistral Inference]     │
└──────────────────────────────────────────────────────────┘
```

---

## 📂 Project Architecture Layout
* `/research` : Formal analytical blueprints outlining localized system configurations.
* `/backend` : Modular computational scripts interacting with data format sequences.
* `/extension` : Layout code for structural browser UI interactions.
* `/automation` : Automated initialization parameters for Windows environments.
* `/benchmarks` : Latency verification and compute performance utilities.

---

## 🚀 Environment Verification

### 1. Requirements
Ensure your background computation service is fully installed and operational on your system.

### 2. Dependency Resolution
Windows system operators can run the automated script within the `/automation` subdirectory to download dependencies automatically:
```bash
automation/setup_env.bat
```

### 3. Execution Verification
Verify local engine accessibility through a standard terminal window:
```bash
curl http://localhost:11434/
```
