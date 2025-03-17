# Repository Overview

This repository contains the complete experimental results and supporting materials for our research.

## Repository Structure

- **OWASP Benchmark Data & Experiment Results in JSON Format**  
  All experiment results and JSON outputs are located in the **/data** directory, which is structured as follows:

  - **[OWASP Benchmark](data/owasp_benchmark/)**  
    The primary dataset for our research was extracted from the [OWASP Benchmark](https://github.com/OWASP-Benchmark/BenchmarkJava) and is stored in [spotbugs_dataset.pkl](data/owasp_benchmark/spotbugs_dataset.pkl).  
    The OWASP Benchmark consists of over **2,740** test cases across **11 different vulnerability areas**, which can be directly analyzed by SAST tools.  
    We used **SpotBugs** with the **FindSecBugs** plugin to analyze these test cases. Based on its results, we created two distinct datasets:

    - A **train split** containing approximately **80%** of all security findings, used in our preliminary study and for generating few-shot examples.
    - A **test split** containing approximately **20%** of the security findings, later used to validate the findings of our preliminary study and to compare various LLMs to assess whether comparative security analysis is feasible using LLMs.
    - For fruther information about the used datasets see: [datasets.md](/datasets.md).

  - **[Preliminary Studies](data/preliminary_study/)**  
    Our preliminary study consists of two experiments:

    1. **[Contextual Information Analysis](data/preliminary_study/contextual_information_experiment/README.md)**  
       This experiment examines how different combinations of contextual information (from SpotBugs reports and the CWE database) impact LLM-based security assessments. We further introduce our used prompt template here. This experiment was conducted on the **train set**.
       More details: [Comparing Contextual Information](data/preliminary_study/contextual_information_experiment/README.md).

    2. **[Prompting Techniques Comparison](data/preliminary_study/prompting_techniques_experiment/README.md)**  
       This study compares Few-Shot, Chain-of-Thought (CoT), and Self-Consistency (SC) prompting techniques using **GPT-3.5 Turbo**. This experiment was conducted on the **train set**.
       More details: [Comparing Prompting Techniques](data/preliminary_study/prompting_techniques_experiment/README.md).

  - **[Main Research Findings](data/towards_efficient_complementary_security_analysis/README.md)**  
    The main results of our research, including an evaluation of various LLM families (**Qwen, GPT, Phi, and Llama**) on both:

    - The **test split** (403 security findings) of the OWASP Benchmark security findings.
    - A **real-world dataset** (114 security findings) extracted from the **Mnestix** project.

    For more information on the used datasets see: [datasets.md](/datasets.md).

    More details: [Towards Efficient Complementary Security Analysis](data/towards_efficient_complementary_security_analysis/README.md).

- **Few-Shot Examples & Prompt Templates**  
  The few-shot examples and prompt templates used for default and Chain-of-Thought prompting are provided in the **/src** directory:

  - [few_shot_examples.py](src/few_shot_examples.py)
  - [prompt_templates.py](src/prompt_templates.py)
