I built this project to explore how security expertise can be expressed through software. I am using Python to demonstrate an approach to seurity compliance automation. In this project, individual audit agents evaluate specific security controls and I built an orchestrator to coordinate everything and display the findings. 

This project demonstrates object-oriented programming and the orchestrator pattern as the foundation for future integrations with JSON, AWS services, and cloud security automation.

## Version History

- v1: Used Python dictionaries and lists for sample data.
- v2: Added JSON-based sample data loading to separate configuration/data from application logic.
- v3: AWS AM Collector
      boto3 integration
      Live AWS evidence collection
      Normalized IAM user model
- v4: Added S3 collector and initial S3 audit agent.
      Collects normalized S3 bucket evidence.
      Evaluates encryption and versioning status.


      ## Purpose

I am a cybersecurity professional focusing on DevSecOps and security automation. My goal is to build practial tools that solve everyday security problems that I encounter.