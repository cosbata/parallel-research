# Sanitized implementation examples

This directory contains small, runnable extracts from the product's non-sensitive behavior. They are included to make the public repository more useful than a design document without exposing production orchestration, credentials, prompts, user data, or deployment configuration.

## Research mode selection

[`research_mode.py`](research_mode.py) chooses an appropriate research mode from an explicit request or a query. It also bounds the number of source items returned to a lane so a deeper request has more evidence without allowing one lane to grow without limit.

Run its checks with the Python standard library:

```bash
python3 examples/test_research_mode.py
```
