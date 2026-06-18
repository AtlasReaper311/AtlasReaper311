<!--
  AtlasReaper311 :: GitHub profile README
  atlas-systems.uk
-->

<div align="center">
  <img src="https://raw.githubusercontent.com/AtlasReaper311/AtlasReaper311/main/atlas-icon-dark-256.png" width="120" alt="Atlas Systems"/>
</div>

<div align="center">

# Atlas Reaper

**audio systems · local AI infrastructure · devops**

[![Site](https://img.shields.io/badge/atlas--systems.uk-live-f5a623?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk)
[![CV](https://img.shields.io/badge/cv.atlas--systems.uk-resume-555560?style=flat-square&labelColor=0a0a0f)](https://cv.atlas-systems.uk)
[![Status](https://img.shields.io/badge/systems-nominal-4ade80?style=flat-square&labelColor=0a0a0f)](https://status.atlas-systems.uk)

</div>

```console
atlas@SPECULAR-CORE:~$ whoami
atlas-reaper  //  audio systems · local AI · deployment infrastructure
```
<details>
  <summary><code>atlas@SPECULAR-CORE:~$ curl https://api.atlas-systems.uk/</code></summary>

---

## The architecture

I build at the intersection of audio systems, local AI, and deployment infrastructure. The three share one core problem: making complex, dynamic systems behave predictably under pressure.

Final year at Abertay University, Saltire Scholar. Building Atlas Systems before I graduate. The repositories below are the backend that runs [atlas-systems.uk](https://atlas-systems.uk); the site is the front of the same system, not a separate thing.

```
P-01  Live domain        atlas-systems.uk, a deployed technical environment     [active]
P-02  GitHub library     Modular kits and Logic Lego components                 [building]
P-03  DevOps core        Docker · GitHub Actions · AWS Cloud Practitioner       [active]
P-04  Honours project    LLM integration with UE5 audio systems                 [planned]
P-05  Technical writing  Build logs and case studies on the domain              [active]
```

---

## Stack

| Domain | Tools |
|---|---|
| Languages | Python · C++ · JavaScript · HTML/CSS |
| Game dev | Unreal Engine 5 · MetaSounds · Blueprints |
| AI/ML | RAG pipelines · local LLMs (Ollama) · ChromaDB · Open WebUI |
| Infrastructure | Docker · Cloudflare Workers · Cloudflare Pages · GitHub Actions |
| In progress | AWS · docker-compose orchestration · CI/CD automation |

---

## Repositories

The backend of the platform, grouped by the layer it sits in. Each repo is built to be read and reused, not just looked at.

### Live infrastructure

The deployed system behind the domain. These run.

| Repo | Layer | What it does |
|---|---|---|
| [`atlas-systems`](https://github.com/AtlasReaper311/atlas-systems) | ![frontend](https://img.shields.io/badge/frontend-4ade80?style=flat-square&labelColor=0a0a0f) | Hand-built site source; deploys to atlas-systems.uk on every push |
| [`atlas-notify`](https://github.com/AtlasReaper311/atlas-notify) | ![event bus](https://img.shields.io/badge/event%20bus-f5a623?style=flat-square&labelColor=0a0a0f) | Cloudflare Worker that routes events from every service into one Discord channel |
| [`github-pulse`](https://github.com/AtlasReaper311/github-pulse) | ![data layer](https://img.shields.io/badge/data%20layer-f5a623?style=flat-square&labelColor=0a0a0f) | Cloudflare Worker serving live GitHub stats to the homepage, token held server-side |
| [`atlas-doc-viewer`](https://github.com/AtlasReaper311/atlas-doc-viewer) | ![tooling](https://img.shields.io/badge/tooling-aaa9a0?style=flat-square&labelColor=0a0a0f) | Cross-device PDF wrapper; serves the CV at cv.atlas-systems.uk |
| [`atlas-infra`](https://github.com/AtlasReaper311/atlas-infra) | ![ci/cd](https://img.shields.io/badge/ci%2Fcd-aaa9a0?style=flat-square&labelColor=0a0a0f) | Docker patterns, deploy workflows, and cross-platform ops scripts |

### Kits and boilerplates

Reusable starting points with production structure baked in. This is the P-02 library.

| Repo | Layer | What it does |
|---|---|---|
| [`atlas-kit-python-rag`](https://github.com/AtlasReaper311/atlas-kit-python-rag) | ![library](https://img.shields.io/badge/library-f5a623?style=flat-square&labelColor=0a0a0f) | Tested Python RAG library: provider-swappable chunking, embeddings, retrieval, FastAPI |
| [`ollama-rag-kit`](https://github.com/AtlasReaper311/ollama-rag-kit) | ![service](https://img.shields.io/badge/service-f5a623?style=flat-square&labelColor=0a0a0f) | The same architecture as a deployable multi-container service, entirely local |

---

## Case studies

Long-form build logs published at [atlas-systems.uk/writing](https://atlas-systems.uk/writing). Each documents the architecture, the bottlenecks hit during development, and the reasoning behind every resolution.

| Project | What it is |
|---|---|
| [Ramone](https://atlas-systems.uk/writing/ramone-local-ai-system/) | Local AI node: Ollama and Open WebUI serving five models on consumer hardware, rebuildable in under 30 minutes |
| [SlamPunk](https://atlas-systems.uk/writing/slampunk-dynamic-mix-engine/) | A 15-stem dynamic mix engine for a competitive arena game |
| [SONIN](https://atlas-systems.uk/writing/sonin-generative-system/) | An autonomous Max/MSP instrument that composes its own evolving music and visuals in real time |

---

## Philosophy

I document every decision. The repos here are meant to be used, not just read: each kit is a module, composable and opinionated and documented. The goal is a GitHub that reads like a library, not a graveyard of submissions.

<div align="center">

[atlas-systems.uk](https://atlas-systems.uk) &nbsp;·&nbsp; [atlas@atlas-systems.uk](mailto:atlas@atlas-systems.uk)

```
systems nominal  ●
```

</div>
