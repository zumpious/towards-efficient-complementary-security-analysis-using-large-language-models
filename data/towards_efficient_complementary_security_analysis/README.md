# Towars Efficient Complementary Security Analysis using Large Language Models

After our preliminary study, we utilized the identified contextual information and prompting technique to compare multiple LLM families on our test split dataset, which consists of 403 test cases across 11 vulnerability areas.

We first compared different LLMs of various sizes and architectures in a 3-shot CoT setup. The results of this experiment are provided in the [results](./results/) directory.

After identifying Qwen2.5 32B, GPT-4o, and Phi-4 as the most accurate models for our use case, we repeated our 3-shot CoT experiment using the self-consistency approach, which further improved the performance of the selected models. The provided [evaluation.ipynb](evaluation.ipynb) notebook demonstrates how to utilize our data and print the results for each model across all possible thresholds.

The following figure visualizes the results of GPT-4o, Qwen2.5 32B, and Phi-4 in the self-consistency environment across various thresholds.

![results](self_consistency_metrics_over_thresholds.png)

The provided [evaluation.ipynb](evaluation.ipynb) notebook presents the SC results of GPT-4o, Qwen2.5 32B, and Phi-4 on a real-world dataset. This dataset was created by applying a variety of SAST tools to Mnestix, an open-source project developed by XITASO GmbH. The security findings from each SAST tool were manually labeled by security experts. Based on their manual labeling, we extracted an additional dataset consisting of 114 security findings, including 65 FPs and 49 TPs, as well as additional few-shot examples (e.g. for infrastructure related SAST tools).
