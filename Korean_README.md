![image](https://github.com/user-attachments/assets/013fead4-495b-4cd8-9019-f64fe8447a22)

# 🏆 수능 국어 LLM 리더보드

--------------

## 🗂️ Index

- [💯 리더보드 순위](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#-%EB%A6%AC%EB%8D%94%EB%B3%B4%EB%93%9C-%EC%88%9C%EC%9C%84)
- [🎯 수능 국어 LLM Leaderboard란?](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#-%EC%88%98%EB%8A%A5-%EA%B5%AD%EC%96%B4-llm-leaderboard%EB%9E%80)
- [🥇 Submit 방식](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#-submit-%EB%B0%A9%EC%8B%9D)
- [🪑 About benchmark Datadataset](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#-benchmark-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B)
- [♾️ Metric](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#%EF%B8%8F-metric)
- [📗 참고해볼만한 Reference](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#%EF%B8%8F-metric)
- [📰 Notice](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#-notice)
- [📬 문의하기](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/Korean_README.md#-%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0)

### [2023 수능 샘플 데이터셋 모델 테스트 하는 방법](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/korean_sat_mini_test/manual/Kor_manual.md)

------------
수능 국어 LLM 벤치마크 리더보드로 Human performance와 LLM의 Performance를 비교해보세요!

여러분이 개발한 한국어 LLM 파인튜닝 모델이 인간의 performance를 넘어 새로운 역사를 쓸 준비가 되었습니까? 지금 바로 벤치마크에서 모델의 한계를 시험하고, 수능 국어에서 SOTA(State Of The
Art) 자리를 차지하세요!👑

### 🚨 Notice. 25 수능 (1개년) 모델 성능 비교 결과
현재는 GPT 모델을 기반으로 벤치마크를 완료한 상태이며, 향후 추가 자원과 예산이 확보되면 다른 모델들의 성능 평가도 진행할 예정입니다.
등급컷은 현재 추정 등급컷이므로 확정 등급컷이 나온다면 업데이트할 예정입니다.

|  순위   |      모델명      | 원점수 | 추정 등급컷(2025.11.18기준) |
|:-----:|:-------------:|:---:|:--------------------:|
| 🥇1st |  o1-Preview   | 97  |         1등급          |
| 🥈2nd |    o1-mini    | 78  |         4등급          |
| 🥉3rd |    gpt-4o     | 75  |         4등급          |
|  4th  |  gpt-4o-mini  | 59  |         5등급          |
|  5th  | gpt-3.5-turbo | 16  |         8등급          |


---

## 💯 리더보드 순위

| Leaderboard Rank |             Model Name             | Submitter Name | Avg. std Score | Avg. Grade | 2024 SAT | 2023 SAT | 2022 SAT | 2021 SAT | 2020 SAT | 2019 SAT | 2018 SAT | 2017 SAT | 2016 SAT | 2015 SAT | URL                                                                                                                                    |
|:----------------:|:----------------------------------:|:--------------:|:--------------:|:----------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:---------------------------------------------------------------------------------------------------------------------------------------|
|    🥇 **1st**    |         gpt-4o-2024-08-06          |     OpenAI     |     114.9      |    3.6     |  65 (4)  |  81 (4)  |  70 (4)  |  69 (4)  |  76 (4)  |  74 (3)  |  77 (4)  |  86 (2)  |  84 (3)  |  77 (4)  | [Link](https://openai.com/)                                                                                                            |
|    🥈 **2nd**    | Meta-Llama-3.1-405B-Instruct-Turbo |   meta-llama   |     113.8      |    3.8     |  77 (3)  |  87 (3)  |  69 (4)  |  70 (4)  |  65 (5)  |  68 (4)  |  78 (4)  |  80 (3)  |  87 (3)  |  68 (5)  | [Link](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct)                                                                      |
|    🥉 **3rd**    |     Qwen2.5-72B-Instruct-Turbo     |      Qwen      |     105.8      |    4.6     |  61 (5)  |  78 (4)  |  52 (6)  |  60 (5)  |  60 (5)  |  64 (4)  |  74 (4)  |  70 (5)  |  74 (4)  |  79 (4)  | [Link](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)                                                                               |
|       4th        | Meta-Llama-3.1-70B-Instruct-Turbo  |   meta-llama   |     103.7      |    4.8     |  50 (6)  |  72 (5)  |  73 (3)  |  61 (5)  |  79 (3)  |  51 (5)  |  58 (6)  |  66 (5)  |  71 (5)  |  70 (5)  | [Link](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct)                                                                       |
|       5th        |         Qwen2-72B-Instruct         |      Qwen      |       98       |    5.2     |  53 (5)  |  57 (6)  |  59 (5)  |  45 (6)  |  57 (5)  |  56 (5)  |  76 (4)  |  69 (5)  |  58 (6)  |  63 (5)  | [Link](https://huggingface.co/Qwen)                                                                                                    |
|       6th        |       gpt-4o-mini-2024-07-18       |     OpenAI     |      93.9      |    5.6     |  57 (5)  |  53 (6)  |  50 (6)  |  55 (5)  |  50 (6)  |  46 (6)  |  62 (5)  |  58 (6)  |  64 (5)  |  57 (6)  | [Link](https://openai.com/)                                                                                                            |
|       7th        |           gemma-2-27b-it           |     Google     |       91       |    5.9     |  51 (6)  |  54 (6)  |  51 (6)  |  51 (6)  |  50 (6)  |  37 (7)  |  50 (6)  |  71 (4)  |  54 (6)  |  56 (6)  | [Link](https://huggingface.co/google/gemma-2-27b-it)                                                                                   |
|       8th        |           solar-mini-ja            |    Upstage     |      85.9      |    6.2     |  46 (6)  |  58 (6)  |  43 (6)  |  41 (7)  |  46 (6)  |  51 (5)  |  49 (6)  |  48 (7)  |  40 (7)  |  52 (6)  | [Link](https://ko.upstage.ai/feed/company/event-recap-exploring-japan-ai-scene-with-upstage-solar-mini-ja)                             |
|       9th        |             solar-mini             |    Upstage     |      85.5      |    6.4     |  33 (7)  |  57 (6)  |  48 (6)  |  42 (7)  |  46 (6)  |  50 (6)  |  43 (7)  |  55 (6)  |  42 (7)  |  56 (6)  | [Link](https://www.upstage.ai/feed/product/solarmini-performance-report)                                                               |
|       10th       |    Mixtral-8x22B-Instruct-v0.1     |   MistralAI    |      83.4      |    6.6     |  40 (7)  |  44 (7)  |  47 (6)  |  31 (8)  |  38 (7)  |  35 (7)  |  65 (5)  |  57 (6)  |  50 (6)  |  44 (7)  | [Link](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1)                                                                   |
|       11th       |          WizardLM-2-8x22B          |   Microsoft    |      83.3      |    6.6     |  37 (7)  |  56 (6)  |  47 (6)  |  30 (8)  |  52 (6)  |  29 (8)  |  51 (6)  |  47 (7)  |  51 (6)  |  53 (6)  | [Link](https://www.microsoft.com/en-us/research/publication/wizardlm-empowering-large-language-models-to-follow-complex-instructions/) |
|       12th       |     Qwen2.5-7B-Instruct-Turbo      |      Qwen      |      80.3      |    6.8     |  40 (7)  |  40 (7)  |  39 (7)  |  35 (7)  |  35 (7)  |  35 (7)  |  58 (6)  |  53 (6)  |  44 (7)  |  42 (7)  | [Link](https://huggingface.co/Qwen/Qwen2.5-72B)                                                                                        |
|       13th       |  Meta-Llama-3.1-8B-Instruct-Turbo  |   meta-llama   |      74.7      |    7.1     |  46 (6)  |  31 (8)  |  36 (7)  |  34 (7)  |  36 (7)  |  24 (8)  |  38 (7)  |  38 (7)  |  37 (7)  |  45 (7)  | [Link](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)                                                                        |
|       14th       |         gpt-3.5-turbo-0125         |     OpenAI     |      68.7      |    7.7     |  29 (8)  |  39 (7)  |  26 (8)  |  17 (9)  |  36 (7)  |  24 (8)  |  38 (7)  |  25 (8)  |  45 (7)  |  27 (8)  | [Link](https://openai.com/)                                                                                                            |
|       15th       |     Mixtral-8x7B-Instruct-v0.1     |   MistralAI    |      63.4      |    8.3     |  19 (9)  |  25 (8)  |  40 (7)  |  20 (9)  |  27 (8)  |  19 (9)  |  37 (7)  |  16 (9)  |  30 (8)  |  19 (9)  | [Link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)                                                                    |
|       16th       |           gemma-2-9b-it            |     Google     |      61.2      |    8.4     |  24 (8)  |  20 (9)  |  16 (9)  |  22 (9)  |  17 (9)  |  29 (8)  |  24 (8)  |  25 (8)  |  25 (8)  |  29 (8)  | [Link](https://huggingface.co/google/gemma-2-9b-it)                                                                                    |
|       17th       |    Llama-3.2-3B-Instruct-Turbo     |   meta-llama   |      60.6      |    8.7     |  28 (8)  |  18 (9)  |  27 (8)  |  23 (9)  |  16 (9)  |  17 (9)  |  21 (9)  |  29 (8)  |  22 (9)  |  23 (9)  | [Link](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)                                                                        |
|       18th       |      Mistral-7B-Instruct-v0.3      |   MistralAI    |      57.2      |    8.9     |  17 (9)  |  11 (9)  |  22 (9)  |  12 (9)  |  18 (9)  |  21 (9)  |  19 (9)  |  27 (8)  |  23 (9)  |  21 (9)  | [Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)                                                                      |

- **Rank 기준**: 10개년 수능 표준점수들의 평균  <표준점수를 통해서 각 년도별 시험의 난이도를 점수에서 반영합니다.>
- **Avg. std Score:** 표준점수 평균
- **Avg. Grade:** 등급 평균
- **년도별 수능 점수 표기**: 원점수(등급)

[점수에 대한 설명 바로가기](https://github.com/minsing-jin/KO-SAT_Slayer_Champions_League/blob/main/Korean_README.md#%EF%B8%8F-metric)

i.e)

- GPU 자원 Donation해주신다면 평가에 큰 도움이 될 것 같습니다. 감사합니다!
- 적극적인 피드백 환영합니다! 언제든 말씀해주세요!

### 📗 Notes. 24 수능 (1개년) 모델 성능 비교 결과

- **o1-preview**: 88점 (1등급, 상위 4%)
- **o1-mini** : 60점 (5등급)

**i.e)** gpt o1 모델은 o1 정식버전이 출시할때 벤치마크 업데이트 예정입니다!

---

## 🎯 수능 국어 LLM Leaderboard란?

수능 국어 LLM Leaderboard는 한국교육과정평가원(KICE)이 개발한 대학수학능력시험(수능) 국어 과목의 10개년 시험문제를 기반으로 한 벤치마크 리더보드입니다.

매년 엄선된 수능 국어 시험 문제를 통해 여러분의 대형 언어 모델(LLM)의 성능을 평가할 수 있습니다. 평가 방식은 실제 수능과 동일하게 표준점수와 등급 체계를 사용하여, Human performance와 LLM의
performance을 직접 비교할 수 있도록 구성되어 있습니다.

## ⭐️ 수능 국어 LLM Leaderboard Project의 목적
1. Human performance와 LLM performance를 비교할수 있는 벤치마크 정보공유
2. 한국어 언어능력을 평가하는 한국의 가장 공신력 있는 KICE 평가원의 엄선된 벤치마크 데이터셋
3. 해마다 업데이트 되는 새로운 수능국어 벤치마크 데이터셋으로 데이터 리키지 방지
4. 특정 국가나 기업에 종속되지 않은 오픈소스 LLM이 한국 수능 1등급에 도달시키는것

## 🏅 Submit 방식

- 리더보드 공개를 원하지 않고, private하게 모델의 성능을 알고 싶다면 하고 싶은 말 파트에 남겨주세요!
- ⭐️ 수능 문제를 풀기 위한 모델의 context length는 최소 8K 이상이어야합니다!

1. **모델 submission**:
    - **[설문 Form으로 제출](https://moaform.com/q/QP0AV0)**: 설문 응답에 맞춰 작성해주세요!
        - 링크: https://moaform.com/q/QP0AV0
    - **이메일로 제출**: huggingFace에 게시된 자신의 finetuning 모델의 Url과 닉네임을 전송해주세요!
        - 제출 메일: developerminsing@gmail.com
    - **issue로 제출**: Github의 이슈에서 자신의 finetuning 모델의 Url과 닉네임을 게시해주세요!
    ```markdown
   <이메일 제출, 이슈 제출시 Form example>
    제출자 이름: 감스트
    HuggingFace 제출 URL: https://huggingface.co/감스트모델짜스
    하고 싶은말: 열심히 하시잖아
    ```

2. **리더보드 확인**: github와 huggingFace에서 자신의 순위를 확인할 수 있습니다.
3. **순위 상승 도전**: 자신의 순위를 올려 **Slayer Champion** 타이틀을 획득하세요.

**Notice:** 모델 제출후 가용한 GPU 리소스와, 제출량에 따라 1~3주일의 시간이 소요될 수 있습니다.

## 🪑 Benchmark 데이터셋

- 본 대회에서는 2015년부터 2024년까지의 10개년 수능 국어 문제를 사용합니다.
- 2022년도부터 시행된 선택과목에 대해서는 화법과 작문 과목 선택과목으로 하여 benchmark를 진행합니다.
- Benchmark 데이터셋의 주요 평가 목록은 언어 이해력, 핵심 내용 파악 능력, 논리적 사고력, 비판적 사고력, 창의적 사고력, 멀티미디어 해석력을 평가합니다.
  <출처: 2024 KICE 수능 국어 평가 목록>

## 📑 Benchmark 데이터셋 Category

### (1) 📚 독서

출제 내용: 인문, 사회, 과학, 기술, 예술 등 다양한 분야의 지문이 출제됩니다.

- **인문 지문**: 철학, 논증, 역사 등을 다룹니다.
- **사회 지문**: 경제, 정치, 법, 문화 등을 다룹니다.
- **과학 지문**: 물리, 화학, 생물, 지구과학 등 과학 관련 내용이 출제됩니다.
- **기술 지문**: 컴퓨터, 기계, 실생활 과학 등이 출제됩니다.
- **예술 지문**: 미술, 음악, 건축, 영화 등 다양한 예술 주제가 포함됩니다.
- **융합 지문**: 다양한 분야를 결합한 복합적인 장문 지문도 자주 출제됩니다.

- **평가 내용**: 다양한 도메인의 이해력 평가, 추론 및 비판적 사고 능력 평가

### (2) 🧑‍🎤 문학

- **출제 내용**: 고전 소설, 현대 소설, 고전 시가, 현대 시, 고전수필 등 다양한 문학 갈래를 다룹니다.

- **평가 내용**: 정서 및 문체 이해력 평가, 다양한 시대와 장르 이해 평가

### (3) 🗣️ 화법과 작문

- 대화와 글쓰기를 다룬 문제 등이 출제됨.

- **평가 내용**: 대화 맥락 이해력 평가, 작문 능력 평가

## ♾️ Metric

### 평가 방식

- 대회에서는 각 모델이 제시된 문제에 대해 제출한 답안이 실제 정답과 일치하는지 여부를 측정하는 방식입니다.
- 평가 점수는 각 년도의 문제별로 채점되며, 최종적으로는 표준점수의 평균을 통해 순위가 매겨집니다.

### 리더보드 점수 설명

- **원점수란?**: 시험에서 100점만점으로 받은 점수
- **표준점수**: 응시생이 받은 원점수가 평균에서 얼마나 떨어져 있는지 일종의 '평균과의 거리'를 측정하는 점수
- **등급**: 표준점수에 근거해 수험생을 나눈 것으로, 총 9등급이 있다. 국어와 수학, 탐구영역에서는 영역과목별 전체 수험생의 상위 4%가 1등급, 그다음 7%(누적 11%)까지가 2등급, 그다음 12%(누적
  23%)까지가 3등급이 된다.
  [EBSI 참고](https://www.ebsi.co.kr/ebs/ent/enta/retrieveEntNewsView.ebs?bbsCd=B011&datNo=142017)

## 📗 참고해볼만한 Reference

- [Nomadamas 실험기록](https://github.com/NomaDamas/KICE_slayer_AI_Korean?tab=readme-ov-file#5-%ED%98%95%EC%8B%9D-%EC%A7%80%EC%A0%95-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8)

## 📰 Notice

- 저작권 문제가 있을수 있어 수능 벤치마크 데이터셋은 공개하지 않을 예정입니다. 평가 데이터는 15수능 ~ 24수능이며 22년도~24년도 선태과목은 화법과 작문에 대해서만 평가합니다.
- 평가의 공정성을 위해서 프롬프트는 공개하지 않습니다!
- 추후 수능 당일 제출해주신 모델들을 전부 반영할 국영수사과 모두 리더보드에서 업데이트 예정입니다.
- 본 수능 벤치마크 시스템은 [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG)를 사용했습니다!
  (AutoRAG is an automatic RAG optimization tool that can also be used for LLM performance comparison and prompt
  engineering.)
- 22년도 선택과목이 시행된 이래로 산출된 표준점수 공식은 [Crux 컨설팅](https://orbi.kr/profile/974081)의 [Crux table](https://suneungcalc.com/)을 활용했습니다.

## 📬 문의하기

- 궁금한 점이나 오류, 지원이 필요하다면 언제든지 연락해 주세요:

- 이메일: developerminsing@gmail.com

**다음 KO-SAT Slayer Champion**이 될 준비가 되셨나요? 💪

## License

- 본 데이터셋의 출처는 [한국교육과정평가원 (KICE)](https://www.kice.re.kr/main.do?s=kice)에 있습니다.

-------
This benchmark leaderboard is a non-profit project that aims to provide information on LLM performance with SAT
benchmarks! 
