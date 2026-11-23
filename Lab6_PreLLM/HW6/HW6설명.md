**Compact Transformer language model on BeRP**

Build a word-level, decoder-only language model from scratch using the BeRP restaurant utterances. Your goal is to improve next-word prediction with as few parameters as possible. Download transcript.txt from the&nbsp;BeRP transcripts.

**Task**

1\. Implement a model with&nbsp;**2–4 causal Transformer layers**, token and position embeddings, and a vocabulary output layer. Train only on the notebook's training split. Use no pretrained model or weights. Limit the model to 2 million trainable parameters.

2\. Train with next-token cross-entropy. Use the provided data preparation and score cells unchanged; you may change architecture, optimizer, batch size, learning rate, and training duration.

**Score**

Run score(model, quick_loader) after an epoch for quick feedback (up to 256 utterances). Run score(model, val_loader) for the final validation result. The cell prints perplexity (lower is better), parameter count, and performance points (higher is better):

points = min(30, 600 / [perplexity × (max(parameters, 100000) / 1000000)^0.15])

The parameter factor rewards a smaller model with the same perplexity. For example, at perplexity 30, a 1-million-parameter model earns 20 points; a 500,000-parameter model earns about 22.2.&nbsp;

**Submit and grading**

Submit the executed notebook, model checkpoint, and a short paragraph explaining which change helped or hurt. Report the final full-validation score.&nbsp;

※ Use score_LM.ipynb for data preparation and performance check (point calculation)

