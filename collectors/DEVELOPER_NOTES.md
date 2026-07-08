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