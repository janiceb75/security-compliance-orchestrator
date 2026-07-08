# Developer Notes

These notes document architectural decisions and lessons learned while building the Security Compliance Orchestrator.

---

## AWSIAMCollector

### Why normalize AWS responses?

AWS returns service-specific responses.

The collector converts them into a consistent internal data model so audit agents don't need AWS-specific knowledge.

---

## AWSS3Collector

### Why is normalized_buckets a local variable?

Originally I stored normalized_buckets as an instance attribute. self.normalized_buckets = []

I changed it to a local variable because the list only exists during one execution of list_buckets().  normalized_buckets = []

Using an instance attribute would cause duplicate buckets if list_buckets() were called multiple times on the same object.

Lesson:
Use local variables for temporary working data.
Use instance attributes when the object needs to remember state.

---

## Versioning

AWS omits the Status key when versioning has never been configured.

Using:

versioning.get("Status", "NotConfigured")

normalizes the response into a consistent value.

## Object Initialization

### Question

Do I always need an `__init__()` method?

### Answer

No.

Python automatically creates a default constructor if one is not provided.

This means an object can still be created:

```python
class S3AuditAgent:
    pass

agent = S3AuditAgent()
```

### When should I create an `__init__()`?

Create one when the object needs to initialize attributes.

Example:

```python
class AWSS3Collector:

    def __init__(self):
        self.s3_client = boto3.client("s3")
```

### Lesson Learned

Creating an object and initializing an object are related but different concepts.

- Creating an object:
  ```python
  agent = S3AuditAgent()
  ```

- Initializing an object:
  Happens inside `__init__()` if one exists.

If no `__init__()` is defined, Python uses a default one.

## S3 Audit Agent

- The S3 collector gathers and normalizes bucket evidence.
- The S3 audit agent does not call AWS directly.
- The audit agent receives normalized bucket data and returns findings.
- Findings include the bucket name as context, not as a finding.
- `return` should happen after the loop, so all buckets are evaluated.