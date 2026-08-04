# pepkio-dna-revcomp-primer-toolkit

Python client for the Pepkio **DNA RevComp & Primer Toolkit** REST API.

## Installation

```bash
pip install pepkio-dna-revcomp-primer-toolkit
```

## Quick Start

```python
from pepkio_dna_revcomp_primer_toolkit import PepkioClient

client = PepkioClient(api_key="your_api_key")
result = client.run({"mode": "single", "sequence": "GAAGGTGAAGGTCGGAGTC"})
print(result.result["single"]["rev_complement"])
```

## CLI Usage

```bash
pepkio-dna-revcomp-primer-toolkit manifest
pepkio-dna-revcomp-primer-toolkit run --example single_gapdh_primer
```
