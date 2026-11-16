# Pepkio DNA RevComp & Primer Toolkit

Execute containerized DNA and RNA reverse complementation, IUPAC degenerate sequence translation, and primer quality-control checks via the Pepkio API without local Python dependencies.

# What It Does

The container runs `pepkio-dna-revcomp-primer-toolkit`, a command-line client for the Pepkio DNA RevComp & Primer Toolkit REST API. It converts DNA and RNA sequences into exact 5' to 3' reverse complements, complements, or reversed strands, resolves standard IUPAC degenerate nucleotide codes, and calculates biophysical quality control metrics including melting temperatures ($T_m$), GC content percentage, molecular weight, 3' GC clamp stability, and potential secondary structures.

Calculations execute on Pepkio servers; provide a network connection and an API key with `tools:run` scope for `run` commands. Inspecting manifests and examples does not require an API key.

# Features

- Directional sequence transformations: 5' to 3' reverse complement, complement, reverse, and DNA/RNA conversions
- IUPAC degenerate nucleotide resolution across standard ambiguity codes (R, Y, S, W, K, M, B, D, H, V, N)
- Dual melting temperature evaluation: basic Wallace rule ($2(A+T) + 4(G+C)$) and salt-adjusted Nearest-Neighbor thermodynamics
- Biophysical profiling: sequence length (bp), exact GC content (%), and single-stranded molecular weight ($g/\text{mol}$)
- Comprehensive primer QC: 3' GC clamp verification, suboptimal GC warnings (<40% or >60%), homopolymer checks, and secondary structure alerts
- Batch and single-sequence processing with structured JSON output
- Preconfigured manifest examples (`single_gapdh_primer`, `batch_two_primers`)
- Manifest and example inspection without an API key

# Quick Start

```bash
docker pull pepkio/dna-revcomp-primer-toolkit:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/dna-revcomp-primer-toolkit:0.1.0 \
  run --example single_gapdh_primer
```

Manifest only (no API key):

```bash
docker run --rm pepkio/dna-revcomp-primer-toolkit:0.1.0 manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Quick Example

Convert and inspect a GAPDH forward primer using the built-in `single_gapdh_primer` dataset:

```bash
export PEPKIO_API_KEY="your-key"

docker run --rm \
  -e PEPKIO_API_BASE_URL=https://tools.pepkio.com \
  -e PEPKIO_API_KEY="$PEPKIO_API_KEY" \
  pepkio/dna-revcomp-primer-toolkit:0.1.0 run --example single_gapdh_primer
```

# Typical Use Cases

- Generating 5' to 3' antiparallel reverse primers for PCR, qPCR, and RT-PCR amplification
- Reversing and complementing Sanger sequencing chromatogram reads for alignment to reference genomes
- Constructing complementary overhangs for Gibson Assembly, Golden Gate cloning, and site-directed mutagenesis
- Designing antisense oligonucleotides (ASO) and siRNA constructs targeting specific mRNA transcripts
- Translating degenerate primer motifs with IUPAC ambiguity codes for environmental metagenomic assays
- Verifying NGS index and adapter orientations prior to high-throughput oligonucleotide synthesis

# Scientific Background

Nucleic acid chains possess intrinsic 5' to 3' polarity determined by the sugar-phosphate backbone. Hybridization during PCR, sequencing, and oligonucleotide assembly requires annealing in an antiparallel orientation. Designing reverse primers or antisense strands necessitates converting sense sequences into their 5' to 3' reverse complements.

Simple character reversal omits base pairing substitutions (A with T, G with C), whereas naive complementation yields 3' to 5' sequences that lead to synthesis failure or improper annealing. Standard molecular biology workflows require deterministic reverse complementation paired with biophysical quality controls—such as melting temperature matching, GC clamp verification, and dimerization risk assessments.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/dna-revcomp-primer-toolkit

The web application provides an interactive sequence workspace, immediate visualization of complements and reverse complements, degenerate codon decoders, and downloadable quality control reports.

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-dna-revcomp-primer-toolkit

Web Application: https://www.pepkio.com/tools/dna-revcomp-primer-toolkit

PyPI Package: https://pypi.org/project/pepkio-dna-revcomp-primer-toolkit/

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

A semantic, AI-native version of this document in the K2F format is available at https://k2f.dev (https://k2f.dev/v/670f4f3b59d222b9aea07bb6001b4e1034e985f087b0da9e167081817c3b1e0c)
