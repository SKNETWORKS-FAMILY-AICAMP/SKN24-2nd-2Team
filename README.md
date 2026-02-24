# 🚀 SK네트웍스 Family AI 캠프 24기 2차 프로젝트 

## 주제: 💘 OkCupid 데이팅앱 유저 데이터를 활용한 가입 고객 이탈 예측 (Churn Prediction)



---

## 1. 2팀 소개 
- **팀명**: 천생연분 (churn 生緣分)
- **팀원**:
 <table>
  <colgroup>
    <col style="width: 100%;">
    <col style="width: 100%;">
    <col style="width: 100%;">
    <col style="width: 100%;">
    <col style="width: 100%;">
  </colgroup>
  <tbody>
    <tr>
      <td style="text-align: center;"><img src="./assets/images/team/ara.png" alt="고아라" width="120"></td>
      <td style="text-align: center;"><img src="./assets/images/team/minje.png" alt="권민제" width="120"></td>
      <td style="text-align: center;"><img src="./assets/images/team/kyuho.png" alt="김규호" width="120"></td>
      <td style="text-align: center;"><img src="./assets/images/team/kjh.png" alt="김정현" width="120"></td>
      <td style="text-align: center;"><img src="./assets/images/team/hyunjin.png" alt="최현진" width="120"></td>
    </tr>
    <tr style="font-weight: bold;">
      <td style="text-align: center;">고아라</td>
      <td style="text-align: center;">권민제</td>
      <td style="text-align: center;">김규호</td>
      <td style="text-align: center;">김정현</td>
      <td style="text-align: center;">최현진</td>
    </tr>
    <tr>
      <td style="text-align: center;">
        <a href="https://github.com/Akoh-0909">
          <img src="https://img.shields.io/badge/AKOH--0909-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/min3802">
          <img src="https://img.shields.io/badge/min3802-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/kyu5KIm">
          <img src="https://img.shields.io/badge/kyu5KIm-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/Jeich-16">
          <img src="https://img.shields.io/badge/Jeich--16-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/lifeisgoodlg">
          <img src="https://img.shields.io/badge/lifeisgoodlg-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
        </a>
      </td>
    </tr>
  </tbody>
</table>

---


## 2. 프로젝트 개요

### 프로젝트 명: 
> 💘 OkCupid 데이팅앱 유저 데이터를 활용한 가입 고객 이탈 예측 (Churn Prediction)

### 프로젝트 소개
> OkCupid는 미국의 온라인 데이팅 플랫폼으로, 본 프로젝트에서 활용한 데이터셋은 **북캘리포니아 지역 한정의 과거 공개 데이터**임. OkCupid는 현재 서비스가 사실상 종료된 상태이며, 데이터 역시 행동 로그 없이 **프로필 정보만으로 구성**된 제한적인 데이터셋임.

이러한 한계에도 불구하고, 본 프로젝트는 해당 데이터를 활용해 **고객 이탈 예측 파이프라인을 직접 설계·구현**하고, ML 모델의 성능을 비교 분석하는 것을 목표로 함. 개발된 파이프라인은 데이팅앱을 포함한 **구독형 서비스 전반의 이탈 예측에 적용 가능한 범용 프레임워크**로 확장될 수 있음.

### 프로젝트 필요성 (배경)

### 📊 데이팅앱 시장 10년 트렌드 (2015–2024)

![글로벌 데이팅앱 시장 트렌드](./data/img/market_trend_chart.png)

> **차트 읽는 법 (각 지표별 원본 데이터 출처 명시)**
> - ① **시장 규모** ($1.69B → $9.65B, 5.7배 성장) — 원본: [Business of Apps, Dating App Revenue and Usage Statistics (2026)](https://www.businessofapps.com/data/dating-app-market/)
> - ② **글로벌 이용자 수** (꾸준히 증가) — 원본: [Statista / Priori Data, Tinder Statistics (2024)](https://prioridata.com/data/tinder-statistics/)
> - ③ **리텐션율 연도별 추이** (Day-1/7/30 매년 하락) — 원본: [Adjust, Valentine's Day App Trends Report (2025)](https://www.adjust.com/blog/valentines-day-app-trends-2025/)
> - ④ **앱별 30일 리텐션** (Bumble 11%, Tinder 7.8%) — 원본: [Similarweb, Hinge vs Bumble Dating App Retention (2023)](https://www.similarweb.com/blog/insights/hinge-bumble-dating-retention/)
> - ⑤ **Tinder 유료 구독자 연도별** (2022년 고점 10.8M 이후 역성장) — 원본: [DemandSage, Tinder Statistics (2026)](https://www.demandsage.com/tinder-statistics/)

> ⚠️ **차트 작성 방법**: 위 5개 원본 출처에서 수집한 수치를 바탕으로 본 프로젝트에서 직접 시각화한 그래프이며, 원본 이미지를 그대로 사용한 것이 아님.

| 차트 항목 | 수치 | 원본 출처 | 링크 |
|---|---|---|---|
| 전 세계 시장 규모 (2015~2024) | $1.69B → $9.65B | Business of Apps (2026) | [바로가기](https://www.businessofapps.com/data/dating-app-market/) |
| 글로벌 이용자 수 | 연도별 추이 | Statista / Priori Data (2024) | [바로가기](https://prioridata.com/data/tinder-statistics/) |
| Day-1/7/30 리텐션율 | 연도별 하락 추이 | Adjust Valentine's Day Report (2025) | [바로가기](https://www.adjust.com/blog/valentines-day-app-trends-2025/) |
| 앱별 30일 리텐션 비교 | Bumble 11%, Tinder 7.8% | Similarweb (2023) | [바로가기](https://www.similarweb.com/blog/insights/hinge-bumble-dating-retention/) |
| Tinder 유료 구독자 수 | 2022년 고점 10.8M 이후 역성장 | DemandSage (2026) | [바로가기](https://www.demandsage.com/tinder-statistics/) |

--- 

#### 📱 데이팅앱 시장의 성장

> 데이팅앱 시장은 전 세계적으로 빠르게 성장하고 있음.

| 지표 | 수치 | 출처 |
|---|---|---|
| 전 세계 데이팅앱 시장 규모 (2024) | **$81억** → 2027년 $87억 전망 | Statista (아시아경제, 2024.05.23 인용) |
| 국내 데이팅앱 시장 규모 (2024) | **$3,507만** → 2028년 $3,642만 전망 | Statista (아시아경제, 2024.05.23 인용) |
| 국내 데이팅앱 소비자 지출 (2023) | **약 1,614억원** ($1.2억) | data.ai, 2024 모바일 현황 보고서 (아시아경제, 2024.03.13 인용) |
| 국내 로맨스 스캠 피해액 (2023) | **55억 1,200만원** — 2020년 대비 15배 급증 | 아시아경제, 2024.05.23 |


![데이팅앱 시장 현황 — 뉴스 데이터 기반](./assets/background_charts_v3 (1).png)


> 📰 **뉴스 출처**  
> - 아시아경제, *커지는 데이팅 앱 시장…로맨스 스캠 주의보* (2024.05.23) — https://www.asiae.co.kr/article/2024052215114422592  
> - 아시아경제, *연애는 하고 싶지만, 돈 쓰긴 싫어…고민에 빠진 데이팅 앱* (2024.03.13) — https://www.asiae.co.kr/article/2024031310245014777

---

#### 📉 데이팅앱 산업의 위기 — 이탈과 수익화 실패

시장은 성장하지만, 동시에 심각한 구조적 문제를 안고 있음.

| 지표 | 수치 | 출처 |
|---|---|---|
| 글로벌 데이팅앱 주요 기업 시총 손실 | 매치그룹 **$400억**, 범블 **$180억** 증발 (2021년 이후 3년간) | 아시아경제, 2024.05.28 (FT 인용) |
| 미국 데이팅앱 지출 증가율 | 2022년 1월 **23.4%** → 2024년 1월 **6.2%** 로 급격 둔화 | 아시아경제, 2024.03.13 (data.ai 인용) |
| 성비 불균형 (영국 18~34세) | 남성 이용률 **47%** vs 여성 **25%** — 여성 이탈이 핵심 문제 | 아시아경제, 2024.05.28 (Mintel 인용) |

> 📰 **뉴스 출처**  
> - 아시아경제, *데이팅앱, 남자만 쓴다…"여성 이용자 유치 어려워"* (2024.05.28) — https://www.asiae.co.kr/article/2024052820301656222


---

#### 📚 참고 문헌

| # | 매체 | 제목 | 성격 | 링크 |
|---|---|---|---|---|
| 1 | 아시아경제 (2024.05.23) | 커지는 데이팅 앱 시장…로맨스 스캠 주의보 | 📰 뉴스 — Statista 시장 규모·로맨스 스캠 통계 인용 | [바로가기](https://www.asiae.co.kr/article/2024052215114422592) |
| 2 | 아시아경제 (2024.03.13) | 연애는 하고 싶지만, 돈 쓰긴 싫어…고민에 빠진 데이팅 앱 | 📰 뉴스 — data.ai 미국 지출 증가율 둔화 통계 인용 | [바로가기](https://www.asiae.co.kr/article/2024031310245014777) |
| 3 | 아시아경제 (2024.05.28) | 데이팅앱, 남자만 쓴다…"여성 이용자 유치 어려워" | 📰 뉴스 — FT·Mintel 성비 불균형·시총 손실 인용 | [바로가기](https://www.asiae.co.kr/article/2024052820301656222) |
| 4 | openads (2024.02.05) | 자만추? 앱만추! 얼마를 써야 사랑을 찾을 수 있나요? | 📊 마케팅 인사이트 — 국내 데이팅앱 시장·소비자 지출 분석 (data.ai 인용) | [바로가기](https://www.openads.co.kr/content/contentDetail?contsId=12476) |
| 5 | 고대신문 (2024.06.03) | 틀린 만남은 없다, 문화로 자리 잡은 데이팅 앱 | 📰 대학신문 — 국내 2030 이용 현황·진정성 인식 설문 | [바로가기](https://www.kunews.ac.kr/news/articleView.html?idxno=42496) |




### **프로젝트 목표**: 이진 분류 모델을 통해 이탈 고위험군 유저를 식별

1. OkCupid 프로필 데이터를 분석하여 이탈 관련 패턴을 탐색.
2. ML(LR/DT/RF/XGB/LGBM/CatBoost)을 학습·비교.
3. 클래스 불균형 환경에서 **Recall 최대화**를 핵심 지표로 모델 개선.
4. 본 파이프라인을 다른 구독형 서비스에 적용 가능한 형태로 구축.

> **📌 Recall을 핵심 지표로 선택한 이유**
> 이탈 예측의 비즈니스 목적은 **이탈 가능성이 있는 유저를 사전에 최대한 많이 포착**하여 선제적으로 개입(프로모션, 알림 등)하는 것임.
> - **False Negative(실제 이탈자를 잔류로 잘못 예측)의 비용 > False Positive(잔류자를 이탈로 잘못 예측)의 비용**
> - 이탈자를 놓치면 고객을 완전히 잃지만, 잔류자에게 잘못 개입하는 비용(예: 불필요한 쿠폰 발송)은 상대적으로 낮음
> - 따라서 **Precision을 일부 희생하더라도 Recall을 높이는 방향**이 이탈 예측 비즈니스에 적합
> - 단, Recall만 높이면 모든 유저를 이탈로 예측해도 높은 수치가 나오므로, **ROC-AUC와 F1을 보조 지표로 함께 활용**하여 모델의 실질적 판별력 검증

### 데이터셋 기본 정보

<div>
  <img src="./data/img/df_info.png" width="40%">
</div>

- 출처: - [OkCupid Profiles](https://github.com/rudeboybert/JSE_OkCupid)
- 규모: 약 59,946건 (거의 60,000명)
- 컬럼 개수: 31개
- 수집 지역: 샌프란시스코 (San Francisco)
- 수집 시기: 2012년 6월
- 데이터 타입: 
  - int64 → 2개 (age, income)
  - float64 → 1개 (height)
  - object → 28개 (대부분 범주형/텍스트)

범주형 데이터 비중이 높은 프로필 설문 기반 데이터셋

### 데이터 선택
| 컬럼명       | 사용 여부 | 설명            | 데이터타입 |
|--------------|-----------|-----------------|------------|
| age          | ✅        | 사용자 나이     | int64      |
| status       | ✅        | 연애 상태       | object     |
| sex          | ✅        | 성별            | object     |
| orientation  | ✅        | 성적 지향       | object     |
| body_type    | ✅        | 체형            | object     |
| diet         | ✅        | 식단 성향       | object     |
| drinks       | ✅        | 음주 빈도       | object     |
| drugs        | ✅        | 약물 사용       | object     |
| education    | ✅        | 학력 상태       | object     |
| ethnicity    | ❌        | 인종            | object     |
| height       | ✅        | 키 (inch)       | float64    |
| income       | ❌        | 연소득 (USD)    | int64      |
| job          | ✅        | 직업            | object     |
| last_online  | ✅        | 마지막 접속     | object     |
| location     | ❌        | 거주 지역       | object     |
| offspring    | ❌        | 자녀 여부/계획  | object     |
| pets         | ✅        | 반려동물        | object     |
| religion     | ✅        | 종교 및 태도    | object     |
| sign         | ❌        | 별자리 및 태도  | object     |
| smokes       | ✅        | 흡연 여부       | object     |
| speaks       | ❌        | 사용 언어       | object     |
| essay0       | ✅        | 자기소개        | object     |
| essay1       | ✅        | 인생 방향       | object     |
| essay2       | ✅        | 잘하는 것       | object     |
| essay3       | ✅        | 첫인상          | object     |
| essay4       | ✅        | 취향            | object     |
| essay5       | ✅        | 필수 요소       | object     |
| essay6       | ✅        | 많이 생각하는 것| object     |
| essay7       | ✅        | 금요일 밤       | object     |
| essay8       | ✅        | 가장 사적인 고백| object     |
| essay9       | ✅        | 메시지 조건     | object     |

## 3. 기술 스택

```
Language     Python 
ML           scikit-learn, XGBoost, LightGBM, CatBoost
Data         pandas, numpy
Viz          matplotlib, seaborn
Imbalance    imbalanced-learn (SMOTE)
Tuning       Optuna, GridSearch, RandomSearch, CrossValidation, K-Fold, early stopping, threshold
Save         joblib (ML)
Environment  Jupyter Notebook / VS Code
Version      Git / GitHub
```

## 4. WBS (Work Breakdown Structure)
<div>
  <img src="./data/img/WBS.png" width="50%">
</div>

## 5. 데이터 전처리 결과서 (EDA)
### 모델 별 전처리 시 확인 포인트

범주형 object 타입 컬럼이 많아 전처리 기준 확립


### 결측치 이상치
<div>
  <img src="./data/img/descrivbe.png" width="30%"><br>
  <img src="./data/img/outlier_age.png" width="40%"> <br>
  <img src="./data/img/outlier_height.png" width="40%"> <br>
  <img src="./data/img/object_col.png" width="40%">
  
</div>


### 전처리

### 1. 인적 사항 및 배경 (Demographic & Background)
| 피처명 | 설명 | 비고 |
| :--- | :--- | :--- |
| **age** | 나이 | 나이대 별 |
| **status** | 연애 중 | 연애를 하는 중, 안하는 중 |
| **orientation** | 성적지향 | 이성애자, 성소수자 |
| **body_type** | 체형 | 마름, 보통, 건강, 통통 |
| **education** | 학력 | 석사이상(4), 학사졸업(3), 학사재학(2), 고등이하(1), 그외(0) |
| **religion** | 종교 | 종교가 있다(1), 없다(0) |
| **job** | 직업 | 연봉 기준으로 0~4로 분류 |

---

### 2. 생활 습관 및 성향 (Lifestyle & Preferences)
- **diet (식단)** : 유연함(0), 중간(1), 엄격함(5)
- **drinks (음주 빈도)** : 안마신다(0), 적당히 마신다(1), 많이마신다(5)
- **drugs (약물 사용)** : 안한다(0), 가끔한다(1), 자주한다(5)
- **smokes (흡연 여부)** : 흡연을 안한다(0), 조금한다(1), 자주 한다(5)
- **niche_score (매칭 시장 내 배타성 지수)** : smokes + drinks + drugs + diet 매칭 마찰력 누적
  > **정의:** 탐색이론기반으로 유저의 생활 습관 데이터에 가중치를 부여하여 매칭 난이도를 수치화 한 지표 <br>
  > **Note:** 음주 기준 0과 1의 지표는 성향 차이라 판단 하지만 %의 지표는 성향 차이가 아닐 것이라 판단해 niche_score 1의 합산보다 높게 설정

---

### 3. 활동성 및 서비스 이용 (Engagement & Activity)
- **last_online (마지막 접속)** : 시간별 데이터를 일별 데이터 분류 -> 이탈율 계산
- **response rate (답변성실도)** : 전체의 빈칸이 적은 정도
- **total_essay_len (에세이 총 글자)** : 에세이의 총 글자 수 합산
- **essay_answered_count (작성한 에세이 질문 개수)** : 작성한 essay 질문 개수

---

###  Target Variable (예측 목표)
- **churn (이탈)** : 이탈(1), 잔류(0)

> **📌 이탈 정의 및 레이블 기준**
> - 본 데이터셋의 `last_online` 컬럼을 기준으로, **기준일(데이터 수집일)로부터 180일(약 6개월) 이상 미접속한 유저를 이탈(1)로 정의**
> - 기준일: 데이터셋 내 `last_online` 최댓값 기준으로 설정
>
> **⚠️ 이탈 정의의 한계 (피드백 반영)**
> 1. **'좋은 이탈' 미구분**: `last_online` 기반 정의는 매칭 성공 후 앱을 떠난 유저(긍정적 이탈)와 단순 무관심으로 떠난 유저(부정적 이탈)를 구분할 수 없음. 두 유형이 모두 이탈(1)로 레이블링되어 모델 학습 시 노이즈로 작용할 수 있음.
> 2. **휴면 고객 미구분**: 장기간 미접속이더라도 향후 재가입할 수 있는 휴면 고객과 완전 이탈 고객을 구분하지 못함. 특히 가입 기간이 짧은 유저의 경우, 단순 미접속과 실질적 이탈의 경계가 모호함.
> 3. **행동 데이터 부재**: OkCupid 데이터셋은 프로필 정보 중심으로, 접속 빈도·매칭 횟수 등 실제 이탈 원인과 직결되는 행동 로그 데이터가 없어 이탈 예측 자체의 구조적 한계가 존재함. 

### EDA



이탈 vs 잔류인원
<div>
  <img src="./data/img/eda_churn.png" width="50%">
</div>


essay_answered_count별 이탈률
<div>
  <img src="./data/img/eda_eac.png" width="50%">
</div>


heatmap
<div>
  <img src="./data/img/heatmap.png" width="50%">
</div>



### 최종 데이터 구조
| 컬럼명                  | 설명                         | 데이터타입 |
|------------------------|-----------------------------|------------|
| sex                    | 성별                        | int8       |
| orientation            | 성적지향 여부                 | int8       |
| diet                   | 식단                         | int64      |
| drugs                  | 약물 사용 여부                | int64      |
| education              | 학력 수준                    | float64    |
| height                 | 키 (inch)                   | float64    |
| body_type_average      | 평균 체형 여부                | bool       |
| body_type_curvy        | 통통한 체형 여부              | bool       |
| body_type_fit          | 건강 체형 여부                | bool       |
| body_type_slim         | 마른 체형 여부                | bool       |
| smokes                 | 흡연자 여부                   | bool      |
| drinks                 | 과음 여부(0, 1 ,5)           | int64      |
| job_score              | 연봉기준  0~4                | float64    |
| religion_religion      | 종교 여부                    | bool       |
| status_encoding        | 연애 상태 인코딩값            | int64      |
| age_group              | 연령대 그룹                  | int64      |
| response rate          | 답변 성실도                  | float64    |
| total_essay_len        | 에세이 전체 글자 수 합산       | int64      |
| essay_answered_count   | 작성한 에세이 질문 개수        | int64      |
| niche_score            | 매칭 시장 내 배타성지수        | float64    |
| churn                  | 고객 이탈                    | int64      |


## 6. 인공지능 학습 결과서

### 모델 성능 평가 비교

<div>
  <img src="./data/img/before_model.png" width="50%">
</div>

#### 보정전

| 모델명        | Accuracy | Recall | F1-Score |
|--------------|----------|--------|----------|
| Logistic     | 0.59     | 0.49   | 0.45     |
| RandomForest | 0.69     | 0.27   | 0.37     |
| XGBoost      | 0.67     | 0.41   | 0.45     |
| Light GBM    | 0.65     | 0.58   | 0.52     |
| CatBoost     | 0.45     | 0.65   | 0.40     |


* **Logistic Regression**
    * **Strategy:** `SMOTE`를 활용한 오버샘플링 (데이터 불균형 해소)
* **RandomForest**
    * **Optimization:** `Optuna` 기반 베이지안 최적화
    * **Strategy:** `GridSearch`, `CrossValidation`을 통한 전수 조사 및 교차 검증
* **CatBoost**
    * **Strategy:** `RandomSearch`를 활용한 효율적 파라미터 탐색

* **XGBoost & LightGBM**
    * **Optimization:** `Optuna` 기반 베이지안 최적화
    * **Validation:** `K-Fold` 교차 검증
    * **Training Control:** `Early Stopping` 적용 (과적합 방지)
    * **Evaluation & Post-processing:** * `PR_AUC` (정밀도-재현율 곡선 아래 면적) 기준 최적화
        * `Threshold` (임계값) 조정을 통한 최종 모델 보정

<div>
  <img src="./data/img/after_model.png" width="50%">
</div>

#### 보정후

| 모델명        | Accuracy | Recall | F1-Score |
|--------------|----------|--------|----------|
| Logistic     | 0.58     | 0.55   | 0.57     |
| RandomForest | 0.66     | 0.54   | 0.51     |
| XGBoost      | 0.58     | 0.75   | 0.55     |
| Light GBM    | 0.60     | 0.72   | 0.54     |
| CatBoost     | 0.55     | 0.70   | 0.45     |

**Accuracy(정확도)**와, **F1-Score**가 고루 분포되어있는가운데 
**Recall(재현율)** 값이 가장 높은 **XGBoost** 채택

### XGBoost 

#### 혼동행렬

<div>
  <img src="./data/img/xgb_cm.png" width="50%">
</div>

#### ROC & P-R

<div>
  <img src="./data/img/xgb_roc.png" width="50%">
</div>

<div>
  <img src="./data/img/xgb_pr.png" width="50%">
</div>

## 7. 결론

본 프로젝트는 **이진 분류(Binary Classification)** 를 통해 이탈 고위험군 유저를 식별하는 것을 목적으로 하였으며, 이에 맞게 모델 학습과 평가를 수행하였습니다.

> **📌 이진 분류 목적에 맞는 학습·평가 여부**
> - **레이블**: `last_online` 기준 180일 이상 미접속 → 이탈(1) / 잔류(0) 로 이진 분류 레이블 생성
> - **클래스 불균형 처리**: 이탈(1) 비율이 약 8%로 불균형하여, SMOTE(일부 모델) 및 class_weight/scale_pos_weight 적용으로 이탈 클래스 학습 강화
> - **평가 지표**: 이탈 예측의 비즈니스 목적(이탈자를 최대한 포착)에 맞게 Recall을 주 지표로, ROC-AUC·F1을 보조 지표로 설정. Accuracy는 클래스 불균형 환경에서 신뢰도가 낮아 주 지표에서 제외.
> - **모델 선정**: ROC-AUC 기준 전 모델이 0.56~0.62 수렴 → 프로필 기반 데이터의 구조적 한계로 판단, Recall 0.75를 기록한 XGBoost를 최종 모델로 선정

### 테스트 데이터 넣어서 결과 도출

<div>
  <img src="./data/img/final_test.png" width="50%">
</div>

### 🔍 한계점

* **이탈 레이블 정의의 모호성**
    * `last_online` 기준 180일 미접속을 이탈로 정의했으나, 이는 행동 의도를 반영하지 못함.
    * 매칭 성공 후 자연스럽게 떠난 **'좋은 이탈'** 과 단순 무관심으로 인한 **'나쁜 이탈'** 이 동일하게 이탈(1)로 레이블링되어 모델 학습의 노이즈로 작용.
    * 가입 기간이 짧은 유저의 경우, 미접속 기간만으로 이탈을 판단하기 어려우며 **휴면 고객과 완전 이탈 고객의 구분이 불가**.

* **프로필 기반 데이터의 구조적 한계**
    * 접속 빈도, 매칭 횟수, 대화 지속 시간 등 **이탈 원인과 직결되는 행동 로그 데이터가 없음**.
    * 전 모델이 ROC-AUC 0.56~0.62 구간에서 수렴한 것은 모델의 문제가 아니라, **피처(데이터) 자체의 정보량 한계**로 해석.
    * ROC-AUC 등 평가 지표는 절대적 기준이 아니며, 데이터 특성과 비즈니스 맥락에 따라 해석이 달라짐.

* **이진 분류의 표현력 한계**
    * 이탈(0/1) 이진 레이블은 이탈의 동기와 성격을 담지 못함.
    * 동일한 '이탈'이라도 매칭 성공, 피로감, 비용 문제 등 원인이 다양하여 단순 이진 분류만으로는 실무 개입 전략 수립에 한계가 있음.

---

### 개선방안

* **이탈 정의 정교화**
    * 향후 행동 로그 데이터(접속 빈도, 매칭 수, 대화 지속 기간 등) 확보 시, 단순 미접속 기간이 아닌 **복합 행동 기반 이탈 정의**로 레이블 품질 향상 가능.
    * 가입 기간별 이탈 기준을 차등 적용(예: 가입 1년 미만은 30일, 이상은 180일)하는 **세분화된 레이블링 전략** 도입 검토.

* **'좋은 이탈' / '나쁜 이탈' 구분**
    * 매칭 성공 여부 데이터가 있다면 이탈 유형을 분리하여 **목적 달성형 이탈을 별도 클래스**로 처리, 모델 노이즈 감소 가능.

* **비지도 학습 기반의 이탈 동기 군집화**
    * 비지도 학습을 도입하여 단순 이탈 여부(0, 1)를 넘어, **이탈 동기에 따른 군집 분석**으로 개입 전략을 차별화.

* **분석의 다각화 및 범용성 확보**
    * 본 파이프라인(전처리 → 학습 → 평가)은 데이팅앱 외에도 채용, 교육, 구독형 서비스 전반에 적용 가능한 **범용 이탈 예측 프레임워크**로 확장 가능.

## 8. 한 줄 회고

<table>
  <colgroup>
    <col style="width: 10%; text-align: center;">
    <col style="width: 85%;">
  </colgroup>
  <thead>
    <tr>
      <th style="text-align: center;">이름</th>
      <th style="text-align: center;">회고</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;"><strong>고아라</strong></td>
      <td>
  <strong>[Keep]</strong> 데이터 전처리 설계와 문서화 작업에서 팀에 기여할 수 있었다.<br>
  <strong>[Problem]</strong> ML/DL 모델의 전체적인 흐름과 구조에 대한 학습이 더 필요하다고 느꼈다.<br>
  <strong>[Try]</strong> SMOTE 적용 후 XGBoost/LightGBM의 Recall이 0에 가까워지는 문제를 직접 발견하고 원인을 분석해 해결하면서, 데이터와 모델의 특성을 함께 이해해야 한다는 것을 배웠다. 다음엔 ML/DL 전체 파이프라인을 처음부터 직접 구현해보는 학습을 진행할 것이다.
</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>권민제</strong></td>
      <td>이번 프로젝트를 통해 모델의 성능 향상을 위한 노력을 기울인 결과, 하이퍼 파라미터 튜닝만큼이나 목적에 부합하는 데이터 전처리가 모델의 예측력에 결정적인 영향을 미친다는 점을 깊이 체감했습니다.  <br>이러한 성찰을 바탕으로 향후에는 비지도 학습을 활용하여 유저의 이탈 동기를 정교하게 라벨링하고 세분화함으로써, 현재의 이진 분류 모델이 가진 한계를 극복하고 모델의 변별력을 한층 더 고도화하는 시도를 이어가고자 합니다.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>김규호</strong></td>
      <td>keep: 데이터의 전처리 과정의 모든 사람의 의견을 듣고 모두가 납득할 방법으로 전처리 시행, 모든 과정에 대해 궁금증을 가지고 접근 <br>
      problem: 행동 데이터의 전처리 과정에 대해 의견 취합<br>
      try: 의견 충돌이 났을 때 두 전처리 데이터를 모두 사용 해보기</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>김정현</strong></td>
      <td>이번 프로젝트 진행을 위해 살펴본 해당 데이터셋은 대부분 문자열 값을 갖는 컬럼들이었습니다. 시간이 오래 걸릴 것으로 예상되어 팀원들과 하나씩 의견을 나누며 EDA/전처리 과정을 수행했습니다. <br>다만 컬럼 하나하나마다 범주화를 어떻게 할지 정하는 게 쉽지 않아 전처리 작업이 어려웠고, 기대만큼 모델들의 성능이 나오지 않아 걱정이 컸습니다. 전처리에 대해서는, 처음부터 복잡한 전처리에 매달리기보다 아주 단순한 모델을 먼저 만들고 단계적으로 전처리를 고도화하는 방식을 고려해 보겠습니다. 또한, 성능 향상에 도움이 되는 방법들을 적용해 보고 성능 변화를 살펴보도록 하겠습니다.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>최현진</strong></td>
      <td></td>
    </tr>
  </tbody>
</table>

---

## 📁 프로젝트 폴더 구조
---
```

📁 SKN24-2ND-2Team/
├── 📁 data/
|   ├──📁 img/               ← README의 사용된 사진
│   ├── Original data.csv     ← 원본 데이터 CSV (gitignore 처리)
│   └── Original data_process ← 전처리 완료데이터 CSV (gitignore 처리)
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




```

