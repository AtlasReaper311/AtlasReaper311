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
[deploy]   ● operational · bd18ead · 2026-09-10 14:25 UTC
[estate]   35 governed public repos
[writing]  W-08 · SPECULAR-CORE: Architectural Recovery
atlas@SPECULAR-CORE:~$ _
```

![estate: 35 repos](https://img.shields.io/badge/estate-35_repos-f5a623?style=flat-square&labelColor=0a0a0f) ![deploy: operational](https://img.shields.io/badge/deploy-operational-4ade80?style=flat-square&labelColor=0a0a0f) [![writing: W-08](https://img.shields.io/badge/writing-W--08-e8e8e0?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk/writing/specular-core-architectural-recovery/)

<sub>governed estate + live publish state · refreshes every 6 hours · updates through a validated pull request</sub>
<!-- ATLAS:LIVE:END -->

<div align="center">

# Atlas Reaper

**local AI · automation · infrastructure · real-time audio**

[![Site](https://img.shields.io/badge/atlas--systems.uk-live-f5a623?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk)
[![Map](https://img.shields.io/badge/system%20map-live%20architecture-f5a623?style=flat-square&labelColor=0a0a0f)](https://atlas-systems.uk/lab/#system-map)
[![CV](https://img.shields.io/badge/cv.atlas--systems.uk-resume-555560?style=flat-square&labelColor=0a0a0f)](https://cv.atlas-systems.uk)
[![Status](https://img.shields.io/badge/systems-nominal-4ade80?style=flat-square&labelColor=0a0a0f)](https://status.atlas-systems.uk)
[![Atlas Systems status](https://api.atlas-systems.uk/v1/badge/status)](https://api.atlas-systems.uk/v1/docs)

</div>

```console
atlas@SPECULAR-CORE:~$ whoami
atlas-reaper  // local AI · automation · infrastructure · real-time audio
```

---

## The architecture

I build and operate Atlas Systems, a technical estate spanning local AI, automation, infrastructure, and real-time audio systems. The repositories below are the source and reusable engineering surface behind the public site.

Final-year Game Development student at Abertay University and 2026 Saltire Scholar. Atlas Systems is my independent technical portfolio and engineering estate behind [atlas-systems.uk](https://atlas-systems.uk). The public Worker registry is fail-closed: only explicitly approved public services are documented and rendered by the site. Internal owner-operated systems remain outside the public topology while retaining their own CI and governance.

```text
P-01  Live domain        atlas-systems.uk, a deployed technical environment     [active]
P-02  GitHub library     Modular kits and Logic Lego components                 [building]
P-03  DevOps core        Docker · GitHub Actions · AWS infrastructure            [active]
P-04  Applied Local AI   Local-model evaluation through interactive, game, and    [active]
                         real-time system experiments
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
| Interactive systems | Unreal Engine 5 · MetaSounds · Blueprints · Max/MSP |
| Local AI | llama.cpp · Ollama · RAG · ChromaDB · retrieval · memory · model evaluation |
| Infrastructure | Docker · WSL2 · Cloudflare Workers · Cloudflare Pages · GitHub Actions · AWS |
| Assurance | Observability · CI/CD · recovery · deterministic automation |

---

## Start here

These six repositories are the clearest entry points into the Atlas Systems engineering surface.

| Repository | Domain | Why start here |
|---|---|---|
| [`atlas-systems`](https://github.com/AtlasReaper311/atlas-systems) | public interface | The public site and Lab surface for Atlas Systems |
| [`atlas-infra`](https://github.com/AtlasReaper311/atlas-infra) | governance and operations | Policy, reusable workflows, assurance, recovery, and runbooks |
| [`atlas-api-public`](https://github.com/AtlasReaper311/atlas-api-public) | public API | Versioned API contracts and declared public topology |
| [`atlas-corpus`](https://github.com/AtlasReaper311/atlas-corpus) | local AI and retrieval | Semantic search over public estate source and published material |
| [`specular-telemetry`](https://github.com/AtlasReaper311/specular-telemetry) | observability | Bounded workstation telemetry with a public edge projection |
| [`atlas-gardener`](https://github.com/AtlasReaper311/atlas-gardener) | bounded automation | Estate conformance remediation proposals |

The full governed public repository set is defined by [`atlas-infra/policy/public-repository-classifications.json`](https://github.com/AtlasReaper311/atlas-infra/blob/main/policy/public-repository-classifications.json). Runtime topology remains a separate contract in [`atlas-api-public/data/estate.manifest.json`](https://github.com/AtlasReaper311/atlas-api-public/blob/main/data/estate.manifest.json). GitHub visibility, ADR-0004 scope, `public_surface`, and projection membership are distinct signals.

---

## Selected engineering records

Long-form build logs are published at [atlas-systems.uk/writing](https://atlas-systems.uk/writing). Each documents architecture, constraints, failures, and the reasoning behind the final design.

| Record | What it is |
|---|---|
| [W-08 SPECULAR-CORE: Architectural Recovery](https://atlas-systems.uk/writing/specular-core-architectural-recovery/) | Architectural recovery of the public technical estate |
| [W-06 Atlas Systems CI/CD](https://atlas-systems.uk/writing/atlas-systems-cicd-pipeline/) | CI/CD design, evidence, and controlled delivery |
| [W-03 Ramone local AI system](https://atlas-systems.uk/writing/ramone-local-ai-system/) | Local AI services with reproducible infrastructure |
| [W-02 SlamPunk dynamic mix engine](https://atlas-systems.uk/writing/slampunk-dynamic-mix-engine/) | A dynamic mix engine for a competitive arena game |
| [W-01 SONIN generative system](https://atlas-systems.uk/writing/sonin-generative-system/) | An autonomous Max/MSP instrument for evolving music and visuals |

---

## Philosophy

I document decisions and build systems that can explain their own current state. Public architecture should be explicit rather than inferred; private operational systems should remain governed without becoming portfolio inventory.

<div align="center">

[atlas-systems.uk](https://atlas-systems.uk) &nbsp;·&nbsp; [live system map](https://atlas-systems.uk/lab/#system-map) &nbsp;·&nbsp; [atlas@atlas-systems.uk](mailto:atlas@atlas-systems.uk)

```text
systems nominal  ●
```

</div>
