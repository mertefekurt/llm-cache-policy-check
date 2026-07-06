# LLM Cache Policy Check

![LLM Cache Policy Check cover](assets/readme-cover.svg)

Check LLM response cache policies for privacy, TTL, and key-scope gaps. This repo keeps the work close to the terminal: clear input, predictable output, and no service to babysit.

## LLM Cache Policy Check catches

- `no-ttl` (high): cache TTL missing. Fix: set cache TTL.
- `pii-cache` (medium): PII may be cached. Fix: disable or isolate sensitive caching.
- `global-scope` (low): cache scope is global. Fix: use tenant or user scoped keys.

## A normal pass

```bash
git clone https://github.com/mertefekurt/llm-cache-policy-check.git
cd llm-cache-policy-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
llm-cache-policy-check examples/sample.txt
llm-cache-policy-check examples/sample.txt --json
```

The input can be text, JSON, JSONL, or CSV. Use `--json` when another script needs the result instead of a Markdown report.

## A deliberately bad line

```text
cache enabled ttl none pii true scope global
```

## Maintainer loop

```bash
ruff check .
pytest
python -m llm_cache_policy_check --help
```
