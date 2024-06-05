# Replication and Extension of SAC3

## Introduction
This project replicates and extends the SAC3 method for detecting hallucinations in large language models (LLMs). SAC3 improves traditional self-consistency checks by incorporating semantically equivalent question perturbations and cross-model response consistency. Semantic-aware cross-check consistency (SAC3) is a novel sampling-based hallucination detection method that expands on the principle of self-consistency checking and incorporates additional mechanisms to detect both question-level and model-level hallucinations by leveraging advances including semantically equivalent question perturbation and cross-model response consistency checking. 

## Project Overview

### Preparation
- **Literature Review**: Thoroughly reviewed the SAC3 paper and methodology.
- **Code Setup**: Adapted the authors' code for use in Google Colab.

### Replication Work
- **Initial Testing**: Evaluated datasets on GPT-3.5-turbo for binary classification and open-domain QA tasks.
- **Method Understanding**: Explored the effects of varying the number of self-responses and perturbed questions.
- **Model Testing**: Tested SAC3 on larger models (Guanaco-33b, Falcon-7b) and expanded datasets.

### Extended Work
- **Smaller Models**: Evaluated SAC3 on models with fewer than 10 billion parameters due to hardware constraints.
- **Customization**: Modified code and prompts for different model characteristics.
- **Bootstrap Testing**: Used bootstrap sampling to achieve more reliable results across multiple models.

## Key Findings
- **Robustness**: SAC3 effectively detects hallucinations across various models.
- **Performance Variability**: High variability indicates the need for further testing with larger datasets.

## Conclusion
SAC3 shows promise in enhancing hallucination detection in LLMs. Future work should focus on optimizing computational efficiency and expanding model and data testing.

## 🤖 Installation

### Requirements

- python 3.8
- openai <= 0.28.1

### Create env and download all the packages required as follows:

```
conda create -n sac3 python=3.8
source activate sac3
pip install -r requirements.txt
```

## Instructions

### Using the Google Colab Notebook

1. Open the Google Colab website.
2. Upload your notebook file (.ipynb) to Google Colab.
3. Run the cells in the notebook sequentially to replicate and extend the SAC3 method.
4. Make sure to adjust any file paths and environment settings as needed within the notebook.

**Note:** for Gemma-7B-it, please choose A100 GPU for high RAM.

## Citation 

```
@inproceedings{zhang2023sac3,
      title={SAC^3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency},
      author={Jiaxin Zhang, Zhuohang Li, Kamalika Das, Bradley Malin, Sricharan Kumar},
      booktitle={EMNLP},
      year={2023},
      eprint={2311.01740},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
