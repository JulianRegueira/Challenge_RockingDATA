# Entity Relationship Diagram – Streaming Platforms

Este diagrama muestra el flujo desde RAW hasta PROCESSED.

```mermaid

erDiagram

    %% =====================
    %% RAW
    %% =====================

    RAW_NETFLIX {
        string show_id
        string type
        string title
        string director
        string cast
        string country
        date   date_added
        int    release_year
        string rating
        string duration
        string listed_in
        string description
        string platform
        datetime audit_created
        datetime audit_updated
    }

    RAW_DISNEY {
        string show_id
        string type
        string title
        string director
        string cast
        string country
        date   date_added
        int    release_year
        string rating
        string duration
        string listed_in
        string description
        string platform
        datetime audit_created
        datetime audit_updated
    }

    %% =====================
    %% CORE
    %% =====================

    TITLES {
        int title_id PK
        string show_id
        string title
        string type
        int release_year
        string rating
        int duration_minutes
        date date_added
        string description
        int platform_id FK
        datetime created_at
        datetime updated_at
    }

    %% =====================
    %% DIMENSIONS
    %% =====================

    PLATFORMS {
        int platform_id PK
        string name
        datetime audit_created
        datetime audit_updated
    }

    DIRECTORS {
        int director_id PK
        string name
    }

    ACTORS {
        int actor_id PK
        string name
    }

    %% =====================
    %% BRIDGE TABLES
    %% =====================

    TITLE_DIRECTORS {
        int title_id FK
        int director_id FK
    }

    TITLES_ACTORS {
        int title_id FK
        int actor_id FK
    }

    %% =====================
    %% RELATIONSHIPS
    %% =====================

    RAW_NETFLIX ||--o{ TITLES : feeds
    RAW_DISNEY  ||--o{ TITLES : feeds

    PLATFORMS ||--o{ TITLES : has

    TITLES ||--o{ TITLE_DIRECTORS : maps
    DIRECTORS ||--o{ TITLE_DIRECTORS : assigned

    TITLES ||--o{ TITLES_ACTORS : maps
    ACTORS ||--o{ TITLES_ACTORS : assigned

