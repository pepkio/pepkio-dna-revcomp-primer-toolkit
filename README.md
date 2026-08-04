# Pepkio DNA RevComp & Primer Toolkit

Reverse, complement, and reverse-complement DNA and RNA sequences, decode IUPAC degenerate bases, and evaluate PCR primer quality control parameters in Python and via web interface.

# Overview

In molecular biology, nucleic acid sequences possess intrinsic 5' to 3' directionality defined by the phosphodiester backbone. During Polymerase Chain Reaction (PCR), quantitative PCR (qPCR), reverse transcription (RT-PCR), Sanger sequencing, Next-Generation Sequencing (NGS) library preparation, site-directed mutagenesis, and Gibson Assembly, oligonucleotides must hybridize antiparallelly to target DNA or RNA templates. Designing reverse primers, Sanger sequencing primers, or antisense oligos requires converting the target strand sequence (5' $\rightarrow$ 3') into its reverse complement (5' $\rightarrow$ 3').

Manual string reversal or unvalidated string manipulation tools often introduce orientation errors (leaving sequences in the 3' $\rightarrow$ 5' direction), complement inversion mistakes, unhandled IUPAC degenerate nucleotide codes, or incorrect melting temperature ($T_m$) calculations. An improperly oriented primer leads to PCR amplification failure, off-target binding, and wasted synthesis resources.

The **Pepkio DNA RevComp & Primer Toolkit** provides a deterministic sequence transformation library and validation framework. It performs reverse complementation, complementation, reversal, RNA-DNA conversion, IUPAC degenerate base mapping, and biophysical primer quality control (QC). The toolkit calculates sequence length, GC content percentage, molecular weight ($g/\text{mol}$), melting temperature ($T_m$ via Wallace rule and Nearest-Neighbor thermodynamics), 3' GC clamp status, and potential secondary structures.

Researchers can access the hosted [Pepkio DNA RevComp & Primer Toolkit](https://www.pepkio.com/tools/dna-revcomp-primer-toolkit) web application for interactive sequence transformation and primer quality control. A programmatic Python client and command-line interface (CLI) are available for pipeline integration.

Common search terms and alternative terminology for this tool include DNA reverse complement calculator, reverse complement generator, primer reverse complement tool, oligonucleotide complement calculator, DNA sequence reverser, IUPAC degenerate primer calculator, RNA reverse complement converter, primer melting temperature calculator, GC content percentage calculator, Sanger sequencing primer reverse complement, and PCR primer design toolkit.

# Features

- **Directional Sequence Transformations**: Computes exact 5' $\rightarrow$ 3' Reverse Complement, 5' $\rightarrow$ 3' Complement, 3' $\rightarrow$ 5' Reverse, and RNA-to-DNA / DNA-to-RNA conversions.
- **IUPAC Degenerate Base Handling**: Full support for standard IUPAC nucleic acid ambiguity codes (R, Y, S, W, K, M, B, D, H, V, N) with complementary mapping (R $\leftrightarrow$ Y, M $\leftrightarrow$ K, S $\leftrightarrow$ S, W $\leftrightarrow$ W, B $\leftrightarrow$ V, D $\leftrightarrow$ H).
- **Melting Temperature ($T_m$) Calculation Engine**: Dual $T_m$ evaluation using the basic Wallace rule ($2(A+T) + 4(G+C)$) for short oligos and Nearest-Neighbor thermodynamic modeling with salt concentration correction ($[\text{Na}^+]$).
- **Biophysical Property Profiling**: Computes sequence length (bp), exact GC content percentage (%), single-stranded molecular weight ($g/\text{mol}$), and monovalent salt-adjusted stability metrics.
- **Primer Quality Control Analysis**: Identifies 3' GC clamps, checks for suboptimal GC content (outside 40–60%), highlights poly-N or homopolymer runs, and flags potential hairpin loops and self-dimerization regions.
- **Batch & FASTA High-Throughput Processing**: Supports multi-sequence FASTA, CSV, TSV, or newline-delimited inputs for batch primer verification and automated tabular exports.
- **Python API & Command Line Interface**: Asynchronous and synchronous Python client (`pepkio-dna-revcomp-primer-toolkit`) and CLI executable for integration into automated bioinformatics pipelines (Nextflow, Snakemake, Jupyter).
- **Reproducible Permalinks**: Generates permanent calculation URLs to share exact primer parameters across electronic lab notebooks (ELNs) and research teams.

# Common Use Cases

- **Reverse PCR Primer Design**: Convert a target coding sequence (CDS) or genomic region into its antiparallel 5' $\rightarrow$ 3' reverse primer sequence for standard PCR, RT-qPCR, or digital droplet PCR (ddPCR).
- **Sanger Sequencing Trace Alignment**: Reverse complement Sanger sequencing reads generated from reverse sequencing primers (e.g., BGH Reverse, T7 Terminator) to align them in the sense orientation with reference genome sequences.
- **Gibson Assembly Overhang Construction**: Generate antiparallel complementary overhangs for multi-fragment Gibson Assembly, Golden Gate assembly, or site-directed mutagenesis primers.
- **RNAi & Antisense Oligonucleotide (ASO) Synthesis**: Compute the reverse complement of target mRNA regions to synthesize small interfering RNAs (siRNA), short hairpin RNAs (shRNA), or antisense oligos.
- **Multiplex PCR & Degenerate Primer Pools**: Convert consensus degenerate sequence motifs containing IUPAC codes into their reverse complements for pathogen detection or metagenomic amplicon profiling (e.g., 16S rRNA primers 515F / 806R).
- **NGS Adapter & Index Primer Verification**: Process batch Illumina, MGI, or PacBio index primer lists to verify 5' $\rightarrow$ 3' orientation prior to high-throughput oligonucleotide ordering.

# Why This Tool Exists

Conventional text editors, general spreadsheets (Excel, Google Sheets), and simple string reversal tools reverse character order without substituting complementary bases ($A \leftrightarrow T$, $G \leftrightarrow C$). Furthermore, basic command-line utilities (such as `tr 'ATGC' 'TACG'`) often fail to account for standard 5' $\rightarrow$ 3' convention, leaving sequences in the 3' $\rightarrow$ 5' orientation, or break when handling IUPAC ambiguity codes (R, Y, S, W, K, M, B, D, H, V, N) and RNA uracil bases ($U$).

Spreadsheet-based primer tracking sheets frequently introduce orientation errors when reverse primer sequences are manually entered in the 3' $\rightarrow$ 5' direction. This results in PCR failure, non-specific binding, and wasted synthesis reagents.

Existing web utilities often lack comprehensive quality control metrics—such as salt-corrected nearest-neighbor $T_m$ calculation, molecular weight evaluation, 3' GC clamp verification, and structured JSON outputs for computational workflows. The online [DNA reverse complement calculator](https://www.pepkio.com/tools/dna-revcomp-primer-toolkit) provides a validation environment that bridges interactive laboratory research and programmatic bioinformatics pipelines.

# Installation

Install the Python client package from PyPI using `pip`:

```bash
pip install pepkio-dna-revcomp-primer-toolkit
```

Or using `uv`:

```bash
uv add pepkio-dna-revcomp-primer-toolkit
```

The official package distribution is indexed on [PyPI](https://pypi.org/project/pepkio-dna-revcomp-primer-toolkit/).

# Quick Start

### Python API Usage

Set your API key as an environment variable:

```bash
export PEPKIO_API_KEY="your_pepkio_api_key"
```

Execute single sequence transformations or batch processing in Python:

```python
from pepkio_dna_revcomp_primer_toolkit import PepkioClient

# Initialize client
with PepkioClient() as client:
    # 1. Single primer analysis (e.g., GAPDH forward primer)
    result = client.run({
        "mode": "single",
        "sequence": "GAAGGTGAAGGTCGGAGTC",
        "uppercase": True,
        "output_nucleotide": "dna"
    })

    single_data = result.result["single"]
    print("Input Sequence (5'->3'):", single_data["input"])
    print("Reverse Complement (5'->3'):", single_data["rev_complement"])
    print("GC Content (%):", single_data["qc"]["gc_percent"])
    print("Wallace Tm (°C):", single_data["qc"]["tm_wallace_c"])
    print("Permalink:", result.permalink)

    # 2. Batch primer conversion from CSV/FASTA format
    batch_input = {
        "mode": "batch",
        "batch_text": "GAPDH_F,GAAGGTGAAGGTCGGAGTC\nACTB_F,GGCTGGGGTGTTGAAGGT\n"
    }
    batch_result = client.run(batch_input)
    for entry in batch_result.result["batch"]:
        print(f"Name: {entry['name']} | RevComp: {entry['rev_complement']}")
```

### Command Line Interface (CLI)

The package includes a command-line executable `pepkio-dna-revcomp-primer-toolkit`:

```bash
# Process a single DNA sequence
pepkio-dna-revcomp-primer-toolkit run --input '{"mode":"single","sequence":"GAAGGTGAAGGTCGGAGTC"}'

# Process a named example from the manifest
pepkio-dna-revcomp-primer-toolkit run-example single_gapdh_primer
```

Source code and issue tracking are hosted on the [pepkio-dna-revcomp-primer-toolkit GitHub repository](https://github.com/pepkio/pepkio-dna-revcomp-primer-toolkit).

# Example Output

A single sequence transformation request returns a structured JSON envelope containing sequence transformations and biophysical quality control metrics:

```json
{
  "run_id": "run_9f82a1b4c3d0",
  "status": "completed",
  "result": {
    "mode": "single",
    "single": {
      "input": "GAAGGTGAAGGTCGGAGTC",
      "rev_complement": "GACTCCGACCTTCACCTTC",
      "complement": "CTTCCACTTCCAGCCTCAG",
      "reverse": "CTGAGGCTGGAAGTGGAAG",
      "qc": {
        "length_nt": 19,
        "gc_percent": 57.89,
        "tm_wallace_c": 60.0,
        "tm_nearest_neighbor_c": 58.4,
        "molecular_weight_g_mol": 5887.85,
        "has_gc_clamp": true
      }
    },
    "warnings": []
  },
  "error": null,
  "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_9f82a1b4c3d0",
  "permalink": "https://tools.pepkio.com/r/run_9f82a1b4c3d0"
}
```

# Scientific Background

### 5' to 3' Nucleic Acid Directionality & Antiparallel Double Helix

Nucleic acid chains possess directionality defined by the carbon atoms of the deoxyribose or ribose sugar ring. The 5' end terminates in a phosphate group attached to the 5' carbon, while the 3' end terminates in a free hydroxyl group ($-OH$) on the 3' carbon. DNA polymerases synthesize nascent nucleic acid strands strictly in the 5' $\rightarrow$ 3' direction by adding dNTPs to the 3' hydroxyl group.

In double-stranded DNA (dsDNA), the two complementary strands align in an antiparallel orientation: one strand runs 5' $\rightarrow$ 3' and the opposing template strand runs 3' $\rightarrow$ 5'. When designing primers for PCR amplification, both the forward primer (sense orientation) and the reverse primer (antisense orientation) must be specified in standard 5' $\rightarrow$ 3' convention so that DNA synthesis proceeds inward toward the target amplicon region.

### Base Complementarity Rules & RNA Substitution

Watson-Crick base pairing governs double-stranded nucleic acid stability:
- Adenine ($A$) forms two hydrogen bonds with Thymine ($T$) in DNA.
- Guanine ($G$) forms three hydrogen bonds with Cytosine ($C$) in DNA.
- In RNA, Uracil ($U$) replaces Thymine ($T$) and pairs with Adenine ($A$).

| Transformation | Original (5' $\rightarrow$ 3') | Result Strand | Orientation |
| :--- | :--- | :--- | :--- |
| **Input Sequence** | `5'- A T G C G A T C -3'` | Template Strand | 5' $\rightarrow$ 3' |
| **Direct Reverse** | `5'- C T A G C G T A -3'` | Reversed Sequence | 5' $\rightarrow$ 3' |
| **Direct Complement** | `3'- T A C G C T A G -5'` | Antiparallel Strand | 3' $\rightarrow$ 5' |
| **Reverse Complement** | `5'- G A T C G C A T -3'` | Antiparallel Strand | 5' $\rightarrow$ 3' |

### IUPAC Degenerate Base Codes

Degenerate PCR primers target conserved gene regions across divergent species or mutant variants by incorporating IUPAC ambiguous nucleotide codes. The toolkit performs complementary mapping across all IUPAC codes:

| IUPAC Code | Meaning | Complement | Complement Meaning |
| :---: | :---: | :---: | :---: |
| **A** | A | **T** | T |
| **C** | C | **G** | G |
| **G** | G | **C** | C |
| **T / U** | T / U | **A** | A |
| **R** | A or G (puRine) | **Y** | C or T (pYrimidine) |
| **Y** | C or T (pYrimidine) | **R** | A or G (puRine) |
| **S** | C or G (Strong) | **S** | C or G (Strong) |
| **W** | A or T (Weak) | **W** | A or T (Weak) |
| **K** | G or T (Keto) | **M** | A or C (aMino) |
| **M** | A or C (aMino) | **K** | G or T (Keto) |
| **B** | C, G, or T (not A) | **V** | A, C, or G (not T) |
| **D** | A, G, or T (not C) | **H** | A, C, or T (not G) |
| **H** | A, C, or T (not G) | **D** | A, G, or T (not C) |
| **V** | A, C, or G (not T) | **B** | C, G, or T (not A) |
| **N** | A, C, G, or T (Any) | **N** | A, C, G, or T (Any) |

### Melting Temperature ($T_m$) Thermodynamics

Primer melting temperature ($T_m$) is the temperature at which 50% of the oligonucleotide molecules are hybridized to their complementary template.

1. **Wallace Rule (Basic $T_m$)**: Accurate for short oligos (14–20 bp):
   $$T_m = 2(A + T) + 4(G + C)$$

2. **Nearest-Neighbor Thermodynamic Model (SantaLucia 1998)**: Accounts for adjacent base stacking interactions and monovalent salt concentration ($[\text{Na}^+]$):
   $$T_m = \frac{\Delta H^\circ}{\Delta S^\circ + R \ln(C_T / x)} - 273.15 + 16.6 \log_{10}[\text{Na}^+]$$
   where $\Delta H^\circ$ is enthalpy ($\text{cal}/\text{mol}$), $\Delta S^\circ$ is entropy ($\text{cal}/\text{mol}\cdot\text{K}$), $R$ is the gas constant ($1.987 \text{ cal}/\text{mol}\cdot\text{K}$), $C_T$ is total strand concentration (typically $0.2 \ \mu\text{M}$), and $[\text{Na}^+]$ is the monovalent sodium ion concentration (typically $50 \text{ mM}$).

### GC Content & 3' GC Clamp

GC content percentage is computed as:
$$\text{GC \%} = \frac{N_G + N_C}{N_{\text{total}}} \times 100$$
Optimal PCR primers maintain a GC content of 40–60%. A 3' GC clamp presence (1–2 G or C residues in the final 5 bases at the 3' terminus) promotes stable polymerase binding and initiation, whereas excess 3' G/C residues increase non-specific priming.

# Frequently Asked Questions

### What is a reverse complement in molecular biology?
A reverse complement sequence is the antiparallel strand of a nucleic acid written in the standard 5' $\rightarrow$ 3' direction. Because complementary DNA strands pair antiparallelly ($A$ with $T$, $G$ with $C$), deriving the complementary sequence of a 5' $\rightarrow$ 3' strand yields a 3' $\rightarrow$ 5' sequence. Reversing this result converts it back into the standard 5' $\rightarrow$ 3' direction required for primer synthesis and sequence alignment.

### How does a reverse complement differ from a simple reverse or simple complement sequence?
A simple reverse sequence flips the character order (5' $\rightarrow$ 3' becomes 3' $\rightarrow$ 5' sequence of the same strand) without complementary base substitution. A simple complement substitutes bases ($A \rightarrow T$, $G \rightarrow C$) but leaves the strand in the antiparallel 3' $\rightarrow$ 5' direction. A reverse complement performs both operations, returning the antiparallel strand in the standard 5' $\rightarrow$ 3' direction.

### Why must PCR primers always be written in the 5' to 3' direction?
DNA polymerases synthesize DNA strictly in the 5' $\rightarrow$ 3' direction by extending the 3' hydroxyl group of an annealed primer. Commercial oligonucleotide synthesis facilities and sequencing software assume all input strings are oriented 5' $\rightarrow$ 3'. Submitting a primer in 3' $\rightarrow$ 5' orientation will result in synthesis of an inverted oligonucleotide that cannot amplify the intended target region.

### How do I design the reverse primer for a target gene coding sequence?
To design a reverse primer for a coding sequence (CDS): locate the 3' target region on the sense strand (5' $\rightarrow$ 3'), select a 18–25 bp sequence, and take its reverse complement. The resulting 5' $\rightarrow$ 3' sequence will anneal to the sense strand and allow DNA polymerase to extend upstream toward the forward primer.

### How does this tool handle IUPAC degenerate nucleotide codes?
The toolkit decodes IUPAC ambiguous codes (such as R, Y, S, W, K, M, B, D, H, V, N) and maps them to their precise complementary IUPAC symbols (e.g., R $\leftrightarrow$ Y, M $\leftrightarrow$ K, B $\leftrightarrow$ V, D $\leftrightarrow$ H). This preserves exact sequence multiplicity and degeneracy during reverse complement transformations.

### What is the difference between DNA reverse complement and RNA reverse complement?
DNA reverse complementation pairs Adenine ($A$) with Thymine ($T$), whereas RNA reverse complementation pairs Adenine ($A$) with Uracil ($U$). The toolkit supports RNA-to-DNA and DNA-to-RNA mode options for transcribing cDNA primers or antisense RNA probes.

### How do I calculate the melting temperature ($T_m$) of a primer?
Primer $T_m$ can be calculated using two primary models: the basic Wallace rule ($2(A+T) + 4(G+C)$) for short oligonucleotides ($<20$ bp), or the Nearest-Neighbor thermodynamic model for longer primers. Nearest-neighbor algorithms calculate base stacking thermodynamics ($\Delta H^\circ, \Delta S^\circ$) and adjust for monovalent salt concentrations ($[\text{Na}^+]$).

### What is the Wallace rule for calculating primer $T_m$?
The Wallace rule estimates melting temperature for short oligonucleotides (14–20 bp) in standard PCR buffer conditions using the formula: $T_m = 2 \times (A + T) + 4 \times (G + C) \ ^\circ\text{C}$.

### When should I use Nearest-Neighbor thermodynamic calculations instead of the Wallace rule?
Nearest-Neighbor calculations should be used for oligonucleotides longer than 20 nucleotides, primers containing internal mismatches or degenerate bases, and applications requiring precise annealing temperature optimization (e.g., qPCR, multiplex PCR).

### How does monovalent salt concentration ($[\text{Na}^+]$) affect primer melting temperature?
Higher monovalent cation concentrations ($Na^+, K^+$) neutralize the negative electrostatic repulsion of the phosphate backbone, stabilizing duplex hybridization and increasing the $T_m$. The Nearest-Neighbor engine adjusts $T_m$ according to salt concentration changes.

### What is a 3' GC clamp and why is it important in PCR primer design?
A 3' GC clamp consists of 1 to 2 Guanine ($G$) or Cytosine ($C$) bases within the last 5 nucleotides at the 3' end of a primer. Because $G-C$ base pairs form three hydrogen bonds, a 3' GC clamp stabilizes the 3' terminus for DNA polymerase initiation.

### What is the optimal GC content range for PCR primers?
The optimal GC content range for standard PCR primers is 40% to 60%. GC content below 40% may require longer primers to achieve adequate $T_m$, while GC content above 60% increases the risk of secondary structure formation and non-specific binding.

### How do I detect and avoid primer hairpin loops and self-dimers?
Hairpin loops occur when a primer folds back and hybridizes with itself, while self-dimers occur when two identical primer molecules anneal to each other. The toolkit flags self-complementary regions and high 3' binding energy to minimize secondary structure risks.

### Can I process multi-sequence FASTA files in batch mode?
Yes. The toolkit supports batch processing of multi-sequence FASTA files, CSV files, or newline-delimited sequence lists via the Python client, CLI, or web application.

### How do restriction site overhangs or Illumina adapter tails affect reverse complement calculations?
Restriction enzyme recognition sites, promoter tails (e.g., T7, SP6), or Illumina NGS adapters added to the 5' end of a primer must be included when taking the reverse complement of the full primer sequence. However, when calculating $T_m$, only the gene-specific annealing region at the 3' end should be evaluated for initial PCR cycles.

### Why do spreadsheets often introduce orientation errors in primer lists?
Spreadsheets do not natively understand biological sequence orientation. Copying and pasting sequences into text fields without automated direction verification frequently leads to reversed or un-complemented primer entries in inventory databases.

### How do I convert single-stranded RNA sequences to cDNA reverse complement primers?
To design a reverse transcription (RT) primer from an mRNA template (5' $\rightarrow$ 3'), take the reverse complement of the target RNA sequence while converting Uracil ($U$) bases to Thymine ($T$). The resulting DNA primer will anneal to the single-stranded RNA template for cDNA synthesis by reverse transcriptase.

### What molecular weight formula is used for oligonucleotide quantification?
The molecular weight ($g/\text{mol}$) of a single-stranded DNA oligonucleotide is calculated by summing the anhydrous molecular weights of its constituent nucleotides ($A=313.21$, $T=304.2$, $G=329.21$, $C=289.18$) and subtracting $61.96 \ g/\text{mol}$ to account for the removal of water and 5' monophosphate terminal adjustments.

# Web Application

The hosted version of this tool is available at the [Pepkio DNA RevComp & Primer Toolkit](https://www.pepkio.com/tools/dna-revcomp-primer-toolkit) web application.

The web application provides an interactive interface, shareable permalinks, protocol generation, printable worksheets, and visualization tools for PCR primer evaluation and batch sequence processing.

Web Application: https://www.pepkio.com/tools/dna-revcomp-primer-toolkit

# Related Resources

- GitHub Repository: https://github.com/pepkio/pepkio-dna-revcomp-primer-toolkit
- PyPI Package: https://pypi.org/project/pepkio-dna-revcomp-primer-toolkit/
- Web Application: https://www.pepkio.com/tools/dna-revcomp-primer-toolkit

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

Pepkio's bioinformatics capabilities include:
- RNA-seq analysis
- Single-cell RNA-seq analysis
- Spatial transcriptomics analysis
- Functional enrichment analysis
- Custom bioinformatics workflows

Website: https://www.pepkio.com/

# Citation

If you use the Pepkio DNA RevComp & Primer Toolkit in your research or computational pipelines, please cite it as follows:

```bibtex
@software{pepkio_dna_revcomp_2026,
  author       = {Pepkio Bioinformatics Team},
  title        = {Pepkio DNA RevComp \& Primer Toolkit: Sequence Transformation and Primer Quality Control Framework},
  year         = {2026},
  publisher    = {Pepkio},
  url          = {https://www.pepkio.com/tools/dna-revcomp-primer-toolkit}
}
```

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.

# Keywords

- dna reverse complement calculator
- reverse complement generator
- primer reverse complement tool
- dna sequence reverse complement
- oligonucleotide complement calculator
- dna reverser tool
- rna reverse complement converter
- iupac degenerate primer calculator
- iupac reverse complement
- primer melting temperature calculator
- wallace rule tm calculator
- nearest neighbor tm calculator
- gc content calculator primer
- 3 prime gc clamp detector
- molecular weight oligonucleotide calculator
- pcr primer design toolkit
- sanger sequencing primer reverse complement
- gibson assembly overhang calculator
- rt qpcr primer reverse complement
- cDNA synthesis primer design
- antisense oligonucleotide calculator
- sirna reverse complement design
- shrna antisense strand generator
- 16s rrna degenerate primer reverse complement
- ngs index primer revcomp
- illumina adapter reverse complement
- single stranded dna molecular weight
- sequence orientation checker
- 5 prime to 3 prime orientation tool
- fasta batch reverse complement
- python dna reverse complement client
- bioinformatics primer quality control
- reverse transcriptase primer design
- site directed mutagenesis primer complement
- standard watson crick base pairing tool
- nucleic acid directionality converter
- bioinformatic oligo quality control
- ambiguous nucleotide reverse complement
- monovalent salt tm correction calculator
- pcr amplification failure prevention
- fasta sequence reverse complement tool
- batch primer complement generator
- electronic lab notebook primer verification
- python bioinformatic sequence converter
- high throughput primer verification
- reverse complement sequence generator online
- how to reverse complement a dna sequence
- how to calculate primer melting temperature nearest neighbor
- difference between reverse complement and simple complement
- why are pcr primers written 5 prime to 3 prime
- how to design reverse primer for gene amplification
- how to calculate gc content of pcr primers
- how does salt concentration affect primer tm
- how to handle iupac degenerate bases in reverse complement
- how to check primer 3 prime gc clamp
- how to calculate molecular weight of single stranded dna oligo
- how to reverse complement sanger sequencing trace primers
- how to convert rna template sequence to cdna primer
- how to generate reverse complement for multiplex pcr primers
- how to verify illumina index primer 5 prime to 3 prime direction
- how to fix spreadsheet primer orientation errors
- best tool for batch dna reverse complement calculation
- wallace rule vs nearest neighbor primer tm calculation
- how to design gibson assembly complementary overhangs
- automated fasta reverse complement python script
