-- Dimension table: Users
CREATE TABLE dim_users (
    user_id        VARCHAR(50) PRIMARY KEY,
    user_name      VARCHAR(100),
    user_email     VARCHAR(150),
    created_date   TIMESTAMP
)
DISTSTYLE ALL;

-- Dimension table: Event Types
CREATE TABLE dim_event_types (
    event_type_id  VARCHAR(50) PRIMARY KEY,
    event_name     VARCHAR(100)
)
DISTSTYLE ALL;

-- Fact table: Events
CREATE TABLE fact_events (
    event_id       VARCHAR(50),
    user_id        VARCHAR(50),
    event_type_id  VARCHAR(50),
    event_time     TIMESTAMP,
    ingestion_time TIMESTAMP DEFAULT GETDATE()
)
DISTKEY(user_id)
SORTKEY(event_time);
