<!--
  AtlasReaper311 :: GitHub profile README
  atlas-systems.uk
-->

<div align="center">
  <img src="https://raw.githubusercontent.com/AtlasReaper311/AtlasReaper311/main/atlas-icon-dark-256.png" width="120" alt="Atlas Systems"/>
</div>

<!-- ATLAS:LIVE:START -->
```text
atlas@SPECULAR-CORE:~$ status
[deploy]   ● operational · 5afea72 · 2026-07-13 23:50 UTC
[estate]   29 public repos · 11 stars
[activity] 528 commits in the last 90 days
[writing]  W-04 · Overclocking SPECULAR-CORE · 2026-06-22
atlas@SPECULAR-CORE:~$ _
```

![estate: 29 repos](https://img.shields.io/badge/estate-29_repos-f5a623?style=flat-square&labelColor=0a0a0f) ![deploy: operational](https://img.shields.io/badge/deploy-operational-4ade80?style=flat-square&labelColor=0a0a0f) [![writing: W-04](https://img.shields.io/badge/writing-W--04-e8e8e0?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk/writing/overclocking-specular-core/)

<sub>live estate telemetry · regenerates every 6 hours · commits only on genuine change</sub>
<!-- ATLAS:LIVE:END -->

<div align="center">

# Atlas Reaper

**audio systems · local AI infrastructure · devops**

[![Site](https://img.shields.io/badge/atlas--systems.uk-live-f5a623?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk)
[![Map](https://img.shields.io/badge/system%20map-live%20architecture-f5a623?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk/lab/#system-map)
[![CV](https://img.shields.io/badge/cv.atlas--systems.uk-resume-555560?style=flat-square&labelColor=0a0a0f)](https://cv.atlas-systems.uk)
[![Status](https://img.shields.io/badge/systems-nominal-4ade80?style=flat-square&labelColor=0a0a0f)](https://status.atlas-systems.uk)
[![Atlas Systems status](https://api.atlas-systems.uk/v1/badge/status)](https://api.atlas-systems.uk/v1/docs)

</div>

```console
atlas@SPECULAR-CORE:~$ whoami
atlas-reaper  // local AI ·
audio systems · deployment infrastructure
```
---

## The architecture

I build at the intersection of audio systems, local AI, and deployment infrastructure. The three share one core problem: making complex, dynamic systems behave predictably under pressure.

Final year at Abertay University, Saltire Scholar. Building Atlas Systems before I graduate. The repositories below are the backend that runs [atlas-systems.uk](https://atlas-systems.uk); the site is the front of the same system, not a separate thing. Eleven Cloudflare Workers, three Pages sites, and a local AI stack behind a tunnel, and the estate documents itself: a registry Worker probes every other Worker's `/_meta` hourly and publishes what it finds.

```
P-01  Live domain        atlas-systems.uk, a deployed technical environment     [active]
P-02  GitHub library     Modular kits and Logic Lego components                 [building]
P-03  DevOps core        Docker · GitHub Actions · AWS Cloud Practitioner       [active]
P-04  Honours project    LLM integration with UE5 audio systems                 [planned]
P-05  Technical writing  Build logs and case studies on the domain              [active]
```

```
        public edge                              SPECULAR-CORE (LAN)
  ┌─────────────────────────┐   cloudflared   ┌──────────────────────┐
  │  11 workers · 3 sites   │ ═══ tunnel ═══> │  telemetry · corpus  │
  │  api.atlas-systems.uk   │                 │  ramone · ollama     │
  └─────────────────────────┘                 └──────────────────────┘
        every node, live: atlas-systems.uk/lab/#system-map
```

---

## Stack

| Domain | Tools |
|---|---|
| Languages | Python · C++ · JavaScript · HTML/CSS |
| Game dev | Unreal Engine 5 · MetaSounds · Blueprints |
| AI/ML | RAG pipelines · local LLMs (Ollama) · ChromaDB · Open WebUI |
| Infrastructure | Docker · Cloudflare Workers · Cloudflare Pages · GitHub Actions |
| In progress | AWS · environment promotion per Worker |

---

## Repositories

The canonical estate map lives in [`atlas-api-public/data/estate.manifest.json`](https://github.com/AtlasReaper311/atlas-api-public/blob/main/data/estate.manifest.json). The registry shows what is live; the manifest shows what the estate owns, how the components connect, and which surfaces are public, internal, or external.The backend of the platform, grouped by the layer it sits in. Each repo is built to be read and reused, not just looked at. Status badges are live; they show the last real run of that repo's pipeline.

### The Estate

Production infrastructure. These run, deploy on push, and report their own outcomes to Discord.

| Repo | Layer | Pipeline | What it does |
|---|---|---|---|
| [`atlas-systems`](https://github.com/AtlasReaper311/atlas-systems) | ![frontend](https://img.shields.io/badge/frontend-4ade80?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/atlas-systems/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-systems/actions) | Hand-built site source; html-validate and lychee gate every deploy to atlas-systems.uk |
| [`status`](https://github.com/AtlasReaper311/status) | ![frontend](https://img.shields.io/badge/frontend-4ade80?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/status/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/status/actions) | Live status page at status.atlas-systems.uk |
| [`atlas-doc-viewer`](https://github.com/AtlasReaper311/atlas-doc-viewer) | ![frontend](https://img.shields.io/badge/frontend-4ade80?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/atlas-doc-viewer/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-doc-viewer/actions) | Cross-device PDF wrapper; serves the CV at cv.atlas-systems.uk |
| [`atlas-notify`](https://github.com/AtlasReaper311/atlas-notify) | ![event bus](https://img.shields.io/badge/event%20bus-f5a623?style=flat-square&labelColor=0a0a0f) | [![ci](https://github.com/AtlasReaper311/atlas-notify/actions/workflows/ci.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-notify/actions) | Central event router; three webhook auth dialects, Vitest-gated, service-binding alert envelope for Worker runtime events |
| [`github-pulse`](https://github.com/AtlasReaper311/github-pulse) | ![data layer](https://img.shields.io/badge/data%20layer-f5a623?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/github-pulse/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/github-pulse/actions) | Live GitHub stats to the homepage, token held server-side |
| [`site-pulse`](https://github.com/AtlasReaper311/site-pulse) | ![data layer](https://img.shields.io/badge/data%20layer-f5a623?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/site-pulse/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/site-pulse/actions) | Cloudflare Analytics proxy behind a cached endpoint |
| [`deploy-watch`](https://github.com/AtlasReaper311/deploy-watch) | ![data layer](https://img.shields.io/badge/data%20layer-f5a623?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/deploy-watch/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/deploy-watch/actions) | Pages deploy poller; conditional KV writes on state change only |
| [`atlas-infra`](https://github.com/AtlasReaper311/atlas-infra) | ![ci/cd](https://img.shields.io/badge/ci%2Fcd-aaa9a0?style=flat-square&labelColor=0a0a0f) | reusable workflows | One `deploy-worker.yml` and one `validate-static.yml`, called by 12-line callers everywhere else; change the pipeline once, every repo inherits it |

Also in the estate, running private: `atlas-vault` (daily backup vault Worker, reports to its own Discord channel).

### Logic Legos

Six repos shipped as one build: memory, telemetry, voice control, search, disaster recovery, and self-documentation, each a self-contained brick that snaps onto the pipeline above. Written up in full on the site.

| Repo | Layer | Pipeline | What it does |
|---|---|---|---|
| [`atlas-api-index`](https://github.com/AtlasReaper311/atlas-api-index) | ![data layer](https://img.shields.io/badge/data%20layer-f5a623?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/atlas-api-index/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-api-index/actions) | Self-documenting Worker registry at api.atlas-systems.uk; probes every Worker's `/_meta` hourly with a read-only token, feeds the live [system map](https://atlas-systems.uk/lab/#system-map) |
| [`ramone-voice-trigger`](https://github.com/AtlasReaper311/ramone-voice-trigger) | ![ci/cd](https://img.shields.io/badge/ci%2Fcd-aaa9a0?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/ramone-voice-trigger/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/ramone-voice-trigger/actions) | Voice command to GitHub `workflow_dispatch`: secret-gated, allowlisted, deploys as `ramone-trigger`. Voice is a client of the pipeline, not a second deployment system |
| [`specular-telemetry`](https://github.com/AtlasReaper311/specular-telemetry) | ![data layer](https://img.shields.io/badge/data%20layer-f5a623?style=flat-square&labelColor=0a0a0f) | [![deploy](https://github.com/AtlasReaper311/specular-telemetry/actions/workflows/deploy.yml/badge.svg)](https://github.com/AtlasReaper311/specular-telemetry/actions) | Live GPU/CPU/RAM/Ollama stats from the workstation, tunnelled and edge-cached by `specular-edge`, rendered on the [Lab](https://atlas-systems.uk/lab/) |
| [`ramone-memory`](https://github.com/AtlasReaper311/ramone-memory) | ![service](https://img.shields.io/badge/service-f5a623?style=flat-square&labelColor=0a0a0f) | [![ci](https://github.com/AtlasReaper311/ramone-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/AtlasReaper311/ramone-memory/actions) | Ollama-compatible memory proxy; cross-session memory for the house AI as a drop-in URL swap, ChromaDB behind it |
| [`atlas-corpus`](https://github.com/AtlasReaper311/atlas-corpus) | ![service](https://img.shields.io/badge/service-f5a623?style=flat-square&labelColor=0a0a0f) | [![ci](https://github.com/AtlasReaper311/atlas-corpus/actions/workflows/ci.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-corpus/actions) | RAG search over the estate's own docs and repos; public, rate-limited in-app, deterministic chunk IDs make re-ingestion idempotent |
| [`atlas-bootstrap`](https://github.com/AtlasReaper311/atlas-bootstrap) | ![tooling](https://img.shields.io/badge/tooling-aaa9a0?style=flat-square&labelColor=0a0a0f) | [![ci](https://github.com/AtlasReaper311/atlas-bootstrap/actions/workflows/ci.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-bootstrap/actions) | Machine reconstruction: health checks, portproxy refresh as a SYSTEM boot task, repos, env, services, all config-driven JSON |

### Kits and boilerplates

Reusable starting points with production structure baked in. This is the P-02 library.

| Repo | Layer | Pipeline | What it does |
|---|---|---|---|
| [`atlas-kit-python-rag`](https://github.com/AtlasReaper311/atlas-kit-python-rag) | ![library](https://img.shields.io/badge/library-f5a623?style=flat-square&labelColor=0a0a0f) | [![ci](https://github.com/AtlasReaper311/atlas-kit-python-rag/actions/workflows/ci.yml/badge.svg)](https://github.com/AtlasReaper311/atlas-kit-python-rag/actions) | Tested Python RAG library: provider-swappable chunking, embeddings, retrieval, FastAPI |
| [`ollama-rag-kit`](https://github.com/AtlasReaper311/ollama-rag-kit) | ![service](https://img.shields.io/badge/service-f5a623?style=flat-square&labelColor=0a0a0f) | [![ci](https://github.com/AtlasReaper311/ollama-rag-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/AtlasReaper311/ollama-rag-kit/actions) | The same architecture as a deployable multi-container service, entirely local |

The case study pipeline runs private: `atlas-article-gen` (Markdown to site HTML, 76 tests) and `atlas-scheduler` (cron publishing with dry-run simulation, 50 tests) generate and ship everything under `/writing/` without a hand-written tag.

---

## Case studies

Long-form build logs published at [atlas-systems.uk/writing](https://atlas-systems.uk/writing). Each documents the architecture, the bottlenecks hit during development, and the reasoning behind every resolution.

| Project | What it is |
|---|---|
| [SPECULAR-CORE](https://atlas-systems.uk/writing/overclocking-specular-core/) | A full overclocking and tuning pass: memory/fabric sync, a hand-built GPU V/F curve, CCD-aware thread scheduling, validated overnight |
| [Ramone](https://atlas-systems.uk/writing/ramone-local-ai-system/) | Local AI node: Ollama and Open WebUI serving five models on consumer hardware, rebuildable in under 30 minutes |
| [SlamPunk](https://atlas-systems.uk/writing/slampunk-dynamic-mix-engine/) | A 15-stem dynamic mix engine for a competitive arena game |
| [SONIN](https://atlas-systems.uk/writing/sonin-generative-system/) | An autonomous Max/MSP instrument that composes its own evolving music and visuals in real time |

Next: the Pipeline & Observability series, three parts documenting the CI/CD rollout and the estate's self-documentation layer, publishing July through September.

---

## Philosophy

I document every decision. The repos here are meant to be used, not just read: each kit is a module, composable and opinionated and documented. The goal is a GitHub that reads like a library, not a graveyard of submissions.

<div align="center">

[atlas-systems.uk](https://atlas-systems.uk) &nbsp;·&nbsp; [live system map](https://atlas-systems.uk/lab/#system-map) &nbsp;·&nbsp; [atlas@atlas-systems.uk](mailto:atlas@atlas-systems.uk)

```
systems nominal  ●
```

</div>
