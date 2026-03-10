# STORAGE CONFIGURATION: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Amazon S3 Buckets Setup
To ensure separation of concerns and security:

- `sarita-public-assets`: Static frontend files (CSS, JS, logos).
- `sarita-user-media`: Secure storage for citizen/merchant files (Photos, Docs).
- `sarita-audit-backups`: Immutable storage for ledger and security log archives.
- `sarita-system-logs`: Centralized collection of pod and RDS logs.

## 2. Security & Compliance Hardening
- **Encryption**: AES-256 S3 Managed Server-Side Encryption (SSE-S3).
- **Public Access**: "Block all public access" active for all buckets EXCEPT `public-assets`.
- **IAM Policy**: Least privilege access; pods use **IRSA (IAM Roles for Service Accounts)** to access specific buckets.
- **Versioning**: Enabled for `user-media` to prevent accidental deletion.

## 3. Storage Lifecycle Rules
- **Intelligent Tiering**: Automatically move older files (e.g., 90-day-old logs) to S3 Glacier for cost optimization.
- **Object Lock**: Configured for the `audit-backups` bucket to ensure WORM (Write Once, Read Many) compliance for financial auditing.

## 4. Stability Metrics
- **Durability**: 99.999999999% (S3 Standard).
- **Latency**: Low (Multi-AZ VPC Endpoints active).

---
**Verdict**: File storage is secure, scalable, and follows regulatory data retention standards.
