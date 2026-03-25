# 🏦 Digital Banking Transaction API

Production-ready banking microservice with **Azure DevOps CI/CD pipeline**, **Docker containerization**, and **multi-environment deployment**.

## Features
- **Azure DevOps Pipeline**: Build → Test → Docker Build → Dev Deploy → Prod Approval
- **Banking Domain**: Transaction status, fund transfers (Hexaware-style)
- **Python Flask API**: High-availability transaction processing
- **Docker Multi-stage**: Local dev + production deployment ready

## Quick Start
```bash
# Clone & run locally
git clone https://github.com/jagannadh-kommuri/banking-transaction-api
cd banking-transaction-api
docker-compose up

# Test banking APIs
curl http://localhost:5000/api/transactions/transfer -X POST \
  -H "Content-Type: application/json" \
  -d '{"amount":1000.50,"account":"ACC123","fromAccount":"ACC123","toAccount":"ACC456"}'

curl http://localhost:5000/api/transactions/status/<transaction_id>
