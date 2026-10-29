# AI Agent Orchestrator

Multi-agent orchestration starter for coordinating specialized AI agents on complex workflows.

Inspired by modern agentic systems: a planner breaks work down, worker agents execute tools, and a supervisor merges results with clear handoffs.

## Why this exists

Single-prompt chatbots struggle with multi-step work. This repo gives you a small, readable skeleton for:

- Task planning and role assignment
- Shared memory / scratchpad between agents
- Tool calling with structured outputs
- Simple retry and escalation policies

## Project layout

```text
src/
  agents/       # planner, worker, and supervisor roles
  memory/       # short-term shared context
  tools/        # example tools agents can call
  orchestrator.py
requirements.txt
```

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# add your OPENAI_API_KEY (or compatible provider key)

python -m src.orchestrator
```

## Core idea

1. **Planner** turns a user goal into ordered steps  
2. **Workers** run tools for each step  
3. **Supervisor** validates outputs and decides next action  

Swap providers, tools, or agent prompts without rewriting the control loop.

## Roadmap

- [ ] Streaming step updates
- [ ] Persistent run history
- [ ] Human-in-the-loop approvals
- [ ] Parallel worker fan-out

## License

MIT
