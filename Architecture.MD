## 🧠 Incident Search System – Architecture Overview

```mermaid
flowchart TD
    A[📂 dataset.csv<br/>Incident Data] -->|Load with pandas| B[💾 DataFrame]

    B -->|Extract Title column| C[🔤 Titles List]
    C -->|Encode using SentenceTransformer<br/>all-MiniLM-L6-v2| D[🧮 Case Embeddings]

    subgraph Search_Function [Search Function]
        E[🔍 User Query] -->|Encode| F[📏 Query Embedding]
        F -->|Cosine Similarity| G[📈 Similarity Scores]
        G -->|Filter ≥ Threshold| H[✅ Matching Incidents]
        H -->|Sort Descending| I[📋 Search Results<br/>IncidentId • Title • InternalTitle • Similarity]
    end

    D -->|Compare with| G

    subgraph Gradio_UI [Gradio UI]
        J[🧑‍💻 User Interface]
        J -->|Input Query and Threshold| E
        I -->|Display Results Table| J
    end

    style A fill:#f9f,stroke:#333,stroke-width:1px
    style B fill:#bbf,stroke:#333,stroke-width:1px
    style D fill:#afa,stroke:#333,stroke-width:1px
    style E fill:#ffb,stroke:#333,stroke-width:1px
    style I fill:#bfb,stroke:#333,stroke-width:1px
    style J fill:#fff,stroke:#333,stroke-width:1px