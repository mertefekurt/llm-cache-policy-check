from __future__ import annotations

from llm_cache_policy_check.models import Rule

PROJECT_NAME = 'llm-cache-policy-check'
SUMMARY = 'Check LLM response cache policies for privacy, TTL, and key-scope gaps.'
SAMPLE_RISK = 'cache enabled ttl none pii true scope global'
SAMPLE_CLEAN = 'cache enabled ttl 1h pii false scope tenant'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='no-ttl',
        severity='high',
        pattern='ttl\\s+(none|missing|unknown)',
        message='cache TTL missing',
        recommendation='set cache TTL',
    ),
    Rule(
        code='pii-cache',
        severity='medium',
        pattern='pii\\s+true',
        message='PII may be cached',
        recommendation='disable or isolate sensitive caching',
    ),
    Rule(
        code='global-scope',
        severity='low',
        pattern='scope\\s+global',
        message='cache scope is global',
        recommendation='use tenant or user scoped keys',
    ),
)
