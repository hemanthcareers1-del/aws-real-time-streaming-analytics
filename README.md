# Real-Time Streaming & Analytics Platform on AWS

This repository contains a **graduate-level academic project** developed during my Master’s program, focused on designing and implementing a real-time streaming and analytics platform using AWS-native services.

The project simulates an enterprise data engineering environment to ingest, process, and analyze high-velocity event data for near real-time business insights.

---

## Architecture Overview
The platform follows a scalable streaming and analytics architecture:

- **Data Sources:** Application events, clickstream data, REST API feeds  
- **Streaming Ingestion:** Amazon Kinesis Data Streams  
- **Processing:** AWS Glue (PySpark – streaming & batch)  
- **Storage:** Amazon S3 (raw, processed, curated zones)  
- **Analytics Warehouse:** Amazon Redshift  
- **Orchestration:** AWS Step Functions, AWS Lambda  
- **Visualization:** Amazon QuickSight  
- **Monitoring:** Amazon CloudWatch  
- **Infrastructure as Code:** Terraform  

---

## Key Features
- Real-time streaming ingestion and processing
- Incremental and micro-batch data pipelines
- Star-schema data modeling for analytics
- Role-based analytics access
- Automated orchestration and monitoring
- Cost-optimized cloud architecture

---

## Technologies Used
AWS Glue, Amazon Kinesis, Amazon S3, Amazon Redshift, AWS Lambda, Step Functions, Amazon QuickSight, CloudWatch, Terraform, Python (PySpark), SQL

---

## Project Context
This project was completed as part of a **Master’s in Analytics & Systems** program and was designed to mirror real-world cloud data engineering use cases and architectural patterns.

