# NETWORK CONFIGURATION: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Virtual Private Cloud (VPC) Setup
- **VPC Range**: `10.0.0.0/16` (65,536 IPs).
- **Regions**: Multi-AZ (at least 3 zones for high availability).

## 2. Subnet Allocation
| Subnet Type | Availability Zone | CIDR Range | Usage |
| :--- | :--- | :--- | :--- |
| **Public** | Zone A/B/C | `10.0.1.0/24` | ALB, NAT Gateways |
| **Private App** | Zone A/B/C | `10.0.10.0/24`| EKS Nodes (Backend/Front) |
| **Private Data** | Zone A/B/C | `10.0.20.0/24`| RDS, ElastiCache |

## 3. Security Rules (Security Groups & NACLs)
### Public Security Group (ALB)
- **Inbound**: 443 (HTTPS) from Everywhere.
- **Outbound**: All to Private App Subnets.

### Application Security Group (EKS)
- **Inbound**: 8000/3000 from Public ALB.
- **Inbound**: 6379 (Redis) / 5432 (Postgres) internally.
- **Outbound**: To Data Security Group.

### Data Security Group (RDS/Redis)
- **Inbound**: 5432/6379 ONLY from Application Security Group.
- **Outbound**: Deny All (Except for system updates).

## 4. Traffic Flow Control
- **NAT Gateway**: Ensures private subnets can download updates/patches without being exposed.
- **Internet Gateway**: Only attached to the Public Subnet for ALB access.

---
**Verdict**: Network configuration is hardened. Data tier is strictly isolated from the public internet.
