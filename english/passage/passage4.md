## [QUARTZNET: DEEP AUTOMATIC SPEECH RECOGNITION WITH 1D TIME-CHANNEL SEPARABLE CONVOLUTIONS](https://arxiv.org/pdf/1910.10261)

### Abstract
We propose a new end-to-end neural acoustic model for automatic speech recognition. The model is composed of multiple blocks with residual connections between them. Each block consists of one or more modules with 1D time-channel separable convolutional layers, batch normalization, and ReLU layers. It is trained with CTC loss. The proposed network achieves near state-of-the-art accuracy on LibriSpeech and Wall Street Journal, while having fewer parameters than all competing models. We also demonstrate that this model can be effectively fine-tuned on new datasets. 

### 1. INTRODUCTION 
In the last few years, end-to-end (E2E) neural networks (NN) have achieved new state-of-the-art (SOTA) results on many automatic speech recognition (ASR) tasks. Such models replace the traditional multi-component ASR system with a single, end-to-end trained NN which directly predicts character sequences and therefore greatly simplify training, fine-tuning and inference. The latest E2E models also have very good accuracy, but this often comes at the cost of increasingly large models with high computational and memory requirements. 

The motivation of this work is to build an ASR model that achieves SOTA-level accuracy, while utilizing significantly fewer parameters and less compute power. Smaller models offer multiple advantages: (1) they are faster to train, (2) they are more feasible to deploy on hardware with limited compute and memory, and (3) they have higher inference throughput. 

We achieve this goal by building a very deep NN with 1D time-channel separable convolutions. This new network reaches near-SOTA word error rate (WER) on LibriSpeech [1] (see Table 4) and WSJ [2] (see Table 7) datasets with fewer than 20 million parameters, compared to previous end-to-end  ASR designs which typically have over 100 million parameters. We have released the source code and pre-trained models in the NeMo toolkit [3].

### 2. RELATED WORK 
There has been a lot of work done in exploring compact network architectures and on investigating the trade-off between accuracy and size of neural networks, such as SqueezeNet [4], ShuffleNet [5], and EfficientNet [6]. Our approach is directly related to MobileNets [7, 8] and Xception [9], which uses depthwise separable convolutions [10, 11]. Each depthwise separable convolution module is made up of two parts: a depthwise convolutional layer and a pointwise convolutional layer. Depthwise convolutions apply a single filter per input channel (input depth). Pointwise convolutions are 1 × 1 convolutions, used to create a linear combination of the outputs of the depthwise layer. BatchNorm and ReLU are applied to the outputs of both layers.


## Translation

### Аннотация
Мы предлагаем новую сквозную нейроакустическую модель для автоматического распознавания речи. Модель состоит из нескольких блоков с остаточными связями между ними. Каждый блок состоит из одного или нескольких модулей с 1D конволюционными слоями, разделяемыми по временным каналам, пакетной нормализацией и слоями ReLU. Обучение проводится с потерями CTC. Предложенная сеть достигает точности, близкой к современной, на LibriSpeech и Wall Street Journal, имея при этом меньшее количество параметров, чем все конкурирующие модели. Мы также демонстрируем, что эта модель может быть эффективно настроена на новых наборах данных.

### 1 Введение
За последние несколько лет сквозные (E2E) нейронные сети (NN) достигли новых передовых результатов (SOTA) во многих задачах автоматического распознавания речи (ASR). Такие модели заменяют традиционную многокомпонентную систему ASR одной сквозной обученной НС, которая непосредственно предсказывает последовательности символов и, следовательно, значительно упрощает обучение, тонкую настройку и вывод. Новейшие модели E2E также обладают очень высокой точностью, но за это часто приходится платить все более крупными моделями с высокими требованиями к вычислительным ресурсам и памяти. 

Мотивация данной работы заключается в построении модели ASR, которая достигает точности уровня SOTA, используя при этом значительно меньшее количество параметров и вычислительных мощностей. Более компактные модели имеют множество преимуществ: (1) они быстрее обучаются, (2) их легче развернуть на оборудовании с ограниченными вычислительными ресурсами и памятью, и (3) они имеют более высокую пропускную способность. 

Мы достигли этой цели, построив очень глубокую NN с разделимыми свертками 1D по временным каналам. Эта новая сеть достигает коэффициента ошибок слов (WER), близкого к SOTA, на наборах данных LibriSpeech [1] (см. табл. 4) и WSJ [2] (см. табл. 7) с менее чем 20 миллионами параметров, по сравнению с предыдущими сквозными ASR-конструкциями, которые обычно имеют более 100 миллионов параметров. Мы выпустили исходный код и предварительно обученные модели в инструментарии NeMo [3].

### 2. СВЯЗАННАЯ РАБОТА 
Было проделано много работы по изучению компактных сетевых архитектур и исследованию компромисса между точностью и размером нейронных сетей, например SqueezeNet [4], ShuffleNet [5] и EfficientNet [6]. Наш подход напрямую связан с MobileNets [7, 8] и Xception [9], в которых используются свертки, разделяемые по глубине [10, 11]. Каждый модуль глубинной сепарабельной свертки состоит из двух частей: глубинного сверточного слоя и точечного сверточного слоя. Глубинные свертки применяют один фильтр на каждый входной канал (глубину входа). Точечные свертки - это свертки 1 × 1, используемые для создания линейной комбинации выходов слоя глубинной свертки. К выходам обоих слоев применяются BatchNorm и ReLU.