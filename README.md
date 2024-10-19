# CodeLMSec Benchmark: Systematically Evaluating and Finding Security Vulnerabilities in Black-Box Code Language Models

This repository is the official implementation of [CodeLMSec Benchmark: Systematically Evaluating and Finding Security Vulnerabilities in Black-Box Code Language Models](https://arxiv.org/abs/2302.04012). 

## Code and Data

### Data
 - Download CodeLMSec benchmark: [**link**](https://drive.google.com/file/d/1c8aJYdwmpyB1OClK7uacAGz2LEyDw98Q/view?usp=drive_link)
 - Download CodeQL queries: [**link**](https://drive.google.com/file/d/1bm7vxDmivb9kEv8m0hTQ79CkJ2swcykq/view?usp=drive_link)

## Abstract
Large language models (LLMs) for automatic code generation have recently achieved breakthroughs in several programming tasks. Their advances in competition-level programming problems have made them an essential pillar of AI-assisted pair programming, and tools such as GitHub Copilot have emerged as part of the daily programming workflow used by millions of developers. Training data for these models is usually collected from the Internet (e.g., from open-source repositories) and is likely to contain faults and security vulnerabilities. This unsanitized training data can cause the language models to learn these vulnerabilities and propagate them during the code generation procedure. While these models have been extensively evaluated for their ability to produce functionally correct programs, there remains a lack of comprehensive investigations and benchmarks addressing the security aspects of these models.

In this work, we propose a method to systematically study the security issues of code language models to assess their susceptibility to generating vulnerable code. To this end, we introduce the first approach to automatically find generated code that contains vulnerabilities in black-box code generation models. This involves proposing a novel few-shot prompting approach. We evaluate the effectiveness of our approach by examining code language models in generating high-risk security weaknesses. Furthermore, we use our method to create a collection of diverse non-secure prompts for various vulnerability scenarios. This dataset serves as a benchmark to evaluate and compare the security weaknesses of code language models.

## Citation

  ```
@inproceedings{
debenedetti2023a,
title={CodeLMSec Benchmark: Systematically Evaluating and Finding Security Vulnerabilities in Black-Box Code Language Models},
author={Hossein Hajipour and Keno Hassler and Thorsten Holz and Lea Schönherr and Mario Fritz},
booktitle={Second IEEE Conference on Secure and Trustworthy Machine Learning},
year={2024}
}
```
