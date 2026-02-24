# 🚀 SK네트웍스 Family AI 캠프 24기 2차 프로젝트 

## 주제: 데이터분석 + 머신러닝 + 딥러닝을 활용한 가입 고객 이탈 예측 (Churn Prediction)



---

## 1. 2팀 소개 - 
- **팀명**: SKN24-2nd-2Team (Cupid Rescue)
- **멤버**:
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

<br />



## 2. 프로젝트 개요

### 프로젝트 명
> 💘 OkCupid 데이팅앱 유저 데이터를 활용한 가입 고객 이탈 예측 (Churn Prediction)

### 프로젝트 소개
> OkCupid는 미국의 온라인 데이팅 플랫폼으로, 본 프로젝트에서 활용한 데이터셋은 **북캘리포니아 지역 한정의 과거 공개 데이터**임. OkCupid는 현재 서비스가 사실상 종료된 상태이며, 데이터 역시 행동 로그 없이 **프로필 정보만으로 구성**된 제한적인 데이터셋임.

이러한 한계에도 불구하고, 본 프로젝트는 해당 데이터를 활용해 **고객 이탈 예측 파이프라인을 직접 설계·구현**하고, ML/DL 모델의 성능을 비교 분석하는 것을 목표로 함. 개발된 파이프라인은 데이팅앱을 포함한 **구독형 서비스 전반의 이탈 예측에 적용 가능한 범용 프레임워크**로 확장될 수 있음.

### 프로젝트 필요성 (배경)

### 📊 데이팅앱 시장 10년 트렌드 (2015–2024)

![글로벌 데이팅앱 시장 트렌드](./assets/market_trend_chart.png)

> **차트 읽는 법**
> - ① 시장 규모는 10년간 **5.7배 성장** ($1.69B → $9.65B) — 그러나 2021년 이후 성장세 뚜렷하게 둔화
> - ② 이용자 수는 꾸준히 증가했지만, ③ **리텐션율(복귀율)은 매년 하락** — 이용자는 늘어도 앱에 머무르지 않음
> - ④ 다운로드는 2019년 역대 최고(287M) 이후 **지속 감소** — 신규 유입이 줄고 있음
> - ⑤ 앱별 30일 리텐션: **Bumble 11%, Tinder 7.8%** — 업계 전체 평균(6%) 대비 여전히 낮은 수준
> - ⑥ Tinder 유료 구독자는 2022년 고점(10.8M) 이후 **첫 역성장** → 수익화 위기의 신호

| 출처 | 데이터 |
|---|---|
| Business of Apps (2026) | 전 세계 시장 규모 연도별 |
| Statista / Priori Data | 글로벌 이용자 수 |
| Adjust Valentine's Day Report (2025) | Day-1/7/30 리텐션율 연도별 추이 |
| Similarweb (2023) | 앱별 30일 리텐션 비교 |
| DemandSage Tinder Statistics (2026) | Tinder 유료 구독자 연도별 |

--- 

#### 📱 데이팅앱 시장의 성장

> 데이팅앱 시장은 전 세계적으로 빠르게 성장하고 있음.

| 지표 | 수치 | 출처 |
|---|---|---|
| 전 세계 데이팅앱 시장 규모 (2024) | **$81억** → 2027년 $87억 전망 | Statista (아시아경제, 2024.05.23 인용) |
| 국내 데이팅앱 시장 규모 (2024) | **$3,507만** → 2028년 $3,642만 전망 | Statista (아시아경제, 2024.05.23 인용) |
| 국내 데이팅앱 소비자 지출 (2023) | **약 1,614억원** ($1.2억) | data.ai, 2024 모바일 현황 보고서 (아시아경제, 2024.03.13 인용) |
| 국내 로맨스 스캠 피해액 (2023) | **55억 1,200만원** — 2020년 대비 15배 급증 | 아시아경제, 2024.05.23 |


![데이팅앱 시장 현황 — 뉴스 데이터 기반](./assets/background_charts_v2.png)


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

#### 🏗️ 데이팅앱의 구조적 이탈 딜레마

> 일반 구독 서비스와 달리, 데이팅앱은 **"매칭 성공 = 앱 이탈"** 이라는 구조적 특수성을 가짐. 
> 서비스가 잘 작동할수록 사용자가 떠나는 역설적 구조이기 때문에, 이탈 예측과 방지가 더욱 중요하고 어려움.
> NYT는 "데이팅 앱이 연애하는 삶을 달라지게 했지만, 젊은 사용자들이 돈을 내도록 설득하진 못했다"고 평가하였음.

본 프로젝트는 이러한 배경 속에서, OkCupid 프로필 데이터를 활용해 **고객 이탈 예측 파이프라인을 설계·구현**하고, 
실무에서 자주 마주치는 클래스 불균형 문제를 직접 해결하고자 함.

---

#### 📚 참고 문헌

| # | 매체 | 제목 | 성격 | 링크 |
|---|---|---|---|---|
| 1 | 아시아경제 (2024.05.23) | 커지는 데이팅 앱 시장…로맨스 스캠 주의보 | 📰 뉴스 — Statista 시장 규모·로맨스 스캠 통계 인용 | [바로가기](https://www.asiae.co.kr/article/2024052215114422592) |
| 2 | 아시아경제 (2024.03.13) | 연애는 하고 싶지만, 돈 쓰긴 싫어…고민에 빠진 데이팅 앱 | 📰 뉴스 — data.ai 미국 지출 증가율 둔화 통계 인용 | [바로가기](https://www.asiae.co.kr/article/2024031310245014777) |
| 3 | 아시아경제 (2024.05.28) | 데이팅앱, 남자만 쓴다…"여성 이용자 유치 어려워" | 📰 뉴스 — FT·Mintel 성비 불균형·시총 손실 인용 | [바로가기](https://www.asiae.co.kr/article/2024052820301656222) |
| 4 | openads (2024.02.05) | 자만추? 앱만추! 얼마를 써야 사랑을 찾을 수 있나요? | 📊 마케팅 인사이트 — 국내 데이팅앱 시장·소비자 지출 분석 (data.ai 인용) | [바로가기](https://www.openads.co.kr/content/contentDetail?contsId=12476) |
| 5 | 고대신문 (2024.06.03) | 틀린 만남은 없다, 문화로 자리 잡은 데이팅 앱 | 📰 대학신문 — 국내 2030 이용 현황·진정성 인식 설문 | [바로가기](https://www.kunews.ac.kr/news/articleView.html?idxno=42496) |



### 프로젝트 목표

1. OkCupid 프로필 데이터를 분석하여 이탈 관련 패턴을 탐색.
2. ML(LR/DT/RF/XGB/LGBM/CatBoost) 및 DL모델을 학습·비교.
3. 클래스 불균형 환경에서 **Recall 최대화**를 핵심 지표로 모델개선.
4. 본 파이프라인을 다른 구독형 서비스에 적용 가능한 형태로 구축.

### 데이터셋 한계 & 그럼에도 얻을 수 있는 인사이트

> ⚠️ **데이터 한계**  
> - 북캘리포니아 한정 해외 데이터 → 국내 서비스에 직접 적용 어려움  
> - 행동 데이터 없음 (접속 빈도, 클릭 등) → 이탈 원인과 직접 인과관계 약한 피처들  
> - `last_online` 기반 churn 정의의 모호함 → "짝을 찾아 떠난 이탈"과 "무관심으로 떠난 이탈"을 구분 불가 (기준: 180일 미접속)

| 인사이트 | 내용 | 실제 근거 |
|---|---|---|
| ⚖️ SMOTE의 함정 발견 | 잘못된 불균형 처리 방법 하나가 Recall을 0.01까지 끌어내림 — 직접 원인 분석 후 해결 | XGB Recall 0.018→0.411 (수치로 증명) |
| 🎯 Threshold는 도구, 성능이 아님 | 임계값 0.3 적용 시 Recall 0.927이지만, 이탈 예측 100명 중 91명이 오탐 — trade-off 직접 체감 | Precision 0.086로 확인 |
| 📉 데이터가 모델의 천장을 결정 | 모델 8개 모두 ROC-AUC 0.56~0.62 수렴 — 피처 정보량 자체가 한계임을 확인 | 전 모델 동일 구간 수렴 |
| 🔄 파이프라인 구조는 재사용 가능 | 전처리→학습→평가 흐름은 다른 서비스에 적용 가능한 구조로 설계됨 (피처 컬럼 재정의 필요) | 코드 모듈화 완료 |

---

### 데이터셋 기본 정보
- 출처: Kaggle - OkCupid Profiles
- 규모: 약 59,946건 (거의 60,000명)
- 수집 지역: 샌프란시스코 (San Francisco)
- 수집 시기: 2012년 6월
- 데이터 타입: 구조화된 프로필 정보 + 자유 텍스트 (에세이)

행 개수: 59,946개

컬럼 개수: 31개

데이터 타입 구성

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
| ethnicity    | ✅        | 인종            | object     |
| height       | ✅        | 키 (inch)       | float64    |
| income       | ❌        | 연소득 (USD)    | int64      |
| job          | ✅        | 직업            | object     |
| last_online  | ✅        | 마지막 접속     | object     |
| location     | ✅        | 거주 지역       | object     |
| offspring    | ❌        | 자녀 여부/계획  | object     |
| pets         | ✅        | 반려동물        | object     |
| religion     | ✅        | 종교 및 태도    | object     |
| sign         | ✅        | 별자리 및 태도  | object     |
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


---

## 3. 기술 스택

```
Language     Python 
ML           scikit-learn, XGBoost, LightGBM, CatBoost
DL           PyTorch
Data         pandas, numpy
Viz          matplotlib, seaborn
Imbalance    imbalanced-learn (SMOTE)
Tuning       Optuna
Save         joblib (ML), torch.save state_dict (DL)
Environment  Jupyter Notebook / VS Code
Version      Git / GitHub
```

---

## 4. WBS (Work Breakdown Structure)

| 단계 | 작업 내용 | 담당 | 상태 |
|---|---|---|---|
| 1. 데이터 수집 | OkCupid 공개 데이터셋 로드 | All | ✅ |
| 2. EDA | 결측치·분포·상관관계 분석 | All | ✅ |
| 3. 전처리 | 인코딩, 스케일링, churn 생성 | All | ✅ |
| 4. ML 모델링 | LR/DT/RF/XGB/LGBM/CatBoost | All | ✅ |
| 5. DL 모델링 | ANN (PyTorch) | All | ✅ |
| 6. 성능 비교 | ML vs DL 비교표 & 시각화 | All | ✅ |
| 7. 수행 결과 | - | 전체 | ✅ |
| 8. README 작성 | 결과서 정리 | All | ✅ |


---

## 5. 데이터 전처리 결과서 (EDA)

### 원본 데이터
> - 출처: OkCupid 공개 프로필 데이터셋
> - 크기: 59,946명 × 31개 컬럼 (원본)

### 타겟 변수 생성 (churn 정의)
```
last_online 컬럼 기준:
- 기준일(데이터 내 가장 최근 접속일: 2012-07-01)로부터 180일 이상 미접속 → 이탈(1)
- 180일 미만 → 잔류(0)
```

![이탈 vs 잔류 인원 수](./assets/prep_churn_bar.png)

### 전처리 주요 작업

> 💡 범주형 object 타입 컬럼이 많아 **전처리 기준 확립이 핵심 과제**였음

**1. 결측치 처리**

![결측치 히트맵](./assets/eda_missing_heatmap.png)

![결측치 비율](./assets/eda_missing_bar.png)

| 컬럼 | 처리 방법 |
|---|---|
| 수치형 (income 등) | 중앙값 대체 |
| 범주형 (religion, education 등) | 최빈값 대체 또는 'unknown' 처리 |
| 결측률 70% 초과 컬럼 | 제거 |

---

**2. 이상치 처리**

![수치형 컬럼 이상치 분포 (age, height, income)](./assets/eda_outlier_dist.png)

---

**3. 피처 인코딩 상세**

| 컬럼 | 인코딩 방식 | 변환 기준 |
|---|---|---|
| `age` | 연령대 그룹화 | 10대별 구간 분류 → `age_group` |
| `status` | Binary Encoding | single(1) / 나머지(0) → `status_encoding` |
| `orientation` | Label Encoding | straight(0) / gay·bisexual(1) |
| `body_type` | One-Hot Encoding | slim / average / fit / curvy → 4개 컬럼 |
| `education` | One-Hot Encoding | univ_grad / univ_ing / high_school / other → 4개 컬럼 |
| `religion` | One-Hot Encoding | religion(1) / no_religion(0) → 2개 컬럼 |
| `diet` | Binary Encoding | 채식·비건(1) / 비채식(0) → `diet_encoding` |
| `drinks` | One-Hot Encoding | no_drinks / moderate / heavy → 3개 컬럼 |
| `drugs` | Ordinal Encoding | never(2) / sometimes(1) / often(0) |
| `smokes` | One-Hot Encoding | no_smoke / smoke / sometime_smoke → 2개 컬럼 (drop_first=True) |
| `job` | Ordinal Encoding | 직군별 연봉 기준 0~5 분류 → `job_encoding` |
| `sign` | Binary Encoding | 별자리 믿음 여부 (1/0) → `sign_belief_encoding` |
| `ethnicity` | One-Hot Encoding | white / asian / black / hispanic / other / mixed → 6개 컬럼 |
| `pets` | Binary Encoding | dogs_encoding (강아지 선호 여부), cats_encoding (고양이 선호 여부) |
| `location` | One-Hot Encoding | sf / east_bay / south_bay / north_bay / outside → 5개 컬럼 |
| `last_online` | 파생 변수 → churn | 180일 이상 미접속 → 이탈(1) |

---

**4. 파생 변수 생성**

| 파생 변수 | 설명 | 생성 방식 |
|---|---|---|
| `age_group` | 연령대 그룹 | age를 10단위로 구간화 |
| `sign_belief_encoding` | 별자리 믿음 여부 | 믿음(1) / 안 믿음(0) |
| `job_encoding` | 직군 연봉 등급 | IT/과학, 비즈니스, 예술, 전문직 등 0~5 분류 |
| `status_encoding` | 연애 상태 | single(1) / 나머지(0) |
| `diet_encoding` | 식단 성향 | 채식·비건(1) / 비채식(0) |
| `dogs_encoding` | 강아지 선호 여부 | 선호(1) / 비선호(0) |
| `cats_encoding` | 고양이 선호 여부 | 선호(1) / 비선호(0) |
| `location_group` | 거주 지역 그룹 | sf / east_bay / south_bay / north_bay / outside |
| `churn` | 이탈 여부 (타겟) | last_online 기준 **180일** 이상 미접속 → 이탈(1) |

---

**5. 인코딩 & 스케일링**
- 이진 범주형: Label Encoding (sex, status 등)
- 다중 범주형: One-Hot Encoding (ethnicity, body_type 등)
- 수치형 범주형: Ordinal Encoding (education, income 등)
- ML 모델: StandardScaler (로지스틱 회귀 적용)
- DL 모델: StandardScaler (전체 피처)

---

**6. 클래스 불균형 처리**
```
원본 비율 — 잔류: 92% / 이탈: 8%

처리 방법:
  - ML (LR/DT/RF): SMOTE (train 데이터만) → 50:50
  - ML (XGB/LGBM/CatBoost): class_weight / scale_pos_weight
  - DL: pos_weight (BCEWithLogitsLoss)
```

---

**7. 최종 데이터셋 구조**
```
행: 59,934명  컬럼: 38개 (특성 37개 + churn 1개)
Train: 47,947명  Test: 11,987명 (stratify=y)
이탈 비율 — Train: 8.0%  Test: 8.0%
```

| 컬럼명 | 설명 | 데이터타입 |
|---|---|---|
| sex | 성별 | int8 |
| orientation | 성적지향 여부 | int8 |
| drugs | 약물 사용 (never=2 / sometimes=1 / often=0) | int8 |
| height | 키 (inch, 표준화) | float64 |
| sign_belief_encoding | 별자리 믿음 여부 | int64 |
| age_group | 연령대 그룹 (표준화) | float64 |
| education_high_school | 고등학교 이하 여부 | bool |
| education_other | 기타 학력 여부 | bool |
| education_univ_grad | 대학교 졸업 여부 | bool |
| education_univ_ing | 대학교 재학 여부 | bool |
| body_type_average | 보통 체형 여부 | bool |
| body_type_curvy | 통통한 체형 여부 | bool |
| body_type_fit | 건강/탄탄 체형 여부 | bool |
| body_type_slim | 마른 체형 여부 | bool |
| smokes_smoke | 흡연자 여부 | bool |
| smokes_sometime_smoke | 가끔 흡연 여부 | bool |
| drinks_heavy | 과음 여부 | bool |
| drinks_moderate | 적당한 음주 여부 | bool |
| drinks_no_drinks | 비음주 여부 | bool |
| religion_no_religion | 무교 여부 | bool |
| religion_religion | 종교 여부 | bool |
| job_encoding | 직군 연봉 등급 0~5 | int64 |
| status_encoding | 연애 상태 (single=1) | int64 |
| diet_encoding | 식단 (채식=1 / 비채식=0) | int64 |
| ethnicity_asian | 아시아계 여부 | bool |
| ethnicity_black | 흑인 여부 | bool |
| ethnicity_hispanic / latin | 히스패닉/라틴계 여부 | bool |
| ethnicity_mixed | 혼혈 여부 | bool |
| ethnicity_other | 기타 인종 여부 | bool |
| ethnicity_white | 백인 여부 | bool |
| dogs_encoding | 강아지 선호 여부 | int64 |
| cats_encoding | 고양이 선호 여부 | int64 |
| location_group_east_bay | East Bay 거주 여부 | bool |
| location_group_north_bay | North Bay 거주 여부 | bool |
| location_group_outside | 외곽 거주 여부 | bool |
| location_group_sf | SF 거주 여부 | bool |
| location_group_south_bay | South Bay 거주 여부 | bool |
| churn | 고객 이탈 (타겟) | int64 |

---


## 6. 인공지능 학습 결과서

### 평가 지표 선정 이유
> 이탈 고객을 **놓치지 않는 것**이 핵심 → **Recall(재현율)**최우선
> ROC-AUC로 전체 판별력, F1으로 균형 성능 보조 확인

### 6-1. 머신러닝 (ML) 모델

#### 초기 학습 결과 (v1 — SMOTE 적용, XGB/LGBM/CatBoost 문제 있음)

| 모델 | Recall | ROC-AUC | F1 | Precision |
|---|---|---|---|---|
| Decision Tree | 0.492 | 0.560 | 0.158 | 0.094 |
| Random Forest | 0.457 | 0.587 | 0.164 | 0.100 |
| Logistic Regression | 0.301 | 0.561 | 0.153 | 0.102 |
| **XGBoost** | **0.018** | 0.588 | 0.033 | 0.185 |
| **LightGBM** | **0.015** | 0.593 | 0.027 | 0.189 |
| **CatBoost** | **0.011** | 0.598 | 0.020 | 0.147 |

> ⚠️ XGBoost/LightGBM/CatBoost: SMOTE 데이터를 eval_set으로 사용하여 early stopping이 잘못 작동 → Recall 거의 0

#### 문제 해결 — 성능 향상을 위한 노력 (v2)

**원인 분석:** SMOTE 처리된 데이터로 early_stopping을 수행하면 원본 불균형 패턴을 학습하지 못함

**해결 방법:** `class_weight / scale_pos_weight / auto_class_weights`로 교체 + 원본 데이터로 학습

```python
# XGBoost: scale_pos_weight (잔류수 / 이탈수)
XGBClassifier(scale_pos_weight=11.55)

# LightGBM: class_weight='balanced'
LGBMClassifier(class_weight='balanced')

# CatBoost: auto_class_weights='Balanced'
CatBoostClassifier(auto_class_weights='Balanced')
```

#### 개선 후 결과 (v2)

| 모델 | Recall | ROC-AUC | F1 | Precision |
|---|---|---|---|---|
| Decision Tree | 0.492 | 0.560 | 0.158 | 0.094 |
| **CatBoost** ⭐ | **0.472** | **0.611** | **0.189** | **0.118** |
| Random Forest | 0.457 | 0.587 | 0.164 | 0.100 |
| LightGBM | 0.423 | 0.603 | 0.182 | 0.116 |
| XGBoost | 0.411 | 0.594 | 0.177 | 0.113 |
| Logistic Regression | 0.301 | 0.561 | 0.153 | 0.102 |

> ✅ XGBoost Recall: 0.018 → 0.411 (+0.393)  
> ✅ LightGBM Recall: 0.015 → 0.423 (+0.408)  
> ✅ CatBoost Recall: 0.011 → 0.472 (+0.461) — ML 최고 성능  

![ML 모델별 성능 비교](./assets/ml_compare.png)

---

### 6-2. 딥러닝 (DL) 모델 — PyTorch

#### 모델 구조

**ANN Basic**
```
Input(37) → Linear(64) → ReLU → Linear(32) → ReLU → Linear(1)
Loss: BCEWithLogitsLoss(pos_weight=11.55)
Optimizer: Adam(lr=0.001)
```

**ANN Advanced**
```
Input(37) → Linear(128) → BatchNorm → ReLU → Dropout(0.3)
         → Linear(64)  → BatchNorm → ReLU → Dropout(0.3)
         → Linear(32)  → ReLU
         → Linear(1)
Loss: BCEWithLogitsLoss(pos_weight=11.55)
Optimizer: AdamW(lr=0.001, weight_decay=0.01)
Scheduler: ReduceLROnPlateau(patience=5, factor=0.5)
EarlyStopping: patience=20
```

#### 성능 향상을 위한 노력

| 시도 | 내용 | 효과 |
|---|---|---|
| pos_weight 설정 | 불균형 처리 (잔류수/이탈수 = 11.55) | Recall 향상 |
| BatchNorm 추가 | 학습 안정화 | Loss 감소 안정화 |
| Dropout(0.3) | 과적합 방지 | Val Loss 개선 |
| AdamW | Weight Decay 적용 | 일반화 성능 향상 |
| ReduceLROnPlateau | 동적 LR 감소 | 수렴 개선 |
| Threshold 조정 | 0.5 → 0.3 | Recall 0.544 → 0.927 |
| patience 조정 (v2) | 5→15 (Basic), 7→20 (Advanced) | 충분한 학습 보장 |

> 💡 **patience를 늘려도 Epoch 17~23에서 조기 종료** → 데이터 자체의 한계로 추가 튜닝 효과 없음

#### DL 최종 결과 (v2)

| 모델 | Recall | ROC-AUC | F1 | Precision |
|---|---|---|---|---|
| ANN Advanced (thr=0.3) | **0.927** | 0.621 | 0.157 | **0.086** |
| ANN Advanced (thr=0.5) | 0.544 | **0.621** | **0.192** | 0.117 |
| ANN Basic (thr=0.5) | 0.483 | 0.588 | 0.170 | 0.103 |

> 💡 **patience를 늘려도 ANN Basic Epoch 17, ANN Advanced Epoch 23에서 조기 종료** → 데이터 자체의 한계로 추가 튜닝 효과 없음

![DL ANN Basic 학습 곡선](./assets/dl_basic_train.png)

![DL ANN Advanced 학습 곡선](./assets/dl_adv_train.png)

---

### 6-3. ML vs DL 최종 비교

| 순위 | 모델 | Recall | ROC-AUC | F1 |
|---|---|---|---|---|
| 🥇 | ANN Advanced (thr=0.3) | **0.927** | 0.621 | 0.157 |
| 🥈 | ANN Advanced (thr=0.5) | 0.544 | **0.621** | **0.192** |
| 🥉 | DT (ML) | 0.492 | 0.560 | 0.158 |
| 4 | ANN Basic | 0.483 | 0.588 | 0.170 |
| 5 | CatBoost (ML) | 0.472 | 0.611 | 0.189 |

> 💡 **Recall 기준**: DL(ANN) > ML — DL이 이탈 고객을 더 잘 잡아냄  
> 💡 **ROC-AUC 기준**: DL(0.621) > ML CatBoost(0.611) — DL의 전반적 판별력 우수  
> 💡 **F1 균형**: Threshold 0.5 기준 ANN Advanced(0.192) ≈ CatBoost(0.189) — 동등  
> 💡 **데이터 한계**: 프로필 기반 데이터 특성상 ROC-AUC 0.65 이상 향상 어려움  

![ML vs DL 전체 모델 성능 비교](./assets/dl_ml_compare.png)

---

## 7. 수행 결과 

### 7-1. 핵심 발견 1 — SMOTE의 함정✅

> **한 줄 요약:** 잘못된 방법을 쓰면 아무리 좋은 모델도 망가진다.

처음에 클래스 불균형(이탈 8%) 문제를 해결하려고 **SMOTE**(소수 클래스 데이터를 인위적으로 늘리는 기법)를 적용했음.  
그런데 XGBoost, LightGBM, CatBoost 세 모델의 Recall이 **0.01~0.02** 수준, 즉 **100명 중 이탈자를 1~2명밖에 못 잡는** 충격적인 결과가 나왔음.

**왜 ?**

```
SMOTE로 부풀린 훈련 데이터 → 모델 학습
             ↓
검증 데이터는 원본 불균형 비율 (이탈 8%)
             ↓
"이탈처럼 생긴 데이터" 기준이 달라져서 → early stopping이 엉뚱한 시점에 멈춤
             ↓
결과: 이탈을 거의 예측 못하는 모델 완성
```

**해결책:** SMOTE 대신 모델 내부에 "이탈이 소수니까 더 중요하게 봐"라고 알려주는 가중치 설정으로 교체

| 모델 | Recall (수정 전) | Recall (수정 후) | 개선폭 |
|---|---|---|---|
| XGBoost | 0.018 | 0.411 | **+0.393** |
| LightGBM | 0.015 | 0.423 | **+0.408** |
| CatBoost | 0.011 | 0.472 | **+0.461** |

> 💡 **배운 점:** 불균형 데이터 처리는 방법 선택이 전부임. 같은 데이터, 같은 모델이라도 전처리 방식 하나로 성능이 0에 가까운 것과 0.47 사이를 왔다갔다 함.

---

### 7-2. 핵심 발견 2 — 임계값(Threshold) 조정의 양면성 ⚠️

> **한 줄 요약:** 이탈을 더 많이 잡을수록, 엉뚱한 사람도 더 많이 잡힌다.

딥러닝 모델(ANN Advanced)에서 **임계값을 0.5 → 0.3으로 낮춘** 결과:

| 설정 | Recall | Precision | 의미 |
|---|---|---|---|
| Threshold = 0.5 (기본값) | 0.544 | 0.117 | 이탈자 100명 중 54명 발견, 오탐 88명 |
| Threshold = 0.3 (낮춤) | **0.927** | **0.086** | 이탈자 100명 중 93명 발견, **오탐 1,065명** |

**임계값을 낮추면 Recall이 올라가는 건 수학적으로 당연한 결과임.**  
문제는 그 대가로 **"이탈하지 않을 사람을 이탈자로 잘못 예측"하는 비율이 폭발적으로 증가**한다는 점.

```
Precision 0.086 = 이탈이라고 예측한 100명 중 실제 이탈자는 9명
                 → 나머지 91명에게 쿠폰·혜택을 보내면 91%가 낭비
```

**모델의 진짜 실력 — ROC-AUC**는 임계값을 어떻게 바꿔도 **0.621로 고정**.  
즉, Threshold 조정은 "어떤 실수를 더 감수할지 선택하는 것"이지, 모델 자체가 좋아지는 게 아님..

```
ROC-AUC 0.621의 의미:
  - 완전 랜덤 예측 = 0.5
  - 완벽한 모델    = 1.0
  - 우리 모델      = 0.621  →  랜덤보다는 낫지만, 실무 투입엔 한계
```

> 💡 **비즈니스 관점 선택 기준**
> - 비용이 싼 혜택(앱 푸시 알림 등) → Threshold 낮춰 Recall 우선
> - 비용이 비싼 혜택(할인 쿠폰, 전화 상담 등) → Threshold 높여 Precision 우선

---

### 7-3. 핵심 발견 3 — 데이터가 모델의 천장을 결정한다 ✅

> **한 줄 요약:** 모델이 나쁜 게 아니라, 데이터에 답이 없었다.

ML 6개 모델과 DL 2개 모델, 총 8개 모델을 돌린 결과 ROC-AUC가 모두 **0.56~0.62 구간에서 수렴**했음.

```
Logistic Regression  ROC-AUC 0.561   ← 가장 단순한 모델
Decision Tree        ROC-AUC 0.560
CatBoost             ROC-AUC 0.611   ← ML 최고
ANN Advanced         ROC-AUC 0.621   ← 전체 최고
```

아무리 복잡한 모델을 써도 성능이 비슷하게 수렴한다는 것은, **모델의 문제가 아니라 피처(데이터) 자체의 정보량이 한계에 달했다**는 신호.

**왜 프로필 정보만으로는 한계인가?**

| 데이터 종류 | 이탈 예측력 | 우리 데이터 포함 여부 |
|---|---|---|
| 최근 접속 빈도, 앱 사용 시간 | 매우 높음 | ❌ |
| 매칭 성공률, 대화 지속 시간 | 높음 | ❌ |
| 나이, 직업, 종교, 라이프스타일 | 낮음~중간 | ✅ (우리가 가진 것) |

또한 이 데이터의 이탈 정의(`last_online` 기준 **180일 미접속**)는 **"짝을 찾아 행복하게 떠난 사람"과 "관심이 없어서 떠난 사람"을 구분할 수 없어**, 예측 자체가 구조적으로 어려운 문제임.

> 💡 **배운 점:** ROC-AUC 0.62 수렴은 실패가 아니다. "이 데이터로 뽑을 수 있는 최대치에 도달했다"는 것을 여러 모델로 교차 검증한 결과다.

---

### 7-4. 최종 성능 요약

| 모델 | Recall | ROC-AUC | F1 | 비고 |
|---|---|---|---|---|
| ANN Advanced (thr=0.3) | **0.927** | 0.621 | 0.157 | Recall 최대, Precision 희생 |
| ANN Advanced (thr=0.5) | 0.544 | **0.621** | **0.192** | 균형 최적 |
| CatBoost | 0.472 | 0.611 | 0.189 | ML 최고, 해석 용이 |
| LightGBM | 0.423 | 0.603 | 0.182 | |
| XGBoost | 0.411 | 0.594 | 0.177 | |
| Random Forest | 0.457 | 0.587 | 0.164 | |
| ANN Basic | 0.483 | 0.588 | 0.170 | |
| Logistic Regression | 0.301 | 0.561 | 0.153 | |

> ✔️ **목표 달성 여부 최종 평가**
> - 이탈 패턴 탐색: ✅ 완료
> - ML/DL 비교 학습: ✅ 완료
> - Recall 최대화: ✅ 수치 달성 — 단, ROC-AUC 0.621은 데이터 한계로 인한 상한선
> - 범용 파이프라인: ✅ 구조 설계 완료 — 다른 서비스 적용 시 피처 컬럼 재정의 필요

---

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
      <td>클래스 불균형 문제를 단순 SMOTE 하나로 해결하려 했다가 XGBoost/LightGBM에서 Recall이 0에 가까워지는 걸 보고, 데이터와 모델의 특성을 함께 이해해야 한다는 것을 배웠다.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>권민제</strong></td>
      <td></td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>김규호</strong></td>
      <td style="text-align: center;">-</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>김정현</strong></td>
      <td></td>
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




```


