# Pepkio DNA RevComp & Primer Toolkit

Perform automated reverse complementation, IUPAC degenerate nucleotide decoding, and thermodynamic primer quality control for DNA and RNA sequences via Python or CLI.

# What It Does

Designing primers, probe oligonucleotides, and sequencing constructs requires converting target nucleic acid sequences into their antiparallel 5' to 3' reverse complements. Manual sequence editing or basic text reversal often causes orientation mistakes (leaving sequences in 3' to 5' order), omits complementary base substitution, or fails when processing IUPAC degenerate bases.

This package provides a Python client and CLI interface for the Pepkio Tools REST API calculation engine. It converts DNA and RNA sequences into exact reverse complement, complement, or reversed outputs, resolves IUPAC ambiguity codes, and evaluates biophysical primer quality control (QC) metrics—including melting temperature ($T_m$), GC content percentage, single-stranded molecular weight, 3' GC clamp status, and potential hairpin or self-dimerization regions.

Programmatic runs require an active network connection and a Pepkio API key. Calculations are processed via the remote API service.

# Features

- **Directional Sequence Transformations**: Computes 5' $\rightarrow$ 3' Reverse Complement, 5' $\rightarrow$ 3' Complement, 3' $\rightarrow$ 5' Reverse, and DNA/RNA conversions.
- **IUPAC Degenerate Base Support**: Full mapping for standard nucleotide ambiguity codes (R, Y, S, W, K, M, B, D, H, V, N) and their complements.
- **Dual Melting Temperature Engine**: Evaluates basic Wallace rule $T_m$ ($2(A+T) + 4(G+C)$) and salt-corrected Nearest-Neighbor thermodynamics.
- **Biophysical Profiling**: Calculates sequence length (bp), exact GC content (%), and single-stranded molecular weight ($g/\text{mol}$).
- **Primer Quality Control**: Flags suboptimal GC content (<40% or >60%), 3' GC clamp status, poly-N/homopolymer runs, hairpins, and self-dimerization.
- **Batch & FASTA Input Processing**: Supports multi-sequence FASTA, CSV, TSV, or newline-delimited inputs for batch primer verification.
- **API Manifest & Examples**: Inspect available examples and inputs using `get_manifest()`, `list_examples()`, and `get_example_input()`.
- **Command-Line Interface**: Run calculations or inspect manifests directly via `pepkio-dna-revcomp-primer-toolkit`.

# Installation

```bash
pip install pepkio-dna-revcomp-primer-toolkit
```

Set your API key as an environment variable before running calculations:

```bash
export PEPKIO_API_KEY="your-api-key"
```

You can obtain an API key from your [Pepkio account API keys](https://www.pepkio.com/account/api-keys) setting page.

# Quick Example

```python
from pepkio_dna_revcomp_primer_toolkit import PepkioClient

with PepkioClient() as client:
    # Analyze a single primer (e.g. GAPDH forward primer)
    result = client.run({
        "mode": "single",
        "sequence": "GAAGGTGAAGGTCGGAGTC",
        "uppercase": True,
        "output_nucleotide": "dna"
    })
    
    data = result.result["single"]
    print("Input (5'->3'):", data["input"])
    print("Reverse Complement (5'->3'):", data["rev_complement"])
    print("GC Content (%):", data["qc"]["gc_percent"])
    print("Wallace Tm (°C):", data["qc"]["tm_wallace_c"])
```

Run via the command-line interface:

```bash
pepkio-dna-revcomp-primer-toolkit run --example single_gapdh_primer
```

Inspect the tool manifest without an API key:

```bash
pepkio-dna-revcomp-primer-toolkit manifest
```

# Typical Use Cases

- Converting target DNA or RNA coding sequences into 5' $\rightarrow$ 3' antiparallel reverse primers for PCR, qPCR, and RT-PCR.
- Reversing and complementing Sanger sequencing traces generated with reverse primers to align in sense orientation.
- Generating complementary overhang sequences for multi-fragment Gibson Assembly, Golden Gate cloning, and site-directed mutagenesis.
- Designing antisense oligonucleotides (ASO), small interfering RNAs (siRNA), and short hairpin RNAs (shRNA) targeting specific mRNA regions.
- Converting degenerate consensus primer motifs containing IUPAC codes into reverse complement primer pools for metagenomic profiling.
- Batch verifying NGS index primers and adapter barcode orientations prior to high-throughput oligonucleotide synthesis orders.

# Scientific Background

Nucleic acid hybridization depends on antiparallel strand orientation (5' to 3' binding against 3' to 5'). Standard PCR primers extend from the 3'-hydroxyl terminus toward the 5' direction of the template strand. Naive string reversal reverses character order without complementary base substitution ($A \leftrightarrow T$, $G \leftrightarrow C$), producing inverted 3' $\rightarrow$ 5' sequences that fail in polymerase amplification.

Melting temperature ($T_m$) reflects the midpoint of thermal denaturation. For short oligonucleotides (<14 bp), the Wallace rule provides a quick estimate based on hydrogen bonding capacity. For longer oligos, Nearest-Neighbor thermodynamics accounts for adjacent base-stacking interactions and monovalent cation concentration ($[\text{Na}^+]$). IUPAC ambiguity codes handle degenerate position positions in primers designed for polymorphic or multi-species targets.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available:

Web Application: https://www.pepkio.com/tools/dna-revcomp-primer-toolkit

The web application provides interactive sequence entry, real-time visual QC alerts, printable laboratory worksheets, and shareable permalink URLs for collaboration and electronic lab notebook (ELN) records.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-dna-revcomp-primer-toolkit

Web Application: https://www.pepkio.com/tools/dna-revcomp-primer-toolkit

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

# Keywords

reverse complement calculator, DNA reverse complement, RNA reverse complement, primer reverse complement, oligonucleotide complement, IUPAC degenerate bases, IUPAC complement calculator, primer melting temperature, Wallace Tm calculator, nearest neighbor Tm, primer GC content, primer molecular weight, 3 GC clamp, primer secondary structure, hairpin loop detection, self dimer primer, PCR primer design, qPCR primer QC, Sanger sequencing reverse complement, Gibson assembly overhang, antisense oligonucleotide design, siRNA reverse complement, NGS index primer verification, degenerate primer pool, batch reverse complement, FASTA reverse complement, Python sequence conversion, pepkio-dna-revcomp-primer-toolkit, bioinformatics oligonucleotide toolkit, how to calculate DNA reverse complement 5 to 3, reverse complement IUPAC ambiguity codes, calculate primer melting temperature nearest neighbor, check primer 3 prime GC clamp online, batch convert FASTA primers reverse complement, generate reverse primer sequence from CDS target, reverse complement RNA sequence to DNA primer, verify Illumina index primer 5 to 3 orientation, Gibson assembly overhang complementary sequence generator, siRNA antisense target sequence calculator, python API DNA reverse complement primer QC
