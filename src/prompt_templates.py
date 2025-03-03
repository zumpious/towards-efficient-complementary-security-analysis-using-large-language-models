default_prompt_template = """
Analyze the following potential vulnerability that was found by the security scanner "SpotBugs" with the "FindSecurityBugs"-Plugin in a Java source code project.

Vulnerability identified by the security scanner and contextual information:
{context_items}

The source code included might be a false positive classification by the SAST scanner.
Do you agree with the scanner that this source code contains an actual vulnerability?

Return a number for your decision ranging from "0.0" to "10.0", where "10.0" means you absolutely agree with the scanner, "0.0" means you absolutely do not agree, and any number around "5.0" means that you are not sure.

Give your answer in the following format:
```
Decision: 0.0 - 10.0
```
"""

CoT_prompt_template = """
Analyze the following potential vulnerability that was found by the security scanner "SpotBugs" with the "FindSecurityBugs"-Plugin in a Java source code project.

Vulnerability identified by the security scanner and contextual information:
{context_items}

The source code included might be a false positive classification by the SAST scanner.
Do you agree with the scanner that this source code contains an actual vulnerability?

Return a number for your decision ranging from "0.0" to "10.0", where "10.0" means you absolutely agree with the scanner, "0.0" means you absolutely do not agree, and any number around "5.0" means that you are not sure.
Think step by step. 

Give your answer in the following format:
```
Explanation: "Let's think step by step..." 
---
Decision: 0.0 - 10.0
```

Explanation:
"""
