# SAS-Datasets

<div style="display:flex;align-items:center;justify-content:center;margin:20px;">
    <img src="https://sas.leavessoft.cn/img/logo.23b72972.svg">
</div>

## 📅 Update

- [2026/03/08]() Our work on LLM-based data augmentation for short answer scoring in low-resource scenarios has been accepted by _IEEE TKDE_.
- [2024/10/10](/ADS) Update a new dataset in the field of Computer Science.

## 📄 Description

- A collection of Chinese short answer scoring datasets.

- In this repo, we first created and released a Chinese short answer scoring dataset named **LE** dataset. Moreover, we translate the other two foreign language short answer scoring datasets into the Chinese version with Microsoft Bing Translator.

- We further translate the **STS-Benchmark (STS-B)** dataset as a text similarity to better compare the text inference performance of NLI models.

## 💾 Datasets

There are five datasets in this repo:

- **ADS Dataset.**
The dataset has 15 questions pertaining to the course of algorithms and data structures. Each question contains a distinct ID. Each item in the dataset include a compilation of student replies, together with the associated question ID and reference responses. The score of each student's response is standardized to a value ranging from zero to one. The dataset contains 1582 response phrases.

- **LE Dataset.**
The dataset consists of a question table and an answer table, where the question table contains 100 domain questions on logistics engineering. Each question has a unique ID. The answer table contains a list of student answers, with the corresponding question's ID and reference answer. The score of each student's answer is normalized to a number from zero to one. The dataset comprises 585 answer sentences.

- **ASAG Dataset.** [[1]](https://aclanthology.org/E09-1065.pdf) [[Original version]](http://infomap-nlp.sourceforge.net/)
The ASAG dataset consists of three assignments of seven questions. The question area is computer science. The dataset comprises three assignments with 630 short answers, and each assignment includes the question, teacher answer, and student answers with two annotators' average grades. Both annotators were asked to grade for correctness on an integer scale from zero to five.

- **SR Dataset.** [[2]](http://ceur-ws.org/Vol-2481/paper48.pdf) [[Original version]](https://zenodo.org/record/3257363#.XRsrn5P7TLY)
The SR dataset contains the list of sentences written by students, with a unique sentence ID, student answer, and manually defined reference answer. The question area is health informatics and the dataset comprises 331 student-reference answer sentence pairs. An answer's score ranges from zero to one.

- **STS Benchmark Dataset.** [[3]](http://ixa2.si.ehu.eus/stswiki/index.php/STSbenchmark) [[Original version]](http://ixa2.si.ehu.eus/stswiki/index.php/Main_Page)
STS Benchmark comprises a selection of the English datasets used in the STS tasks organized in the context of SemEval between 2012 and 2017. The selection of datasets includes text from image captions, news headlines, and user forums. The dataset comprises 8628 sentence pairs. Each line includes a sentence pair and an integer score scale from zero to five.

- Short Answer Scoring Datasets

| Dataset | Total | Train | Dev/Test | Topic                 |
|---------|-------|-------|----------|-----------------------|
| ADS     | 1,582  | 70%   | 30%      | Computer Science      |
| LE      | 585   | 70%   | 30%      | Logistics Engineering |
| ASAG    | 630   | 70%   | 30%      | Computer Science      |
| SR      | 331   | 70%   | 30%      | Health Informatics    |

- Chinese Translation of STS Dataset

| Dataset       | Total | Train | Dev/Test | Topic |
|---------------|-------|-------|----------|-------|
| STS-Benchmark | 8,625  | 67%   | 16%      | News  |

## Citation

```
@ARTICLE{11433809,
  author={Lai, Peichao and Zhang, Kexuan and Wang, Yilei and Cui, Bin},
  journal={IEEE Transactions on Knowledge and Data Engineering}, 
  title={Improving Low-Resource Short Answer Scoring Through Large Language Model-Based Data Augmentation}, 
  year={2026},
  volume={},
  number={},
  pages={1-14},
  keywords={Synthetic aperture sonar;Semantics;Training;Data models;Transfer learning;Data augmentation;Multilingual;Knowledge graphs;Feature extraction;Accuracy;Few-shot learning;knowledge graph-based data augmentation;semantic alignment;short answer scoring},
  doi={10.1109/TKDE.2026.3673734}}
```

```
@article{Lai2023MSimMS,
  title    = {{M-Sim}: Multi-level Semantic Inference Model for Chinese short answer scoring in low-resource scenarios},
  journal  = {Computer Speech \& Language},
  volume   = {84},
  pages    = {101575-101590},
  year     = {2024},
  issn     = {0885-2308},
  doi      = {https://doi.org/10.1016/j.csl.2023.101575},
  url      = {https://www.sciencedirect.com/science/article/pii/S0885230823000943},
  author   = {Peichao Lai and Feiyang Ye and Yanggeng Fu and Zhiwei Chen and Yingjie Wu and Yilei Wang},
  keywords = {Short answer scoring, Text similarity, Few-shot learning}
}
```

## Next

We are constructing a new, multi-feature, and sufficient Chinese short answer dataset and the dataset would be released with our next work.

Copyright (c) 2024 Creator SN®
