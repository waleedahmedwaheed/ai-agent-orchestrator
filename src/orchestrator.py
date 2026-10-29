"""Minimal multi-agent orchestration entrypoint."""

from __future__ import annotations


def plan(goal: str) -> list[str]:
    return [
        f"Clarify goal: {goal}",
        "Gather required context",
        "Execute tools",
        "Summarize results",
    ]


def main() -> None:
    goal = "Ship a demo multi-agent workflow"
    steps = plan(goal)
    print("Planner steps:")
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")
    print("Supervisor: ready for worker execution.")


if __name__ == "__main__":
    main()
