# ⚡ LiteLLM

**LiteLLM** is an open-source Python SDK and proxy server that offers a **unified interface** for interacting with over **100 Large Language Models (LLMs)** across a wide range of providers — including OpenAI, Azure, Anthropic, Hugging Face, AWS Bedrock, Vertex AI, Cohere, Replicate, and Groq.

Whether you're building an AI-powered application or managing LLM infrastructure at scale, LiteLLM simplifies integration, monitoring, and routing through a single, OpenAI-compatible interface.

---

## 🚀 Features

### 🔗 Unified API

- Interact with multiple LLMs using a single, OpenAI-compatible API format.
- Seamlessly switch between providers with minimal code changes.

### 🌐 Proxy Server (LLM Gateway)

- Run a centralized **LiteLLM proxy server** to:
  - Manage and route requests across multiple providers
  - Enable **load balancing**
  - Apply **rate limiting**
  - Track usage and performance metrics

### 🐍 Python SDK

- Use the LiteLLM SDK to embed LLM interactions directly into your Python applications.
- Built-in support for multiple provider APIs under one abstraction layer.

### 💸 Cost Tracking & Budgeting

- Monitor LLM usage in real-time.
- Set and enforce **budgets per project or API key**.
- Track provider-specific token costs and optimize for savings.

---

## 🧠 Supported LLM Providers

LiteLLM supports 100+ models from leading AI platforms, including:

- **OpenAI** (GPT-4, GPT-3.5)
- **Azure OpenAI**
- **Anthropic** (Claude models)
- **Hugging Face Inference API**
- **AWS Bedrock**
- **Google Vertex AI**
- **Cohere**
- **Replicate**
- **Groq**
- ...and many more.

---

## 📦 Installation

```bash
pip install litellm


Retry & Fallback Mechanisms: Ensure robustness by automatically handling failures and switching between providers.

Caching & Guardrails: Implement prompt caching and set up guardrails for safer deployments.

Admin Dashboard: Visual interface to monitor and manage LLM usage and configurations
