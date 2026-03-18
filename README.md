# AWS Security Scanner — Boto3 Practice
Python scripts implementing CIS AWS Foundations Benchmark checks using Boto3 — scanning S3, IAM, and EC2 for real-world misconfigurations.
Built as practice toward a Cloud Security Engineer career.

## Checks implemented
- S3: public access block detection
- IAM: users without MFA  
- EC2: dangerous ports open to 0.0.0.0/0

## How to run
- In place of an actual AWS infrastructure I downloaded Localstack on to my local machine to emulate a real AWS infrastructure and intentionally made it vulnerable for the checks.

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Python 3.8+

### 1. Install dependencies
pip install boto3 awscli-local

### 2. Start LocalStack
docker run --rm -p 4566:4566 localstack/localstack

### 3. Seed fake AWS resources to test against
Run the setup script to create intentionally misconfigured resources:

python seed_localstack.py

### 4. Run a check
python exercise_2.py
