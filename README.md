# AI Runtime — Learning AI from First Principles

This repository documents my learning journey in **AI Engineering** by building an AI system **from first principles**, one layer at a time.

Instead of starting with frameworks or end-to-end demos, I focused on **understanding the core mechanics** of how modern AI systems actually work:
- how state flows
- where memory lives
- why retrieval exists
- what embeddings really solve
- and how scaling pressure shapes architecture

Each version (`v1` → `v5`) answers **one specific systems question** and introduces **only the minimum new concept required**.

---

## Philosophy

**Rules I followed throughout this repo:**
- No frameworks (LangChain, LlamaIndex, etc.)
- No agents until grounding is solved
- Replace internals, not architectures
- Let systems fail before “fixing” them
- Treat AI as a systems + data problem, not magic

---

## Repository Structure

```
ai-runtime/
├── v1_real_model/
├── v2_memory/
├── v3_naive_retrieval/
├── v4_embeddings/
├── v5_scaled_retrieval/
└── README.md
```


Each version builds directly on the previous one.

---

## Version Breakdown

---

## v1 — Real Model Integration

**Question answered:**  
What actually changes when the model becomes real?

**What I did:**
- Replaced a fake rule-based model with a real LLM
- Kept the runtime loop and context system unchanged

**Key insights:**
- Models are stateless
- Replacing the model does not fix system-level problems
- Context size is a hard constraint, not a suggestion

---

## v2 — Explicit Memory System

**Question answered:**  
What is memory, structurally?

**What I did:**
- Introduced a `MemoryStore` separate from context
- Persisted memory across runs
- Injected selected memory back into context

**Key insights:**
- Context ≠ memory
- Memory introduces a **selection problem**
- Bad memory compounds errors over time

---

## v3 — Naive Relevance & Failure

**Question answered:**  
Why is relevance hard?

**What I did:**
- Implemented lexical token-overlap–based retrieval
- Ranked memories by shared words
- Injected top-k memories into context

**Key insights:**
- Lexical similarity ≠ semantic relevance
- Rules fail structurally, not accidentally
- Memory kinds compete destructively without meaning
- Autonomy collapses with noisy retrieval

This version is intentionally flawed to expose the problem.

---

## v4 — Embedding-Based Retrieval

**Question answered:**  
How does relevance become geometric?

**What I did:**
- Introduced embeddings as a new primitive
- Replaced rule-based relevance with vector similarity
- Stored embeddings alongside memory entries

**Key insights:**
- Relevance is continuous, not discrete
- Embeddings reduce noise but do not eliminate errors
- Wrong memories can still rank highly
- Representation quality matters more than rules

Embeddings were treated as a system primitive, not magic.

---

## v5 — Scaled Retrieval & Indexing

**Question answered:**  
How does embedding-based retrieval scale?

**What I did:**
- Removed full memory scans
- Introduced sharding-based approximate indexing
- Queried only candidate shards
- Persisted memory and rebuilt indexes on startup
- Explicitly separated:
  - durable state (memory)
  - derived state (index)

**Key insights:**
- AI systems are data systems first
- Recall vs latency is an explicit tradeoff
- Approximate retrieval is unavoidable at scale
- Vector databases are indexing + persistence abstractions

At this stage, vector DBs feel **obvious**, not magical.

---

## Current Status

Completed:
- LLM fundamentals
- Context management
- Explicit memory
- Retrieval failure modes
- Embeddings
- Indexing and persistence

Next:
- **v6 — Retrieval-Augmented Generation (RAG)**
  - Separate conversational memory from external knowledge
  - Chunking strategies
  - Controlled grounding
  - Explainable retrieval

Agents, tools, and frameworks will come **after grounding is correct**.

---

## Why This Repo Exists

Most AI learning paths start at:
> “Build a chatbot using X framework”

This repo starts at:
> “What must exist for this system to work?”

The goal is not to memorize tools, but to build **transferable system intuition** that survives API changes and hype cycles.

---

## Final Note

Every version here is intentionally incomplete.

That incompleteness is not a flaw —  
it is how real systems are learned, built, and evolved.


