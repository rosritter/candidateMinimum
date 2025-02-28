## [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/pdf/2006.11477)

(удалить заголовок)

### Review3

The article I’m reviewing is called **"Wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations."** It’s written by Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, and Michael Auli, all from Facebook AI. It’s a preprint under review, so no specific journal or date has been listed yet.

The topic is about teaching computers to understand speech without needing tons of labeled examples. The authors made a model called wav2vec 2.0 that learns from raw audio by itself, then gets fine-tuned with a little labeled data to do speech recognition. The big idea is that it can work really well even with just a tiny bit of labeled speech, unlike older systems that need thousands of hours.

The paper starts by saying most speech systems need lots of transcribed audio, which is hard to get for most of the 7,000 languages in the world. Humans don’t learn that way—babies pick up language just by listening. So, the authors built wav2vec 2.0 to mimic that. It uses a convolutional network to turn raw audio into a basic form, hides parts of it, and trains a Transformer to guess what’s missing by comparing it to options. It also learns speech units on its own using a trick called Gumbel softmax.

The article explains how it works: the model has an encoder to process audio, a Transformer to understand context, and a quantizer to make discrete speech units. The authors trained it on 53,000 hours of unlabeled audio from LibriVox, then tested it with labeled data from Librispeech. With all 960 hours of labeled data, it got a super low error rate of 1.8/3.3 WER (word error rate) on clean/noisy test sets. With just one hour of labeled data, it beat the best older method using 100 times less labeled stuff. Even with only 10 minutes—48 short clips—it hit 4.8/8.2 WER, which is amazing for so little data.

The authors also tested it on TIMIT, a phoneme recognition task, and set a new record, cutting errors by 23-29% compared to past work. The paper shows tables proving bigger models and more unlabeled data make it better. For example, the LARGE model with LibriVox data dropped WER to 2.0/4.0 with 100 hours labeled, way better than older models like Noisy Student (4.2/8.6).

At the end, the authors say wav2vec 2.0 could help make speech tech for tons of languages that don’t have much data. They think switching to a seq2seq setup or word pieces might boost it more. They shared their code online too, which is cool for others to try.

I found this article exciting because it shows how computers can learn speech like humans, using way less labeled data. It’s simple but powerful, and could help people who speak rare languages get better tech. The results are clear, and it’s neat to see how it beats older ways with so little effort!