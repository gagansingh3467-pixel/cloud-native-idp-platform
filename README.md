# Cloud-Native Internal Developer Platform (IDP)

A self-hosted Internal Developer Platform that provides a GitHub Actions–like CI/CD engine, a Zero-Trust API Gateway, and a centralized Log Analytics system.

This project focuses on **platform engineering concepts** such as reliability, security, and observability rather than user-facing application features.

## 🏗 Architecture Diagram

![IDP Architecture](docs/architecture.png)
---

## 🚀 What This Platform Does

- Triggers CI pipelines via webhooks
- Executes builds asynchronously using workers
- Builds Docker images from services
- Secures all APIs using Zero-Trust principles
- Collects and indexes logs centrally
- Visualizes logs using Grafana

The **platform itself is the product**.

---

## 🧱 Architecture Overview

Client / GitHub
↓
Zero-Trust API Gateway (Nginx)
↓
CI/CD Backend (FastAPI)
↓
PostgreSQL (Pipeline State)
↓
Redis (Job Queue)
↓
Worker (Docker Build Executor)
↓
OpenSearch (Log Storage)
↓
Grafana (Visualization)



---

## 🔐 Zero-Trust Security

- Backend is **not publicly exposed**
- All requests pass through an API Gateway
- Token-based authentication
- Rate limiting and request auditing
- No implicit trust between services

---

## ⚙️ CI/CD Engine Features

- Webhook-triggered pipelines
- Asynchronous job execution
- Pipeline lifecycle tracking (QUEUED, RUNNING, SUCCESS, FAILED)
- Docker-based build execution
- Fault-tolerant startup (DB & Redis retries)

---

## 📊 Observability & Log Analytics

- Centralized log ingestion API
- Per-service log indices
- OpenSearch used as log store
- Grafana used for log search and visualization
- Logs include service name, level, timestamp, and pipeline ID

---

## 🛠 Tech Stack

### Backend & Control Plane
- FastAPI
- PostgreSQL
- Redis

### CI/CD & Execution
- Docker
- Asynchronous workers

### Security
- Nginx (Zero-Trust API Gateway)
- Token-based access control
- Rate limiting

### Observability
- OpenSearch
- Grafana

### Platform
- Docker Compose
- Linux

---

## 🧠 Why This Project?

Modern teams need:
- Reliable CI/CD pipelines
- Secure internal APIs
- Centralized observability

This project demonstrates **how such a platform can be built from scratch**, focusing on:
- System design
- Reliability
- Security boundaries
- Observability

---

## 📌 Status

- CI/CD Core: ✅ Complete  
- Zero-Trust Gateway: ✅ Implemented  
- Log Analytics Backend: ✅ Implemented  
- Dashboards & Alerts: ⏳ Optional Enhancements  

---

## 📎 Note

This is a **platform engineering project**, not a user-facing application.

   

