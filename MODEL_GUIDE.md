# Supervised-Learning Model Guide

Use this as a reference, not as a checklist of algorithms to try. Begin with a baseline and add complexity only when validation evidence supports it.

| Family | Main idea | Scaling? | Main caution |
|---|---|---:|---|
| Mean or majority baseline | Measure what is achievable without useful feature learning | No | Every serious model should beat it on a task-appropriate metric |
| Linear regression | Fit a weighted sum for a continuous target | Usually no | Misses nonlinear structure; correlated inputs complicate coefficient interpretation |
| Ridge and Lasso | Penalise coefficient size | Yes | Select penalty strength using validation data |
| Logistic regression | Rank or classify outcomes with a linear boundary | Usually yes | Raw features do not automatically represent interactions |
| Decision tree | Learn threshold-based rules | No | Deep trees can memorise noise |
| Random forest | Average many varied trees | No | Less interpretable; probability estimates may need calibration |
| Gradient boosting | Add trees sequentially to correct earlier errors | No | More tuning and easier to overfit through repeated experimentation |
| k-nearest neighbours | Predict from nearby training observations | Yes | Sensitive to scale, irrelevant features, and high dimension |
| Support vector machine | Find a wide separating margin | Yes | Kernel and hyperparameter choices matter |
| Naïve Bayes | Combine class-conditional feature likelihoods | Usually no | Conditional independence is often unrealistic for process sensors |
| Multi-layer perceptron | Learn nonlinear feature transformations | Yes | Optimisation, architecture, and random initialisation affect training |

## A practical selection sequence

1. Define the target and the decision the prediction will support.
2. Establish a simple baseline.
3. Fit an interpretable linear or logistic model.
4. Inspect validation errors and residuals for missing structure.
5. Try trees or ensembles when thresholds and interactions matter.
6. Select the model and operating threshold before opening the final test set.
7. Report limitations, monitoring needs, and the conditions under which the model should not be used.

Probability estimation and action selection are separate steps. A model supplies a score or estimated probability; an operating threshold converts that output into a decision with real costs and constraints.
