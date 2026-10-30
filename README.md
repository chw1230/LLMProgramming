# LLM Programming

상명대학교 컴퓨터과학과 **LLM Programming** 수업의 실습(Lab)과 과제(HW) 코드 저장소입니다.
N-gram 언어 모델에서 시작해 Word2Vec, RNN, Transformer까지 언어 모델의 발전 흐름을 직접 구현하며 따라갑니다.

## 구성

| 폴더 / 파일 | 내용 | 구분 |
|---|---|---|
| `환경구축/` | VS Code + Python 가상환경, PyTorch/CUDA 동작 확인 (`check_env.py`) | Lab 1 |
| `Ngram/Ngram실습(Bigram).ipynb` | Unigram/Bigram 카운트, MLE 확률, 문장 생성, Perplexity | Lab 2 |
| `Ngram/Ngram과제(Trigram).ipynb` | Trigram 언어 모델 구현, Unigram/Bigram/Trigram Perplexity 비교, Interpolation | HW 2 |
| `Word2Vec/Word2Vec.ipynb` | Skip-gram Word2Vec 학습, 코사인 유사도, PCA 시각화 | Lab 3 |
| `Word2Vec/과제/HW3.ipynb` | window 크기 비교, 유사도 분석, 학습 문장 추가에 따른 임베딩 변화 | HW 3 |
| `gpu.ipynb` | CPU↔GPU 데이터 이동 비용, 행렬 연산 속도, VRAM, 정밀도별 메모리 | GPU 실습 |
| `Lab4RNN.ipynb` | Vanilla RNN 언어 모델 학습과 텍스트 생성 (temperature, top-k) | Lab 4 |
| `Lab4RNN_과제.ipynb` | `trace_model()`로 한 문장의 학습/생성 과정 추적 | Lab 4 과제 |
| `밑LLM/` | 『밑바닥부터 만들면서 배우는 LLM』 개인 학습 (부록 A 파이토치, 2장 텍스트 데이터) | 자기주도 학습 |

## 실행 환경

- Python 3, PyTorch, scikit-learn, matplotlib
- 노트북은 Google Colab(T4 GPU)과 로컬 VS Code 모두에서 실행
- 과제 노트북(HW2, HW3, Lab4)은 `seed=42`로 고정해 같은 결과가 재현되도록 작성
