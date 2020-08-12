# NLP Natural Language Processing Multi-Classification Support Vector Modeling for Sentiment Analysis & Segmentation using LDA: Latent Dirichlet Allocation.

## Abstract: 
A comparative analysis of top 5 grossing health/wellness apps -**Natural Laguage Processing (NLP)** and linear **Support Vector Classification** for positive and negative sentiment analysis. **Latent Dirchilet Application (LDA) clustering for deep sentiment analysis** to inform best practices and growth opportunities the world of wellness apps.

**Business Case/Problem** App reviews can equal conversion rates - higher rated apps are more attractive to reviewers. Gaining insight from these reviews can provide business intelligence for process improvements and future iterations of products.

**Methodology** Natural Language Processing used with a multinomal linear Support Vector Classification model was applied to identify positive and negative reviews with baseline values of 40% and 28% to realize 92% and 85% recall respectively and 74% accuracy. While terms used to identify positive an negative reviews like 'awesome' and 'horrible' in the classifier, they proved to be not useful to identify business insights for improvements and how best to maximize existing offerings. With these adjectives stripped from the corpus, overall model performance decreased. To identify the core feedback insight, the highest and lowest rating reviews were analyzed separately with non-informative adjectives removed. Various methodologies were used for sentiment analysis including KMeans Clustering, visualization and Latent Dirichlet Allocation or LDA were experimented with. LDA provided the greatest insights to what reviewers were talking about and details and an interactive tool can be found in the Negative Reviews section and Positive Reviews sections of the notebook.

**Findings** The top five grossig health/wellness apps in order are:

1) Calm
2) MyFitnessPal
3) Headspace
4) BetterMe(Me)
5) Fitbit

Once positive and negative sentiment was classified, cluster segment analysis was used to identify topics using Latent Dirichlet Allocation (LDA).

In the positive reviews(highest rated), 4 main areas were identified in order of importance: 
* Well-Being, Information 
* Ease of Use and 
* Weight-Loss

In the negative reviews(lowest rated), 3 main areas were identified in order of imporance: 
* Technical Issues 
* Billing Terms 
* Ease of Use

Inline-style: 
![Topic Frequency for 5 Star Reviews](topic_frequency_5_star.png)   ![Topic Frequency for 1 Star Reviews](topic_frequency_1_star.png)

These findings would support the following recommendations for health/wellness app makers:

1) Exploit app-specific features like well-being, sleep or weight loss features.
2) Improve access to relevant information to keep users best informed.
3) Resolve technical issues, syncing / updates 
4) Be clear on billing terms
5) Maximize ease of uses for features since it was highlighted 


# Background: 

<img src='yogapic.png' width=10% alignment=center>

Mobile or **mHealth** is defined by the [WHO](https://www.who.int/goe/publications/goe_mhealth_web.pdf) as the “medical and public health practice supported by mobile devices, such as mobile phones, patient monitoring devices, personal digital assistances and other wireless devices”.  

[According to Grand View Research](https://www.grandviewresearch.com/press-release/global-mhealth-app-market) The global mHealth app market is projected to register a compound annual growth rate of 44.7% by 2027 forecasted at  $236. billion USD.  Increased adoption of technology coupled with the availability of mobile applications for users is witnessing a rapid growth, especially healthcare apps that assist consumers in self-management of disease, wellness, and chronic conditions. Rapid growth in chronic diseases along with the rise in the number of app users is accountable for the mHealth apps market growth.  These apps are comprised of fitness, lifestyle management, nutrition and diet, women’s health, medication adherence, healthcare providers, and disease management. Of these, the fitness category accounted for the majority of segment share in 2018. According to Wired, a mobile advertising and analytics platform, women are more inclined toward tracking their health than men.

Reviews are important to consumers.  Nearly [95 percent of shoppers](https://spiegel.medill.northwestern.edu/online-reviews/) read online reviews before making a purchase .  In fact, one-to-one peer recommendations, original research, and product reviews are [the most influential content](https://contentmarketinginstitute.com/wp-content/uploads/2017/07/smartbrief-content-marketing-institute-how-content-influences-purchasing-process-research.pdf) in affecting purchase decisions.  Reviews can not only boost business, they can inform what is being done well, and what can be done to improve products and services.  

[App Annie](https://www.appannie.com/apps/google-play/top-chart/?country=US&category=19&device=&date=2020-04-05&feed=All&rank_sorting_type=rank&page_number=0&page_size=100&table_selections=) is a decision-making platform for the mobile app economy. App Annie combines the analytics of one's own apps with a granular understanding of the competition and market to provide a unique 360-degree view of one's mobile business.  It was used in  combination with [google play scraper](https://pypi.org/project/google-play-scraper/) to obtain the data for this project. 


> **Questions to be answered:**
* What are the top grossing health and wellness apps? 
* What's in a positive review versus a negative review?
* What insight can be gleaned from reviews to provide business intelligence for next-gen apps?


Additional reading/resources:

* https://www.itproportal.com/features/the-wellness-industry-is-a-leader-in-mobile-app-development/ 
* https://imtinnovation.com/digital-health/health-and-wellness-apps 

  ___
*Inspired by: https://www.curiousily.com/posts/create-dataset-for-sentiment-analysis-by-scraping-google-play-app-reviews-using-python/ SEVERAL copies of this same project exist in various formats by various authors.



