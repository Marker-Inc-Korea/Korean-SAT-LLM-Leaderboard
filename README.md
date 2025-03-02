![image](https://github.com/user-attachments/assets/ff0b3721-8ba0-4938-a38b-ca5636d0a3ae)

# 🏆 Korean SAT LLM Leaderboard

-------

## 📊 Test Your Own Model on the 2023 Korean SAT Sample Dataset

[Learn How to Test Your Model](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/korean_sat_mini_test/manual/En_manual.md)

--------

## 🗂️ Index

- [🎯 What is the Korean SAT LLM Leaderboard?](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-what-is-the-korean-sat-llm-leaderboard)
- [💯 Leaderboard](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-leaderboard)
- [🏅 Submission Guidelines](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-submission-guidelines)
- [🪑 About benchmark Datadataset](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-benchmark-dataset)
- [♾️ Metric](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#%EF%B8%8F-metric)
- [📗 Helpful Reference](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-helpful-reference)
- [🤷 More About CSAT(Korean college entrance exam)](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-more-about-csatkorean-college-entrance-exam)
- [📰 Notice](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-notice)
- [📬 Contact Us](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/README.md#-contact-us)

### [한국어 설명 바로가기](https://github.com/minsing-jin/KO-SAT_Slayer_Champions_League/blob/main/Korean_README.md)

------
Take advantage of this unique opportunity to compare human academic ability with the performance of large language
models (LLMs) based on the highly reputable College Scholastic Ability Test (CSAT)!

Test how well your fine-tuned Korean LLM performs on a 10-year benchmark of the Korean CSAT and see what score it would
achieve right now!

cf) To prevent data leakage, this benchmark only includes models released before each year's CSAT (Suneung) on the
leaderboard.

### 🚨 Notice: 2025 SAT (1-Year) Model Performance Comparison Results

The current benchmark has been completed using GPT-based models. Future performance evaluations for other models will be
conducted as additional resources and funding become available.  
Please note that the current grade thresholds are **estimated**, and they will be updated once the official thresholds
are announced.

|  Rank  |         Model Name         | Standard Score | Raw Score | Common Subject Score | Elective Subject Score | Estimated Grade Cut ([CruxTable Standard](https://suneungcalc.com/)) |
|:------:|:--------------------------:|:--------------:|:---------:|:--------------------:|:----------------------:|:--------------------------------------------------------------------:|
| 🥇 1st |         o1-Preview         |      133       |    97     |          73          |           24           |                               Grade 1                                |
| 🥈 2nd |          o1-mini           |      115       |    78     |          57          |           21           |                               Grade 4                                |
| 🥉3rd  |           gpt-4o           |      112       |    75     |          56          |           19           |                               Grade 4                                |
|  4th   | claude-3-5-sonnet-20241022 |      108       |    70     |          54          |           16           |                               Grade 4                                |
|  5th   |        HyperClovaX         |      108       |    61     |          48          |           24           |                               Grade 4                                |
|  6th   |        gpt-4o-mini         |       97       |    59     |          44          |           15           |                               Grade 5                                |
|  7th   |   claude-3-opus-20240229   |       91       |    53     |          35          |           18           |                               Grade 6                                |
|  8th   | claude-3-5-haiku-20241022  |       90       |    52     |          37          |           15           |                               Grade 6                                |
|  9th   |       gpt-3.5-turbo        |       56       |    16     |          10          |           6            |                               Grade 9                                |

cf)

The incorrectly answered question on the o1-preview was question 8 (3 points) from the CSAT Korean section, a
non-literary text question!  
For those curious about the analysis of the incorrect question and a detailed explanation of the experiment, please
refer
to [this link](https://velog.io/@minsing-jin/o1-preview-2025-%EC%88%98%EB%8A%A5-%EA%B5%AD%EC%96%B4-97%EC%A0%90-%EB%8B%AC%EC%84%B1).

- To prevent data leakage issues, models released after the CSAT (Suneung) are recorded separately as references rather
  than being officially listed on the leaderboard.

|            Model Name            | Standard Score | Raw Score | Common Subject Score | Elective Subject Score | Estimated Grade Cutoff ([CruxTable Standard](https://suneungcalc.com/)) |  
|:--------------------------------:|:--------------:|:---------:|:--------------------:|:----------------------:|:-----------------------------------------------------------------------:|  
|    gpt-4.5-preview-2025-02-27    |      124       |    86     |          68          |           18           |                                   3등급                                   |
|           deepseek r1            |      116       |    78     |          65          |           13           |                                 Grade 4                                 |
| gemini_2.0_experimental_advanced |      114       |    77     |          55          |           22           |                                 Grade 4                                 |

## 🎯 What is the Korean SAT LLM Leaderboard?

The Korean SAT LLM leaderboard is a leaderboard benchmarking 10 years of Korean CSAT (College Scholastic Ability Test)
exams, developed by the reputable KICE (Korea Institute for Curriculum and Evaluation).  
The CSAT consists of a wide range of question types depending on the difficulty level, designed to assess reading
comprehension, critical thinking, and sentence interpretation skills.

If you want to know more about Korean SAT (Korean College entrance exam), please
refer [this](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard?tab=readme-ov-file#-benchmark-dataset)!

## 💯 Leaderboard

| Leaderboard Rank |             Model Name             | Submitter Name | Avg. std Score | Avg. Grade | 2024 SAT | 2023 SAT | 2022 SAT | 2021 SAT | 2020 SAT | 2019 SAT | 2018 SAT | 2017 SAT | 2016 SAT | 2015 SAT | URL                                                                                                                                    |
|:----------------:|:----------------------------------:|:--------------:|:--------------:|:----------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:---------------------------------------------------------------------------------------------------------------------------------------|
|    🥇 **1st**    |         gpt-4o-2024-08-06          |     OpenAI     |     114.9      |    3.6     |  65 (4)  |  81 (4)  |  70 (4)  |  69 (4)  |  76 (4)  |  74 (3)  |  77 (4)  |  86 (2)  |  84 (3)  |  77 (4)  | [Link](https://openai.com/)                                                                                                            |
|    🥈 **2nd**    | Meta-Llama-3.1-405B-Instruct-Turbo |   meta-llama   |     113.8      |    3.8     |  77 (3)  |  87 (3)  |  69 (4)  |  70 (4)  |  65 (5)  |  68 (4)  |  78 (4)  |  80 (3)  |  87 (3)  |  68 (5)  | [Link](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct)                                                                      |
|    🥉 **3rd**    |     Qwen2.5-72B-Instruct-Turbo     |      Qwen      |     105.8      |    4.6     |  61 (5)  |  78 (4)  |  52 (6)  |  60 (5)  |  60 (5)  |  64 (4)  |  74 (4)  |  70 (5)  |  74 (4)  |  79 (4)  | [Link](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)                                                                               |
|       4th        | Meta-Llama-3.1-70B-Instruct-Turbo  |   meta-llama   |     103.7      |    4.8     |  50 (6)  |  72 (5)  |  73 (3)  |  61 (5)  |  79 (3)  |  51 (5)  |  58 (6)  |  66 (5)  |  71 (5)  |  70 (5)  | [Link](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct)                                                                       |
|       5th        |     claude-3-5-sonnet-20241022     |    Antropic    |     102.6      |     5      |  60 (5)  |  61 (6)  |  69 (4)  |  58 (5)  |  72 (4)  |  63 (4)  |  71 (5)  |  70 (5)  |  58 (6)  |  55 (6)  | [Link](https://www.anthropic.com/news/claude-3-5-sonnet)                                                                               |
|       6th        |         Qwen2-72B-Instruct         |      Qwen      |       98       |    5.2     |  53 (5)  |  57 (6)  |  59 (5)  |  45 (6)  |  57 (5)  |  56 (5)  |  76 (4)  |  69 (5)  |  58 (6)  |  63 (5)  | [Link](https://huggingface.co/Qwen)                                                                                                    |
|       7th        |       gpt-4o-mini-2024-07-18       |     OpenAI     |      93.9      |    5.6     |  57 (5)  |  53 (6)  |  50 (6)  |  55 (5)  |  50 (6)  |  46 (6)  |  62 (5)  |  58 (6)  |  64 (5)  |  57 (6)  | [Link](https://openai.com/)                                                                                                            |
|       8th        |       claude-3-opus-20240229       |    Antropic    |      91.9      |    5.7     |  46 (6)  |  44 (7)  |  62 (5)  |  49 (6)  |  56 (5)  |  51 (5)  |  69 (5)  |  52 (6)  |  53 (6)  |  49 (6)  | [Link](https://www.anthropic.com/news/claude-3-5-sonnet)                                                                               |
|       9th        |           gemma-2-27b-it           |     Google     |       91       |    5.9     |  51 (6)  |  54 (6)  |  51 (6)  |  51 (6)  |  50 (6)  |  37 (7)  |  50 (6)  |  71 (4)  |  54 (6)  |  56 (6)  | [Link](https://huggingface.co/google/gemma-2-27b-it)                                                                                   |
|       10th       |           solar-mini-ja            |    Upstage     |      85.9      |    6.2     |  46 (6)  |  58 (6)  |  43 (6)  |  41 (7)  |  46 (6)  |  51 (5)  |  49 (6)  |  48 (7)  |  40 (7)  |  52 (6)  | [Link](https://ko.upstage.ai/feed/company/event-recap-exploring-japan-ai-scene-with-upstage-solar-mini-ja)                             |
|       11th       |             solar-mini             |    Upstage     |      85.5      |    6.4     |  33 (7)  |  57 (6)  |  48 (6)  |  42 (7)  |  46 (6)  |  50 (6)  |  43 (7)  |  55 (6)  |  42 (7)  |  56 (6)  | [Link](https://www.upstage.ai/feed/product/solarmini-performance-report)                                                               |
|       12th       |    Mixtral-8x22B-Instruct-v0.1     |   MistralAI    |      83.4      |    6.6     |  40 (7)  |  44 (7)  |  47 (6)  |  31 (8)  |  38 (7)  |  35 (7)  |  65 (5)  |  57 (6)  |  50 (6)  |  44 (7)  | [Link](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1)                                                                   |
|       13th       |          WizardLM-2-8x22B          |   Microsoft    |      83.3      |    6.6     |  37 (7)  |  56 (6)  |  47 (6)  |  30 (8)  |  52 (6)  |  29 (8)  |  51 (6)  |  47 (7)  |  51 (6)  |  53 (6)  | [Link](https://www.microsoft.com/en-us/research/publication/wizardlm-empowering-large-language-models-to-follow-complex-instructions/) |
|       14th       |     Qwen2.5-7B-Instruct-Turbo      |      Qwen      |      80.3      |    6.8     |  40 (7)  |  40 (7)  |  39 (7)  |  35 (7)  |  35 (7)  |  35 (7)  |  58 (6)  |  53 (6)  |  44 (7)  |  42 (7)  | [Link](https://huggingface.co/Qwen/Qwen2.5-72B)                                                                                        |
|       15th       |     claude-3-5-haiku-20241022      |    Antropic    |       80       |    6.8     |  45 (6)  |  41 (7)  |  34 (7)  |  23 (9)  |  38 (7)  |  37 (7)  |  39 (7)  |  63 (5)  |  43 (7)  |  53 (6)  | [Link](https://www.anthropic.com/news/claude-3-5-sonnet)                                                                               |
|       16th       |  Meta-Llama-3.1-8B-Instruct-Turbo  |   meta-llama   |      74.7      |    7.1     |  46 (6)  |  31 (8)  |  36 (7)  |  34 (7)  |  36 (7)  |  24 (8)  |  38 (7)  |  38 (7)  |  37 (7)  |  45 (7)  | [Link](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)                                                                        |
|       17th       |         gpt-3.5-turbo-0125         |     OpenAI     |      68.7      |    7.7     |  29 (8)  |  39 (7)  |  26 (8)  |  17 (9)  |  36 (7)  |  24 (8)  |  38 (7)  |  25 (8)  |  45 (7)  |  27 (8)  | [Link](https://openai.com/)                                                                                                            |
|       18th       |     Mixtral-8x7B-Instruct-v0.1     |   MistralAI    |      63.4      |    8.3     |  19 (9)  |  25 (8)  |  40 (7)  |  20 (9)  |  27 (8)  |  19 (9)  |  37 (7)  |  16 (9)  |  30 (8)  |  19 (9)  | [Link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)                                                                    |
|       19th       |           gemma-2-9b-it            |     Google     |      61.2      |    8.4     |  24 (8)  |  20 (9)  |  16 (9)  |  22 (9)  |  17 (9)  |  29 (8)  |  24 (8)  |  25 (8)  |  25 (8)  |  29 (8)  | [Link](https://huggingface.co/google/gemma-2-9b-it)                                                                                    |
|       20th       |    Llama-3.2-3B-Instruct-Turbo     |   meta-llama   |      60.6      |    8.7     |  28 (8)  |  18 (9)  |  27 (8)  |  23 (9)  |  16 (9)  |  17 (9)  |  21 (9)  |  29 (8)  |  22 (9)  |  23 (9)  | [Link](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)                                                                        |
|       21th       |      Mistral-7B-Instruct-v0.3      |   MistralAI    |      57.2      |    8.9     |  17 (9)  |  11 (9)  |  22 (9)  |  12 (9)  |  18 (9)  |  21 (9)  |  19 (9)  |  27 (8)  |  23 (9)  |  21 (9)  | [Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)                                                                      |

- **Ranking Criteria**: Average of the standard scores over 10 years of CSAT <The standard scores reflect the difficulty
  level of each year's exam in the overall score.>
- **Avg. Std Score:** The average of standard scores calculated using the KICE (Korea Institute for Curriculum and
  Evaluation) method.
- **Avg. Grade:** Average grade
- **CSAT Scores by Year**: Raw score (grade)

Here’s the English translation:

[Click here for details on the scoring system](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/tree/main?tab=readme-ov-file#%EF%B8%8F-metric)

i.e.)

- Donating GPU resources would be greatly appreciated and would help with the evaluations. Thank you!
- Welcome any and all feedback! Feel free to share your thoughts anytime!

### 📗 Notes: Performance comparison of models on the 2024 CSAT (1-year)

- **o1-preview**: 88 points (Grade 1, Top 4%)
- **o1-mini**: 60 points (Grade 5)

i.e) The gpt o1 model is scheduled for a benchmark update when the official version of o1 is released!

---

## ⭐️ Purpose of the Korean SAT LLM Leaderboard Project

1. **Sharing Benchmark Data**: Provide benchmarks that allow for the comparison of human performance and LLM
   performance.
2. **Reliable Evaluation Dataset**: Utilize the highly authoritative benchmark dataset curated by KICE (Korea Institute
   for Curriculum and Evaluation) to assess Korean language proficiency.
3. **Annual Updates with Leakage Prevention**: Update the CSAT Korean benchmark dataset annually to prevent data
   leakage.
4. **Open-Source LLM Advancement**: Enable open-source LLMs, independent of any specific country or company, to achieve
   top-tier (1st-grade) performance on the Korean CSAT.

## 🏅 Submission Guidelines

- If you prefer to keep your model’s performance private and not appear on the public leaderboard, feel free to leave a
  note in the "Comments" section.
- ⭐️ Your model must have a **minimum context length of 8K tokens** to solve the Korean SAT questions!

1. **Model Submission**:
    - **[Submit via the Form](https://moaform.com/q/X6xfGE)**: Fill in the survey form to submit your model!
        - Link: https://moaform.com/q/X6xfGE
    - **Email Submission**: Send the Hugging Face URL of your fine-tuned model along with your nickname.
        - Submission email: developerminsing@gmail.com
    - **Submit via GitHub Issue**: Post your model’s Hugging Face URL and nickname in a GitHub issue.
    ```markdown
    <Example for email or GitHub issue submission>
    Submitter Name: Elon musk
    Hugging Face Submission URL: https://huggingface.co/Elon_model
    Comments: Let's go Mars!
    ```

2. **Check the Leaderboard**: View your rank on GitHub or Hugging Face.
3. **Climb the Ranks**: Improve your score and claim the **Slayer Champion** title!

**Notice:** Evaluation may take 1-3 weeks depending on available GPU resources and submission volume.

## 🪑 Benchmark Dataset

- This competition utilizes CSAT Korean questions from the 10-year period between 2015 and 2024.
- For the elective subjects introduced in 2022, **Speech and Composition** will be used as the elective subject for
  benchmarking.
- The key evaluation metrics for the benchmark dataset include: **Language Comprehension**, **Core Content Understanding
  **, **Logical Reasoning**, **Critical Thinking**, **Creative Thinking**, and **Multimedia Interpretation Skills**.
  <Source: 2024 KICE CSAT Korean Evaluation Criteria>
- The comprehension of LLMs can be assessed by examining their performance on problems from various fields such as
  humanities, social sciences, science, technology, and the arts.

## 📑 Category of Benchmark Dataset

### (1) 📚 Reading Comprehension

Content: Passages are drawn from a wide range of fields, including humanities, social sciences, science, technology, and
the arts.

- **Humanities passages**: Cover topics such as philosophy, argumentation, and history.
- **Social sciences passages**: Focus on subjects like economics, politics, law, and culture.
- **Science passages**: Include content related to physics, chemistry, biology, and earth sciences.
- **Technology passages**: Feature topics like computers, machinery, and everyday science.
- **Arts passages**: Encompass a variety of artistic themes, including visual arts, music, architecture, and film.
- **Integrated passages**: Complex, long passages that combine multiple fields are also frequently included.

- **Evaluation focus**: Assessment of understanding across diverse domains, evaluation of reasoning and critical
  thinking skills.

### (2) 🧑‍🎤 Literature

Content: Covers a variety of literary genres such as classical and modern novels, classical and modern poetry, and
classical essays.

- **Evaluation focus**: Assessment of emotional and stylistic comprehension, evaluation of understanding of various
  literary periods and genres.

### (3) 🗣️ Speech and Writing

Content: Includes problems dealing with dialogue and writing.

- **Evaluation focus**: Assessment of understanding in conversational contexts and evaluation of writing skills.

## ♾️ Metric

### Evaluation Method

- In this competition, the answers submitted by each model are evaluated based on whether they match the actual correct
  answers.
- Scores are graded for each year's questions, and the final ranking is determined by the **average of the standardized
  scores**.

### Explanation of Leaderboard Score

- **Raw Score**: The score achieved out of a maximum of 100 points on the test.
- **Standardized Score**: A score that measures how far the test taker's raw score deviates from the average.
- **Grade**: Based on standardized scores, test takers are classified into 9 grades. For the Korean, Math, and Inquiry
  subjects, the top 4% of all test takers receive a grade of 1, the next 7% (cumulative 11%) receive a grade of 2, and
  the next 12% (cumulative 23%) receive a grade of 3.
  [Refer to EBSI](https://www.ebsi.co.kr/ebs/ent/enta/retrieveEntNewsView.ebs?bbsCd=B011&datNo=142017)

## 📗 Helpful Reference

- [Nomadamas Experimental Records](https://github.com/NomaDamas/KICE_slayer_AI_Korean?tab=readme-ov-file#5-%ED%98%95%EC%8B%9D-%EC%A7%80%EC%A0%95-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8)

## 🤷 More About CSAT(Korean college entrance exam)

The Korean CSAT (College Scholastic Ability Test) Korean Language section is a university entrance exam,
with questions meticulously selected by renowned scholars from KICE (Korea Institute for Curriculum and Evaluation),
who are confined to a hotel for this process. It is one of the most reputable exams in Korea. Evaluating the performance
of LLMs (Large Language Models) based on the metrics used to assess test-takers provides an excellent opportunity to
compare human proficiency with the language capabilities of LLMs.

## 📰 Notice

- Due to copyright concerns, the CSAT benchmark dataset will not be made publicly available. The evaluation data spans
  from the **2015 CSAT to the 2024 CSAT**, and elective subjects for the years 2022 to 2024 will be limited to **Speech
  and Composition**.
- To ensure fairness, the prompts will not be disclosed.
- In the future, the leaderboard will be updated to reflect models submitted for all subjects, including Korean,
  English, Math, Science, and Social Studies, on the day of the CSAT.
- This Korean-SAT benchmarking system powered by [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG). AutoRAG is
  awesome!!
  (AutoRAG is an automatic RAG optimization tool that can also be used for LLM performance comparison and prompt
  engineering.)
  Since the implementation of elective subjects in 2022, the standard score formula has been derived using
  the [Crux Table](https://suneungcalc.com/) provided by [Crux Consulting](https://orbi.kr/profile/974081).

## 📬 Contact Us

- For questions, errors, or support, feel free to reach out:

- Email: developerminsing@gmail.com

Are you ready to become the next **KO-SAT Slayer Champion**? 💪

## License

- This dataset is sourced from
  the [Korea Institute for Curriculum Evaluation (KICE)](https://www.kice.re.kr/main.do?s=kice).

---------
This benchmark leaderboard is a non-profit project that aims to provide information on LLM performance with SAT
benchmarks! 
