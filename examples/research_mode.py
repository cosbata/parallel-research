"""A small, dependency-free extract from Parallel Research's lane policy."""


def infer_research_mode(query: str, requested_depth: str | None = None) -> str:
    """Prefer an explicit depth; otherwise infer a safe default from the request."""
    depth = (requested_depth or "").lower().strip()
    if depth in ("fast", "quick", "short"):
        return "fast"
    if depth in ("balanced", "normal"):
        return "balanced"
    if depth in ("deep", "comprehensive", "full"):
        return "deep"

    normalized_query = (query or "").lower()
    deep_markers = (
        "심화", "깊게", "deep", "in-depth", "comprehensive", "학술", "논문", "primary source", "원전"
    )
    verify_markers = (
        "검증", "출처 강화", "source verification", "verify", "fact check", "근거"
    )
    if any(marker in normalized_query for marker in verify_markers):
        return "verify_sources"
    if any(marker in normalized_query for marker in deep_markers):
        return "deep"
    return "fast"


def max_sources_for_mode(mode: str) -> int:
    """Bound the material displayed in one lane while allowing deeper work more context."""
    return {
        "fast": 6,
        "balanced": 8,
        "deep": 10,
        "verify_sources": 10,
    }.get(mode or "balanced", 8)
