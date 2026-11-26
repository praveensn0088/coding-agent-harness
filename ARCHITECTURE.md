
# Coding Agent Harness Architecture

## 1. Project Overview

This project implements a Python-based AI Coding Agent Harness.

The harness uses an LLM to understand software engineering tasks,
inspect source code, propose changes, execute permitted tools,
and validate implementation results.

The initial implementation uses OpenAI through LangChain.

LangGraph will be introduced for workflow orchestration.

## 2. High-Level Components

### LLM Integration
Location: harness/llm.py

Responsibilities:
- Initialize the configured LLM.
- Load provider configuration.
- Handle model invocation.
- Expose a reusable model factory.

### Agents
Location: harness/agents/

Responsibilities:
- Agent behavior.
- Task planning.
- Implementation and review logic.

### Tools
Location: harness/tools/

Responsibilities:
- File reading.
- File modification.
- Directory inspection.
- Controlled command execution.

### Skills
Location: harness/skills/

Responsibilities:
- Reusable engineering procedures.
- Task-specific workflows.
- Standardized problem-solving instructions.

### Quality
Location: harness/quality/

Responsibilities:
- Automated testing.
- Linting.
- Static analysis.
- Quality evaluation.

### Context
Location: harness/context/

Responsibilities:
- Repository instructions.
- Architecture information.
- Context loading.
- Relevant documentation.

## 3. Target Application

Location: workspace/

The workspace contains applications that the coding agent
will inspect and modify.

Initial sample application:

workspace/sample_app/

- calculator.py
- test_calculator.py

The harness and target application must remain logically separated.

## 4. Technology Stack

- Python 3.13
- LangChain
- LangGraph
- OpenAI API
- Pydantic
- Python-dotenv
- Pytest
- Ruff

## 5. Target Execution Lifecycle

1. Receive user task.
2. Load instructions and relevant context.
3. Inspect the target repository.
4. Prepare an implementation plan.
5. Execute permitted tools.
6. Modify application code.
7. Run deterministic quality checks.
8. Review failures.
9. Correct implementation when necessary.
10. Report results to the user.

## 6. Architectural Principles

- Separation of concerns.
- Provider-independent LLM integration.
- Controlled tool execution.
- Explicit workflow orchestration.
- Deterministic quality validation.
- Bounded retry and correction loops.
- Human approval for high-impact actions.
- Observable execution and token usage.

## 7. Current Implementation Status

Completed:
- Project foundation.
- Python environment.
- Sample calculator application.
- LLM integration.

In progress:
- Instructions and context engineering.

Planned:
- Tools and skills.
- LangGraph orchestration.
- Quality sensors.
- Feedback loop.
- Human approval.
- Observability.
