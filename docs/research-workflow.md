# Product walkthrough

## 1. Frame a research question

The user begins with a question, not a preconfigured agent. The workspace turns that question into a set of research lanes, each with a distinct angle and its own conversation state.

## 2. Compare parallel lanes

The research board keeps the lanes side by side. A lane contains its own findings, collected source material, and follow-up conversation. This prevents a useful perspective from being buried in one long chat transcript.

## 3. Inspect the evidence

Each lane can expose the research text, collected material, and verification context. The UI does not present provider labels as if they were sources: a source is a concrete title, URL, and saved excerpt that the user can inspect.

## 4. Deepen one direction

When one lane matters, the user can start deeper research from it. The deep work stays attached to the parent lane, rather than appearing as an unrelated new conversation. That preserves the reasoning path:

```text
Question
├─ Market structure
├─ Customer behavior
│  ├─ Interviews
│  └─ Pricing signals
└─ Competitor evidence
```

## 5. Synthesize selectively

A synthesis is built from selected research material. It keeps a route back to the contributing lanes and claims, so the user can read the result first and inspect its support when needed.

## Core objects

| Object | Role |
| --- | --- |
| Research question | Starts the investigation and gives each lane shared context. |
| Parallel lane | Explores one distinct angle without overwriting the others. |
| Source material | Preserves the evidence collected by a lane. |
| Claim | A traceable statement used in a synthesis. |
| Synthesis | Connects a conclusion to the selected research and claims behind it. |
| Follow-up research | Extends a useful lane while keeping its parent relationship. |

## Design decisions

- **Preserve the path, not only the answer.** A synthesis must be inspectable after it is written.
- **Keep lanes independent.** Different research directions remain comparable instead of collapsing into one chat stream.
- **Treat sources as product data.** Sources are not decorative citations; they are the route back to evidence.
- **Lead with findings.** The reader sees the result before deciding whether to open sources or verification details.
