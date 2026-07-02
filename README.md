# llm-cache-policy-check

> Check LLM response cache policies for privacy, TTL, and key-scope gaps.

## Workflow Overview

Check LLM response cache policies for privacy, TTL, and key-scope gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 38

Accepts LLM cache policy. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 38

```bash
python -m pip install -e ".[dev]"
llm-cache-policy-check examples/sample.txt
llm-cache-policy-check examples/sample.txt --json --fail-on medium
python -m llm_cache_policy_check --help
```

## Rule Surface 38

| Rule | Severity | Meaning |
|---|---:|---|
| `no-ttl` | high | cache TTL missing |
| `pii-cache` | medium | PII may be cached |
| `global-scope` | low | cache scope is global |

## Validation Notes 38

```bash
ruff check .
pytest
python -m llm_cache_policy_check --help
```

Example risky input:

```text
cache enabled ttl none pii true scope global
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
