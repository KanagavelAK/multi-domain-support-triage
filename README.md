# Multi-Domain Support Triage Agent

This is an Agentic RAG triage system designed to handle support tickets across three ecosystems: HackerRank, Claude, and Visa. It automates ticket classification, status determination, and grounded response generation while strictly adhering to safety and escalation guidelines.

## Approach Overview

The agent is built using an async-capable pipeline with the following key design decisions:
1. **In-Memory Knowledge Base**: The support documentation is curated and embedded directly into a Python dictionary (`corpus.py`). This eliminates the need for a vector database (like ChromaDB), dramatically improving speed and reducing complexity.
2. **Contextual Routing**: The agent first identifies which company (HackerRank, Claude, or Visa) the ticket belongs to. It then injects *only* that company's documentation into the LLM prompt. This minimizes token usage and prevents cross-contamination of policies.
3. **Multi-Layered Safety & Escalation**:
   - **Pre-flight checks**: Keyword detection (e.g., "identity theft", "fraud", "lawsuit") triggers automatic escalation before hitting the LLM.
   - **Prompt Injection Defense**: Explicit system instructions prevent the LLM from revealing internal rules or system prompts.
   - **Constrained Generation**: The LLM is strictly instructed to only use the provided knowledge base. If a topic is not covered, it must escalate.
4. **Performance Optimization**: Uses the `llama-3.1-8b-instant` model via the Groq API for maximum speed and cost-efficiency. Exponential backoff and concurrency control are implemented to respect API rate limits.

## Setup Instructions

### Prerequisites
- Python 3.8+
- A Groq API Key

### Installation

1. **Clone/Extract the project**
   Ensure all files are extracted to a directory.

2. **Install Dependencies**
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   *(This installs `groq`, `pandas`, `python-dotenv`, and `tqdm`)*

3. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_api_key_here
   ```

### Usage

Run the agent from the terminal. By default, it looks for an input CSV at `support_tickets/support_tickets.csv` and outputs to `support_tickets/results.csv`.

```bash
python agent.py
```

To specify custom input/output paths:
```bash
python agent.py path/to/input.csv path/to/output.csv
```

The output CSV will contain the following columns: `Issue`, `Subject`, `Company`, `status`, `product_area`, `response`, `justification`, and `request_type`.
