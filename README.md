# SAS-Datasets

<div style="display:flex;align-items:center;justify-content:center;margin:20px;">
    <img src="https://sas.leavessoft.cn/img/logo.23b72972.svg">
</div>


## Description

- A collection of Chinese short answer scoring datasets.

- In this repo, we first created and released a Chinese short answer scoring dataset named **LE** dataset. Moreover, we translate the other two foreign language short answer scoring datasets into the Chinese version with Microsoft Bing Translator.

- We further translate the **STS-Benchmark (STS-B)** dataset as a text similarity to better compare the text inference performance of NLI models.

## Datasets

There are four datasets in this repo:

- **LE Dataset.**
The dataset consists of a question table and an answer table, where the question table contains 100 domain questions on logistics engineering. Each question has a unique ID. The answer table contains a list of student answers, with the corresponding question's ID and reference answer. The score of each student's answer is normalized to a number from zero to one. The dataset comprises 585 answer sentences.

- **ASAG Dataset.** [[1]](https://aclanthology.org/E09-1065.pdf) [[Original version]](http://infomap-nlp.sourceforge.net/)
The ASAG dataset consists of three assignments of seven questions. The question area is computer science. The dataset comprises three assignments with 630 short answers, and each assignment includes the question, teacher answer, and student answers with two annotators' average grades. Both annotators were asked to grade for correctness on an integer scale from zero to five.

- **SR Dataset.** [[2]](http://ceur-ws.org/Vol-2481/paper48.pdf) [[Original version]](https://zenodo.org/record/3257363#.XRsrn5P7TLY)
The SR dataset contains the list of sentences written by students, with a unique sentence ID, student answer, and manually defined reference answer. The dataset comprises 331 student-reference answer sentence pairs. An answer's score ranges from zero to one.

- **STS Benchmark Dataset.** [[3]](http://ixa2.si.ehu.eus/stswiki/index.php/STSbenchmark) [[Original version]](http://ixa2.si.ehu.eus/stswiki/index.php/Main_Page)
STS Benchmark comprises a selection of the English datasets used in the STS tasks organized in the context of SemEval between 2012 and 2017. The selection of datasets includes text from image captions, news headlines, and user forums. The dataset comprises 8628 sentence pairs. Each line includes a sentence pair and an integer score scale from zero to five.

## Next

We are constructing a new, multi-feature, and sufficient Chinese short answer dataset and the dataset would be released with our next work.

Copyright (c) 2022 Creator SN®