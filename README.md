# anonymized_ieee_paper

This paper provides owasp benchmark data and all JSON of our experiments.

All our experiment results are placed in the /data directory.

## todos:

1. describe the data directory
2. describe the few-shot examples strucutre and explain what of them were used for default and cot prompting
3. The provided "seed" parameter was used to split our spotbugs dataset in a 80/20 manner using sklearn train_test_split() method. We decided to use 80% of the dataset, our train split, to perform our prelimary experiments and create the few-shot examples. The test split was then used to compare the different LLMs. IMPORTANT: State the the few-shot examples were removed from every experiment to make the experiment results comparable
