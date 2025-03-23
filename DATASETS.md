# Datasets Overview

This document provides detailed information about the datasets used in our research.

## OWASP Benchmark Dataset

The primary dataset for our research was extracted from the [OWASP Benchmark (v1.2)](https://github.com/OWASP-Benchmark/BenchmarkJava).

### Characteristics

- The benchmark contains over **2,740** test cases
- Covers **11 different vulnerability areas** (imbalanced)
- Can be directly analyzed by SAST tools

We used **SpotBugs** with the **FindSecBugs** plugin to analyze these test cases and stored the results in [spotbugs_dataset.pkl](data/owasp_benchmark/spotbugs_dataset.pkl). The SAST tool produced a total of **2,015** security findings on the benchmark dataset, from which we then extracted two datasets:

- ## **Train Split**: Approximately **80%** of all security findings

  - Originally containing 1,612 samples.
  - To later generate [few-shot examples](/src/few_shot_examples.py), we held back **55** of these samples (**5** per unique vulnerability area), resulting in our **train split** of **1,557 samples**.
  - The train split was used in both experiments of our **preliminary study**.
  - The train split, as well as the entire benchmark dataset, is imbalanced. For that reason, we perform a **weighted calculation** of performance metrics. The sample distribution of the train split is shown below:

    | Vulnerability Area         | CWE-ID | TP   | FP  | Total | TPR (%) | FPR (%) |
    | -------------------------- | ------ | ---- | --- | ----- | ------- | ------- |
    | Command Injection          | 78     | 98   | 85  | 183   | 100.00  | 100.00  |
    | Weak Cryptography          | 327    | 97   | 0   | 97    | 100.00  | 0.00    |
    | Weak Hashing               | 328    | 69   | 0   | 69    | 100.00  | 0.00    |
    | LDAP Injection             | 90     | 20   | 19  | 39    | 100.00  | 100.00  |
    | Path Traversal             | 22     | 109  | 103 | 212   | 100.00  | 100.00  |
    | Secure Cookie Flag         | 614    | 23   | 0   | 23    | 100.00  | 0.00    |
    | SQL Injection              | 89     | 223  | 170 | 393   | 100.00  | 100.00  |
    | Trust Boundary Violation   | 501    | 68   | 22  | 90    | 100.00  | 100.00  |
    | Weak Randomness            | 330    | 167  | 0   | 177   | 100.00  | 0.00    |
    | XPATH Injection            | 643    | 7    | 13  | 20    | 100.00  | 100.00  |
    | XSS (Cross-Site Scripting) | 79     | 183  | 81  | 264   | 100.00  | 100.00  |
    | **Total**                  | —      | 1064 | 493 | 1557  | —       | —       |
    | **Mean**                   | —      | —    | —   | —     | 100.00  | 63.64   |

- ## **Test Split**: Approximately **20%** of the security findings

  - The **test split** contains **403** samples, again across **11 unique vulnerability areas**.
  - Used in our **main experiment** to identify whether LLMs are capable of performing a conservative analysis.
  - Similar to the train split, the test split is also imbalanced. The distribution of samples is shown below:

    | Vulnerability Area         | CWE-ID | TP  | FP  | Total | TPR (%) | FPR (%) |
    | -------------------------- | ------ | --- | --- | ----- | ------- | ------- |
    | Command Injection          | 78     | 22  | 23  | 49    | 100.00  | 100.00  |
    | Weak Cryptography          | 327    | 28  | 0   | 28    | 100.00  | 0.00    |
    | Weak Hashing               | 328    | 15  | 0   | 15    | 100.00  | 0.00    |
    | LDAP Injection             | 90     | 4   | 6   | 10    | 100.00  | 100.00  |
    | Path Traversal             | 22     | 22  | 23  | 45    | 100.00  | 100.00  |
    | Secure Cookie Flag         | 614    | 8   | 0   | 8     | 100.00  | 0.00    |
    | SQL Injection              | 89     | 47  | 37  | 84    | 100.00  | 100.00  |
    | Trust Boundary Violation   | 501    | 13  | 10  | 23    | 100.00  | 100.00  |
    | Weak Randomness            | 330    | 46  | 0   | 46    | 100.00  | 0.00    |
    | XPATH Injection            | 643    | 5   | 4   | 9     | 100.00  | 100.00  |
    | XSS (Cross-Site Scripting) | 79     | 61  | 25  | 86    | 100.00  | 0.00    |
    | **Total Count**            |        | 275 | 128 | 403   |         |         |
    | **Mean**                   |        |     |     |       | 100.00  | 63.64   |

## Real-World Dataset: Mnestix

To demonstrate that we have developed a generalizable framework for complementary security analysis of SAST tools and LLMs, we decided to test our approach on a real-world software project. The project we selected is called **Mnestix**, which was partly open-sourced and is available [here](https://github.com/eclipse-mnestix/mnestix-browser).

### Characteristics

- Mnestix is primarily written in **C# and TypeScript**, but also includes infrastructure code such as **Dockerfiles**.
- Mnestix also imported the **Java components** from the open‐source project [BaSyx](https://github.com/eclipse-basyx), which were subsequently analyzed.

### Used SAST Tools

We selected several SAST tools for our static analysis:

- CodeQL
- Semgrep
- KICS
- Checkov
- SpotBugs with FindSecBugs plugin

### Processing & Dataset Distribution

Originally, a total of **120** findings were extracted from all SAST tool reports and combined into one dataset. Out of these **120** real-world samples, **6** were excluded from the dataset and used to generate [few-shot examples](/src/few_shot_examples.py) (3 samples for CWE-374 and 3 samples for infrastructure code). This resulted in a newly created dataset of **114 real-world security findings**. All of these findings were manually labeled by multiple security experts, forming our ground source of truth. The distribution of samples by the used SAST tool and security finding type is detailed below:

| scanner                 | type                                      | TP  | FP  | Total |
| ----------------------- | ----------------------------------------- | --- | --- | ----- |
| Checkov                 | CKV_DOCKER_2                              | 0   | 2   | 2     |
| Checkov                 | CKV_DOCKER_3                              | 0   | 2   | 2     |
| Checkov                 | CKV_SECRET_4                              | 2   | 2   | 4     |
| Checkov                 | CKV_SECRET_6                              | 4   | 3   | 7     |
| CodeQL                  | cs/log-forging                            | 34  | 1   | 35    |
| CodeQL                  | js/overly-large-range                     | 0   | 2   | 2     |
| KICS                    | IncorrectValue                            | 1   | 8   | 9     |
| KICS                    | MissingAttribute                          | 4   | 18  | 22    |
| KICS                    | RedundantAttribute                        | 4   | 4   | 8     |
| Semgrep                 | Inefficient-Regular-Expression-Complexity | 0   | 3   | 3     |
| SpotBugs w/ FindSecBugs | BC_VACUOUS_INSTANCEOF                     | 0   | 1   | 1     |
| SpotBugs w/ FindSecBugs | EI_EXPOSE_REP                             | 0   | 6   | 6     |
| SpotBugs w/ FindSecBugs | EI_EXPOSE_REP2                            | 0   | 13  | 13    |
| **Total Count**         |                                           | 49  | 65  | 114   |

The manually labeled security reports are stored in [this directory](/data/towards_efficient_complementary_security_analysis/mnestix/tool_results/). To see how to extract the results from the manually labeled `.xlsx` files and use them in a Python environment, see the corresponding experiment [notebook](/data/towards_efficient_complementary_security_analysis/evaluation.ipynb).
