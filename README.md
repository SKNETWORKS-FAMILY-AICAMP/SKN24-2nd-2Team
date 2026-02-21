# 🚀 SK네트웍스 Family AI 캠프 24기 2차 프로젝트 
## 주제: 데이터분석 + 머신러닝 + 딥러닝을 활용한 가입 고객 이탈 예측 (Churn Prediction)

---

## 1. 2팀 소개 - 
- **팀명**: SKN24-2nd-2Team (Cupid Rescue)
- **멤버**:
  
| 이름 | 이미지 | GitHub |
| :--- | :--- | :--- |
| 고아라 | - | - |
| 김정현 | - | - |
| 권민제 | - | - |
| 김규호 | - | - |
| 최현진 | - | - |



## 2. 프로젝트 개요
- **프로젝트 명**: 💘 OkCupid 데이팅앱 유저 데이터를 활용한 가입 고객 이탈 예측 (Churn Prediction)
- **프로젝트 소개**: 데이팅 앱 OkCupid 유저들의 가치관과 활동 데이터를 분석하여 이탈 가능성을 예측.
- **필요성**: 
- **목표**: 이진 분류 모델을 통해 이탈 고위험군 유저를 90% 이상의 정밀도로 식별

### 데이터셋 기본 정보
- 출처: Kaggle - OkCupid Profiles
- 규모: 약 59,946건 (거의 60,000명)
- 수집 지역: 샌프란시스코 (San Francisco)
- 수집 시기: 2012년 6월
- 데이터 타입: 구조화된 프로필 정보 + 자유 텍스트 (에세이)
  
## 3. 기술 스택


## 4. WBS (Work Breakdown Structure)


## 5. 데이터 전처리 결과서 (EDA)
> (각 팀원이 분석한 주요 상관관계 시각화 이미지 삽입)


## 6. 인공지능 학습 결과서
| Model | Accuracy | F1-Score | 비고 |
|-------|----------|----------|------|


## 7. 수행결과 (시연)


## 8. 한 줄 회고

... (팀원별 작성)

---

## 📁 프로젝트 폴더 구조
---

📁 SKN24-2ND-2Team/
├── 📁 data/
│   ├── raw/              ← Kaggle 원본 데이터 CSV (gitignore 처리)
│   └── processed/        ← 전처리 완료데이터 CSV (gitignore 처리)
│
├── 📁 docs/
│   ├── 기획서.md          ← 프로젝트 기획 문서
│   ├── EDA_결과.md        ← 데이터 분석 정리
│   └── 회의록/            ← 팀 회의 기록
│
├── 📁 models/
│   ├── saved/            ← 학습된 모델 파일 (gitignore 처리)
│   └── results/          ← 모델별 성능 비교 결과 CSV나 이미지
│
├── 📁 notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_ML_models.ipynb
│   └── 04_DL_models.ipynb
│
├── 📁 src/
│   ├── preprocess.py     ← 전처리 함수 모듈
│   ├── train.py          ← 학습 실행 스크립트
│   ├── evaluate.py       ← 평가 지표 함수
│   └── predict.py        ← 예측 실행 스크립트
│
├── .gitignore
├── README.md
└── requirements.txt
