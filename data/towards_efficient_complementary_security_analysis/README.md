# Towars Efficient Complementary Security Analysis using Large Language Models

After our preliminary study, we utilized the identified contextual information and prompting technique to compare multiple LLM families on our test split dataset, which consists of 403 test cases across 11 vulnerability areas.

We first compared different LLMs of various sizes and architectures in a 3-shot CoT setup. The results of this experiment are provided in the [results](./results/) directory.

After identifying Qwen2.5 32B, GPT-4o, and Phi-4 as the most accurate models for our use case, we repeated our 3-shot CoT experiment using the self-consistency approach, which further improved the performance of the selected models. The provided [evaluation.ipynb](evaluation.ipynb) notebook demonstrates how to utilize our data and print the results for each model across all possible thresholds.

The following figure visualizes the results of GPT-4o, Qwen2.5 32B, and Phi-4 in the self-consistency environment across various thresholds.

![results](metrics_over_thresholds.png)
