---
title: "Openai Releases GPT-3, the Largest Model So Far" 
date: 2020-06-05 
draft: false 
---

Story source:

https://analyticsindiamag.com/open-ai-gpt-3-language-model/


> _OpenAI researchers_[ _released a
> paper_](https://arxiv.org/pdf/2005.14165.pdf) _describing the development of
> GPT-3, a state-of-the-art language model made up of 175 billion parameters._

The previous [OpenAI](https://analyticsindiamag.com/models-large-compression-
pruning-quantization-nlp/) GPT model had 1.5 billion parameters and was the
biggest model back then, which was soon eclipsed by NVIDIA’s Megatron, with 8
billion parameters followed by Microsoft’s Turing NLG that had 17 billion
parameters. Now, OpenAI turns the tables by releasing a model that is 10x
larger than Turing NLG.

Current NLP systems still largely struggle to learn from a few examples. With
GPT-3, the researchers show that scaling up language models greatly improves
task-agnostic, few-shot performance, sometimes even reaching competitiveness
with prior state-of-the-art fine-tuning approaches.

Natural language processing tasks range from generating news articles to
language translation and answering standardised test questions.

* * *

[![](https://www.analyticsindiamag.com/wp-content/uploads/2019/05/ALabs-
banner.gif)](https://www.analytixlabs.co.in/)

* * *

The researchers trained 8 different sizes of model ranging from 125 million
parameters to 175 billion parameters, with the last being GPT-3.

### How GPT-3 Pipped Other Models

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

For GPT-3, the OpenAI team used the same model and architecture as GPT-2 that
includes modified initialisation, pre-normalisation, and reversible
tokenisation along with alternating dense and locally banded sparse attention
patterns in the layers of the transformer.

* * *

[ ![W3Schools](https://mk0analyticsindf35n9.kinstacdn.com/wp-
content/uploads/2020/04/700X80-1.gif) ](https://www.jigsawacademy.com/online-
analytics-
training/?query=online&utm_source=AIM&utm_medium=in_article_banner&utm_campaign=low_arpu)

* * *

The researchers state that larger models make increasingly efficient use of
in-context information. As can be seen in the plot above, the steeper “in-
context learning curves” for large models show improved ability to learn from
contextual information.

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

For training, the researchers have used a combination of model parallelism
within each matrix multiply and model parallelism.

GPT-3 was trained on [V100 GPU’s](https://news.developer.nvidia.com/openai-
presents-gpt-3-a-175-billion-parameters-language-model/) on the part of a
high-bandwidth cluster provided by Microsoft.

Evaluation of GPT-3 is done under 3 conditions:

  1. few-shot learning
  2. one-shot learning
  3. zero-shot learning

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

GPT-3 achieved promising results in the zero-shot and one-shot settings, and
in the few-shot setting, occasionally surpassed state-of-the-art models.

The results show that GPT-3 showed strong performance with translation,
question-answering, and cloze tasks, as well as with unscrambling words and
performing 3-digit arithmetic. The researchers claim that GPT-3 can even
generate news articles which human evaluators have difficulty distinguishing
from articles written by humans.

GPT-3 is an incredibly large model, and one cannot expect to build something
like this without fancy computational resources. However, the researchers
assure that these models can be efficient once trained, where even a full
GPT-3 model generating 100 pages of content from a trained model can cost only
a few cents in energy costs.

### Where Can This Go Wrong

> _“GPT-3 has the potential to advance both the beneficial and harmful
> applications of language models.”_
>
> OpenAI researchers

In an unprecedented approach, the researchers go in detail about the harmful
effects of GPT-3 in their paper. The high-quality text generating capability
of GPT-3 can make it difficult to distinguish synthetic text from the human-
written text, so the authors warn that there can be a misuse of language
models. They admit that malicious uses of language models can be difficult to
anticipate because language models can be repurposed in a very different
environment or for a different purpose than what the researchers intended.

They list the following misuses:

  * Spam & phishing 
  * Fraudulent academic essay writing 
  * Abuse of legal and governmental processes and
  * social engineering pretexting

Since GPT-3 scraped almost everything on the internet and every word written,
the researchers had an opportunity to identify how the racial sentiments and
other sentiments play out in conversations. For example, with the religion of
Islam, they have found that words such as violent, terrorism and terrorist co-
occurred at a greater rate than with other religions.

Despite many limitations and weaknesses, the researchers conclude that very
large language models may be an important ingredient in the development of
adaptable, general language systems.

Read the full paper [here](https://arxiv.org/pdf/2005.14165.pdf).

### Provide your comments below

comments

[![](https://mk0analyticsindf35n9.kinstacdn.com/wp-
content/uploads/2020/03/telegram.png)](https://t.me/joinchat/NJLxnhZB7GkX3CPvjs9QGQ)

