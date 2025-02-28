## [QUARTZNET: DEEP AUTOMATIC SPEECH RECOGNITION WITH 1D TIME-CHANNEL SEPARABLE CONVOLUTIONS](https://arxiv.org/pdf/1910.10261)
(заголовок удалить)


## Review 4

The article I’m reviewing is called **"QuartzNet: Deep Automatic Speech Recognition with 1D Time-Channel Separable Convolutions."** It’s written by Samuel Kriman, Stanislav Beliaev, Boris Ginsburg, Jocelyn Huang, Oleksii Kuchaiev, Vitaly Lavrukhin, Ryan Leary, Jason Li, and Yang Zhang, mostly from NVIDIA, with some from the University of Illinois Urbana-Champaign, High School of Economics, and University of Saint Petersburg. It’s a research paper, but no specific journal or date is listed.

The topic is about a new way to make computers understand speech using a model called QuartzNet. It’s built with special 1D time-channel separable convolutions, which help it stay small but still work really well. The big idea is to get near top accuracy on speech tasks with fewer parts than other models, making it faster and easier to use on small devices.

The paper starts by saying old speech systems used big neural networks with over 100 million parts, which were slow and heavy. QuartzNet uses a lighter trick—splitting convolutions into two steps: one for time and one for channels. This cuts the size down to under 20 million parts. The authors tested it on LibriSpeech and Wall Street Journal (WSJ) datasets and got close to the best scores, like 3.9% error on LibriSpeech’s clean test set with a language model.

The article explains QuartzNet’s setup: it has a starting layer, then five block groups, each repeated a few times, and ends with three more layers. Each block has a depthwise convolution (for time) and a pointwise convolution (for channels), plus normalization and ReLU. The authors tried three sizes—5x5, 10x5, and 15x5—where 15x5 (15 blocks, 5 modules each) did best. On LibriSpeech, it hit 3.98% error on dev-clean and 11.58% on dev-other with just 18.9 million parts.

The authors trained it with tricks like speed perturbation and SpecCutout, using NovoGrad to adjust learning, and mixed-precision to speed things up. Training the 15x5 model took 5 days on 8 GPUs, or just 4.3 hours on 32 DGX2 nodes with a huge batch. On WSJ, a smaller 5x3 model got 4.5% error with a Transformer-XL language model, beating some bigger models like RNN-CTC (8.7%).

The paper also shows it can adapt. The authors pretrained QuartzNet-15x5 on LibriSpeech and Common Voice, then fine-tuned it on WSJ’s 80 hours. It dropped WSJ error to 2.99% with Transformer-XL, way better than starting fresh. Tables show it’s smaller and often better than rivals like Jasper or Wav2Letter++.

At the end, the authors say QuartzNet’s small size makes it great for phones or tiny gadgets. They’re working on adding attention decoders next. They shared it in NVIDIA’s NeMo toolkit, which is neat.


I find this artile topical and useful. I think that such small models can also find own usage in autonomous devices like phones or smartspeakers. It`s great that nowadays ideas go not only in a way of making models larger, but also optimizing architecture of them.  