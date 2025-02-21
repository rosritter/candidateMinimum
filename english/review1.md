## [Attention Is All You Need](https://arxiv.org/pdf/1706.03762)

### Review1

The article I’m reviewing is called "Attention Is All You Need." It was written by a group of researchers: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Most of them worked at Google Brain or Google Research, while Aidan did some of his work at the University of Toronto. This paper was presented at a big conference called the 31st Conference on Neural Information Processing Systems (NIPS) in 2017, held in Long Beach, California.

The article is about a new model called the "Transformer" that translates languages like English to German or French. Unlike older models that used slow recurrent neural networks (RNNs) or convolutional neural networks (CNNs) to process words one by one, the Transformer uses "attention" to look at all words at once. This makes it faster and better at handling long sentences.

The key point is that the Transformer relies only on attention, not old methods, to connect words, even if they’re far apart. The researchers tested it on English-to-German and English-to-French translations. It scored 28.4 BLEU for German (beating others by over 2 points) and 41.8 BLEU for French (a new record), training in just 3.5 days on eight GPUs—much quicker than older models.

The paper explains that RNNs were slow because they worked step-by-step. The Transformer’s "self-attention" checks all words together, and "multi-head attention" looks at sentences in different ways for better results. It has an encoder to code the input and a decoder to make the output, using six layers each and positional encodings (sine and cosine waves) to track word order.

The Transformer is fast, connecting all words in one step, unlike RNNs or CNNs. It also did well on English parsing (sentence structure) with little tweaking. They trained it on 4.5 million sentence pairs for German and 36 million for French, using eight GPUs. The big model took 3.5 days, the small one 12 hours, with tricks like dropout and the Adam optimizer.

The paper ends by saying the Transformer could change translation and work for images or audio too. They shared their code online for others to use.

I found this article really interesting because it shows how smart ideas can make computers better at understanding and translating languages. It’s amazing how fast and accurate the Transformer is compared to older ways. It’s not just about translation—it could help with lots of other tasks in the future. The simple explanations and clear results made it fun to read, even if some parts with math were a bit tricky. I think it’s an important paper for anyone curious about how machines learn to handle languages.