## [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
(Заголовок удалить)

### Review 2

The article I’m reviewing is called **"Language Models are Unsupervised Multitask Learners."** It’s written by Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever, all from OpenAI in San Francisco. The paper doesn’t have a specific journal or date listed, but it’s about a cool new idea in language tech.

The main topic is how language models can learn to do lots of tasks—like answering questions or translating—without being taught each one step-by-step. They trained a model called GPT-2 on a big pile of webpages called WebText, and it started figuring things out on its own. The key idea is that if you make a model big enough and give it tons of text, it can do tasks without extra training, which they call "zero-shot" learning.

The article starts by saying most language systems need specific training for each job, like question answering or summarizing. But these systems mess up if things change a bit. The authors think training on one task at a time is why they’re not flexible. So, they made GPT-2, a huge model with 1.5 billion parts, and fed it WebText—millions of webpages scraped from Reddit links. They wanted it to learn from real, messy text, not just clean datasets.

The paper explains that GPT-2 can do stuff like read and answer questions or summarize articles without being told how. They tested it on things like the CoQA dataset, where it scored 55 F1—pretty good compared to systems trained with over 127,000 examples. It also set new records on 7 out of 8 language tasks, like LAMBADA, where it dropped perplexity (a measure of confusion) from 99.8 to 8.6. Bigger models worked better, and the biggest, GPT-2, even wrote paragraphs that made sense.

The authors go into how it works: GPT-2 uses a Transformer setup, like another famous model, but tweaked a bit. It reads text as bytes, not words, so it can handle anything, and they used a trick called Byte Pair Encoding to mix word and character smarts. They trained four sizes of models, from 117 million to 1.5 billion parts, and all got better with more size, though they still think it could learn more from WebText.

The article also checks if GPT-2 just memorized stuff. They found some overlap with training data—like 1-6% on test sets—but it didn’t cheat much. It even made up new text instead of copying, like when it wrote about unicorns speaking English in the Andes. They tested translation too, like English to French, and got 5 BLEU—not great, but neat for no training.

At the end, the authors say this could lead to systems that learn tasks naturally, like humans do, without tons of labeled data. They’re excited to keep pushing it further.


I think it is great step in long way of neural nerwork development. Because costs of createing datasets significantly lowers. That allows researches teach bigger models.