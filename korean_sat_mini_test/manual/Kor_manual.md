# 2023 수능 벤치마크 하는 방법

2023년도 수능 벤치마크를 할 수 있게 실험코드를 만들었습니다! 
궁금한 모델을 Submit하기전에 얼마정도의 성능이 나오는지 파악하고 싶다면 써보세요!

## 🏁 Quick Start
0. 수능 벤치마크를 위해서 프로젝트를 git clone합니다.

```git clone https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard.git```

1. `AutoRAG`를 설치합니다.
    ```bash
    pip install AutoRAG
   ```
2. `.env`에 OpenAI API KEY를 환경 변수로 설정합니다.
3. `make_autorag_dataset.ipynb`를 실행하여 json 데이터를 AutoRAG 데이터셋으로 변경합니다.
4. `autorag_config.yaml`에서 프롬프트와 추가할 모델을 설정합니다. [설정방법](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/korean_sat_mini_test/Kor_manual.md#-how-to-replace-prompt-and-model)
5. `autorag_run.py`를 실행합니다.
    ```bash
    python ./korean_sat_mini_test/autorag_run.py --qa_data_path ./data/autorag/qa_2023.parquet --corpus_data_path ./data/autorag/corpus_2023.parquet
    ```
   - run하기 전 모델과 프롬프트를 바꾸고 싶다면 [아래 설명을 참고하세요](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/korean_sat_mini_test/Kor_manual.md#-how-to-replace-prompt-and-model)

6. `autorag_project_dir` 폴더에서 결과를 확인합니다.
7. `grading_report_card.ipynb`를 실행하여 여러분의 성적표를 확인해보세요!
   - 성적표 결과는 `data/result/` 폴더에 저장됩니다!
---


## 🤷 How to replace prompt and model?
- `korean_sat_mini_test` 폴더에서 `autorag_config.yaml`파일을 엽니다.

### [Case 1] prompt수정방법
1. `autorag_config.yaml`에서 `node_type`에 prompt_maker부분에서 `prompt`의 내용을 수정합니다.

```yaml
    - node_type: prompt_maker
      strategy:
        metrics:
          - metric_name: kice_metric
      modules:
        - module_type: fstring
          prompt:
          - |            
            Answer the given question.
            Read paragraph, and select only one answer between 5 choices.
            
            paragraph :
            {retrieved_contents}
            
            question of problem :
            {query}
            
            Answer : 3
```

### [Case 2] 모델을 바꾸고 싶을때 yaml파일 설정하는법
1. `node_type`의 `generator`부분에 `Modules`부분을 수정해야합니다. 

##### <OpenAI 모델>
- `module_type`을 `openai_llm` 설정
- `llm`에는 OpenAI 모델들을 자유롭게 설정
```yaml
- node_type: generator
  strategy:
    metrics:
      - metric_name: kice_metric
  modules:
    - module_type: openai_llm
      llm: [gpt-4o-mini, gpt-4o]
      batch: 5
```

##### <HuggingFace LLM 모델>
- `module_type`에는 `llama_index_llm`을 설정
- `llm`을 `huggingfacellm` 설정
- `model`에는 huggingface모델들을 자유롭게 설정

```yaml
- node_type: generator
  strategy:
    metrics:
      - metric_name: kice_metric
  modules:
    - module_type: llama_index_llm
      llm: huggingfacellm
      model: HumanF-MarkrAI/Gukbap-Qwen2-7B
```
HuggingFace모델 외에 yaml파일을 커스터마이징 하는방법에 대해 더 알고 싶다면 [AutoRAG 공식문서](https://docs.auto-rag.com/local_model.html)를 참고해주세요!



#### 📒 Notice
- 현재 실험에 올라와있는 프롬프트는 최소한의 프롬프트로 벤치마크에 리더보드에서 올라오는 프롬프트와는 다릅니다. 떄문에 실제 테스트할때의 벤치마크 리더보드와 성능은 다를수 있습니다.
  - 프롬프트를 수정하고 싶으시다면 yaml파일에서 프롬프트를 수정하세요!
