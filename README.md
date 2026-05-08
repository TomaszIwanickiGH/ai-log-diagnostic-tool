# AI Log Diagnostic Tool

A modern DevOps automation tool that leverages Local LLMs to analyze server logs and provide actionable troubleshooting steps.

## Overview
This project demonstrates an **AIOps** approach to infrastructure management. It uses a Python-based agent running in a **Docker** container to communicate with a local **Llama 3** model (via Ollama). 

The tool is specifically tuned to recognize and suggest fixes for **Oracle Database** errors (e.g., ORA-errors), making it a valuable asset for database administrators and DevOps engineers.

##  Tech Stack
- **Language:** Python 3.9
- **AI Engine:** Ollama (Llama 3 model)
- **Containerization:** Docker
- **Focus:** DevOps Automation & Log Analysis

## Getting Started

### Prerequisites
1. Install [Ollama](https://ollama.com/)
2. Pull the Llama 3 model:
   ```bash
   ollama run llama3
3. Install Docker Desktop

## Installation & Running

### Prerequisites
1. Clone this repository:
   ```bash
   git clone [https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/ai-log-diagnostic-tool.git](https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/ai-log-diagnostic-tool.git)
   cd ai-log-diagnostic-tool
2. Build the Docker image:
   ```bash
   docker build -t ai-log-analyzer .
3. Run the container:
   ```bash
   docker run ai-log-analyzer

## 📈 Key Features Demonstrated
- **Docker Networking:** Successfully implemented container-to-host communication using `host.docker.internal`.
- **AI Integration:** Practical usage of LLMs for technical diagnostic tasks.
- **Oracle DB Troubleshooting:** Tailored analysis for common database connectivity issues.
- **Infrastructure as Code (Basic):** Fully containerized environment for consistent execution.

---
*Created as part of my journey to becoming a DevOps Engineer.*