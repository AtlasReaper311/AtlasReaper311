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
[deploy]   ● operational · 3b3dcb6 · 2026-07-22 17:16 UTC
[estate]   31 public repos · 11 stars
[activity] 1256 commits in the last 90 days
[writing]  W-04 · Overclocking SPECULAR-CORE · 2026-06-22
atlas@SPECULAR-CORE:~$ _
```

![estate: 31 repos](https://img.shields.io/badge/estate-31_repos-f5a623?style=flat-square&labelColor=0a0a0f) ![deploy: operational](https://img.shields.io/badge/deploy-operational-4ade80?style=flat-square&labelColor=0a0a0f) [![writing: W-04](https://img.shields.io/badge/writing-W--04-e8e8e0?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk/writing/overclocking-specular-core/)

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
atlas-reaper  // local AI · audio systems · deployment infrastructure
```

---

## The architecture

I build at the intersection of audio systems, local AI, and deployment infrastructure. The three share one core problem: making complex, dynamic systems behave predictably under pressure.

Final year at Abertay University, Saltire Scholar. Building Atlas Systems before I graduate. The public repositories below are the source and reusable engineering surface behind [atlas-systems.uk](https://atlas-systems.uk). The public Worker registry is fail-closed: only explicitly approved public services are documented and rendered by the site. Internal owner-operated systems remain outside the public topology while retaining their own CI and governance.

```text
P-01  Live domain        atlas-systems.uk, a deployed technical environment     [active]
P-02  GitHub library     Modular kits and Logic Lego components                 [building]
P-03  DevOps core        Docker · GitHub Actions · AWS Cloud Practitioner       [active]
P-04  Honours project    LLM integration with UE5 audio systems                 [planned]
P-05  Technical writing  Build logs and case studies on the domain              [active]
```

```text
        public edge                              SPECULAR-CORE (LAN)
  ┌─────────────────────────┐   cloudflared   ┌──────────────────────┐
  │ approved public workers │ ═══ tunnel ═══> │ telemetry · corpus  │
  │ api.atlas-systems.uk    │                 │ ramone · ollama     │
  └─────────────────────────┘                 └──────────────────────┘
        public runtime map: atlas-systems.uk/lab/#system-map
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

## Public repositories

The public estate map lives in [`atlas-api-public/data/estate.manifest.json`](https://github.com/AtlasReaper311/atlas-api-public/blob/main/data/estate.manifest.json). The public registry shows approved live Workers; the manifest describes the intentionally published architecture. Repository visibility is not inferred from account membership.

### Production infrastructure

| Repo | Layer | What it does |
|---|---|---|
| [`atlas-systems`](https://github.com/AtlasReaper311/atlas-systems) | frontend | Hand-built public site and Lab surface |
| [`status`](https://github.com/AtlasReaper311/status) | frontend | Live public status surface |
| [`atlas-doc-viewer`](https://github.com/AtlasReaper311/atlas-doc-viewer) | frontend | Cross-device public document viewer |
| [`atlas-api-public`](https://github.com/AtlasReaper311/atlas-api-public) | public API | Versioned public API and declared public topology |
| [`atlas-api-index`](https://github.com/AtlasReaper311/atlas-api-index) | registry | Fail-closed public Worker metadata registry |
| [`atlas-notify`](https://github.com/AtlasReaper311/atlas-notify) | event bus | Central operational event router with a sanitized public event projection |
| [`github-pulse`](https://github.com/AtlasReaper311/github-pulse) | data layer | GitHub activity proxy with public detail and anonymous aggregate activity |
| [`site-pulse`](https://github.com/AtlasReaper311/site-pulse) | data layer | Cached Cloudflare Analytics projection |
| [`deploy-watch`](https://github.com/AtlasReaper311/deploy-watch) | data layer | Public Pages deployment outcome monitor |
| [`atlas-blackbox`](https://github.com/AtlasReaper311/atlas-blackbox) | observability | Incident evidence recorder |
| [`atlas-dora`](https://github.com/AtlasReaper311/atlas-dora) | observability | Aggregate DORA and release-reliability metrics |

### Local AI and edge

| Repo | Layer | What it does |
|---|---|---|
| [`specular-telemetry`](https://github.com/AtlasReaper311/specular-telemetry) | telemetry | Bounded workstation telemetry through a public edge projection |
| [`specular-sonify`](https://github.com/AtlasReaper311/specular-sonify) | audio | Telemetry-derived sonification frames |
| [`specular-sentinel`](https://github.com/AtlasReaper311/specular-sentinel) | observability | Local infrastructure health observer |
| [`atlas-corpus`](https://github.com/AtlasReaper311/atlas-corpus) | RAG | Semantic search over public estate source and published material |
| [`ramone-edge`](https://github.com/AtlasReaper311/ramone-edge) | edge | Bounded public gateway to local AI services |
| [`ramone-memory`](https://github.com/AtlasReaper311/ramone-memory) | local AI | Ollama-compatible long-term memory layer |
| [`ramone-voice-trigger`](https://github.com/AtlasReaper311/ramone-voice-trigger) | automation | Authenticated allowlisted workflow dispatch |

### DevOps and reusable kits

| Repo | Layer | What it does |
|---|---|---|
| [`atlas-infra`](https://github.com/AtlasReaper311/atlas-infra) | CI/CD | Reusable workflows, public runtime contracts, policy and runbooks |
| [`atlas-bootstrap`](https://github.com/AtlasReaper311/atlas-bootstrap) | recovery | Cross-machine reconstruction automation |
| [`atlas-journey-watch`](https://github.com/AtlasReaper311/atlas-journey-watch) | assurance | Synthetic journeys across public surfaces |
| [`atlas-dep-audit`](https://github.com/AtlasReaper311/atlas-dep-audit) | assurance | SBOM, OSV, action pin and provenance audit |
| [`atlas-resource-audit`](https://github.com/AtlasReaper311/atlas-resource-audit) | assurance | Read-only Cloudflare resource reconciliation |
| [`atlas-gardener`](https://github.com/AtlasReaper311/atlas-gardener) | tooling | Bounded estate conformance remediation proposals |
| [`atlas-badges`](https://github.com/AtlasReaper311/atlas-badges) | tooling | Evidence-backed engineering concept badges |
| [`worker-meta-kit`](https://github.com/AtlasReaper311/worker-meta-kit) | kit | Shared Worker metadata convention |
| [`atlas-kit-python-rag`](https://github.com/AtlasReaper311/atlas-kit-python-rag) | library | Reusable Python RAG package |
| [`ollama-rag-kit`](https://github.com/AtlasReaper311/ollama-rag-kit) | kit | Local Docker, FastAPI and Chroma RAG starter |

---

## Case studies

Long-form build logs are published at [atlas-systems.uk/writing](https://atlas-systems.uk/writing). Each documents architecture, constraints, failures, and the reasoning behind the final design.

| Project | What it is |
|---|---|
| [SPECULAR-CORE](https://atlas-systems.uk/writing/overclocking-specular-core/) | A full overclocking and tuning pass with measured stability validation |
| [Ramone](https://atlas-systems.uk/writing/ramone-local-ai-system/) | Local AI node with Ollama, Open WebUI and reproducible infrastructure |
| [SlamPunk](https://atlas-systems.uk/writing/slampunk-dynamic-mix-engine/) | A 15-stem dynamic mix engine for a competitive arena game |
| [SONIN](https://atlas-systems.uk/writing/sonin-generative-system/) | An autonomous Max/MSP instrument that composes evolving music and visuals |

---

## Philosophy

I document decisions and build systems that can explain their own current state. Public architecture should be explicit rather than inferred; private operational systems should remain governed without becoming portfolio inventory.

<div align="center">

[atlas-systems.uk](https://atlas-systems.uk) &nbsp;·&nbsp; [live system map](https://atlas-systems.uk/lab/#system-map) &nbsp;·&nbsp; [atlas@atlas-systems.uk](mailto:atlas@atlas-systems.uk)

```text
systems nominal  ●
```

</div>
