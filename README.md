# NLP Multi-Classification Support Vector Modeling for Sentiment Analysis & Segmentation using LDA: Latent Dirichlet Allocation.

## Abstract: 
A comparative analysis of top 5 grossing health/wellness apps -** Natural Laguage Processing (NLP)** and linear **Support Vector Classification** for positive and negative sentiment analysis. **Latent Dirchilet Application (LDA) clustering for deep sentiment analysis** to inform best practices and growth opportunities the world of wellness apps.

**Business Case/Problem** App reviews can equal conversion rates - higher rated apps are more attractive to reviewers. Gaining insight from these reviews can provide business intelligence for process improvements and future iterations of products.

**Methodology** Natural Language Processing used with a multinomal linear Support Vector Classification model was applied to identify positive and negative reviews with baseline values of 40% and 28% to realize 92% and 85% recall respectively and 74% accuracy. While terms used to identify positive an negative reviews like 'awesome' and 'horrible' in the classifier, they proved to be not useful to identify business insights for improvements and how best to maximize existing offerings. With these adjectives stripped from the corpus, overall model performance decreased. To identify the core feedback insight, the highest and lowest rating reviews were analyzed separately with non-informative adjectives removed. Various methodologies were used for sentiment analysis including KMeans Clustering, visualization and Latent Dirichlet Allocation or LDA were experimented with. LDA provided the greatest insights to what reviewers were talking about and details and an interactive tool can be found in the Negative Reviews section and Positive Reviews sections of the notebook.

Findings In the positive reviews(highest rated), 4 main areas were identified in order of importance: Well-Being, Information, Ease of Use, and Weight-Loss In the negative reviews(lowest rated), 3 main areas were identified in order of imporance: Technical Issyes, Billing Terms, and Ease of Use

Inline-style: 
![Topic Frequency for 5 Star Reviews](topic_frequency_5_star.png)   ![Topic Frequency for 1 Star Reviews](topic_frequency_1_star.png)

These findings would support the following recommendations for health/wellness app makers:

1) Exploit app-specific features like well-being, sleep or weight loss features.
2) Improve access to relevant information to keep users best informed.
3) Resolve technical issues, syncing / updates 
4) Be clear on billing terms
5) Maximize ease of uses for features since it was highlighted 
