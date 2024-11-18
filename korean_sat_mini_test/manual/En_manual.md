# 2023 Korean SAT Benchmark Guide

I've created experimental code to help benchmark performance on the 2023 Korean SAT (Suneung) dataset! 
If you'd like to get a sense of how your model performs before submitting it, give this a try!

## 🏁 Quick Start

0. Clone this project.

```git clone https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard.git```

1. Install `AutoRAG`.
    ```bash
    pip install AutoRAG
    ```
2. Set your OpenAI API key as an environment variable in `.env`.
3. Run the `make_autorag_dataset.ipynb` notebook to convert the dataset from JSON format into the AutoRAG dataset format.
4. Configure your prompt and model settings in the `autorag_config.yaml` file. [How to configure](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/korean_sat_mini_test/Kor_manual.md#-how-to-replace-prompt-and-model)
5. Execute `autorag_run.py`:
    ```bash
    python ./korean_sat_mini_test/autorag_run.py --qa_data_path ./data/autorag/qa_2023.parquet --corpus_data_path ./data/autorag/corpus_2023.parquet
    ```
   - If you'd like to modify the prompt or model settings, [refer to the steps below](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard/blob/main/korean_sat_mini_test/Kor_manual.md#-how-to-replace-prompt-and-model).

6. Check the results in the `autorag_project_dir` folder.
7. Run `grading_report_card.ipynb` to view your results! 
   - The report card will be saved in the `data/result/` folder.

---

## 🤷 How to replace the prompt and model?
- Open the `autorag_config.yaml` file located in the `korean_sat_mini_test` folder.

### [Case 1] How to edit the prompt
1. In `autorag_config.yaml`, under the `node_type` for `prompt_maker`, modify the `prompt` field:

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

### [Case 2] How to change the model
1. To change the model, edit the `node_type` under the `generator` section in the YAML file:

##### <Using OpenAI Models>
- Set `module_type` to `openai_llm`.
- Specify your desired OpenAI models under the `llm` field.

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

##### <Using HuggingFace LLM Models>
- Set `module_type` to `llama_index_llm`.
- Set `llm` to `huggingfacellm`.
- Specify the HuggingFace model in the `model` field.

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

For more details on how to customize the YAML file or use models in addition to HuggingFace or OpenAI, refer to the [AutoRAG official documentation](https://docs.auto-rag.com/local_model.html).

#### 📒 Notice
- The current prompt used in this experiment is a minimal example, and may differ from those used on the official benchmark leaderboard. As such, the performance may vary from the actual test.
  - Feel free to adjust the prompt within the YAML file to better fit your needs!
