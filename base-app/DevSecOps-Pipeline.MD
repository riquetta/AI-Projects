## 🔐 DevSecOps Pipeline Flow

```mermaid
flowchart TD
    A[💻 Developer] -->|Push code / Open PR| B[🔄 GitHub Actions CI/CD]

    B --> C[🐍 Install Python Dependencies]
    C --> D[🔍 Static Code Analysis - Bandit]
    C --> E[📦 Dependency Audit - pip-audit / safety]

    D --> F{Any issues?}
    E --> F

    F -->|Yes| G[❌ Fail Pipeline<br/>Report Issues]
    F -->|No| H[✅ Pass Checks]

    H --> I[🏗️ Build & Test Application]
    I --> J[🚀 Deploy to Environment<br/>Dev / Staging / Prod]
