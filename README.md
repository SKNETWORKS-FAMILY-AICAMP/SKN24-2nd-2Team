# 🚀 SK네트웍스 Family AI 캠프 24기 2차 프로젝트 
## 주제: 💘 OkCupid 데이팅앱 유저 데이터를 활용한 가입 고객 이탈 예측 (Churn Prediction)


---

## 1. 2팀 소개 - 
- **팀명**: SKN24-2nd-2Team (Cupid Rescue)
- **멤버**:
  
<table>
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 20%;">
    <col style="width: 20%;">
    <col style="width: 20%;">
    <col style="width: 20%;">
  </colgroup>
  <tbody>
    <tr style="font-weight: bold;">
      <td style="text-align: center;">고아라</td>
      <td style="text-align: center;">권민제</td>
      <td style="text-align: center;">김규호</td>
      <td style="text-align: center;">김정현</td>
      <td style="text-align: center;">최현진</td>
    </tr>
    <tr>
      <td style="text-align: center;">
        <a href="https://github.com/Akoh-0909"><img src="https://img.shields.io/badge/AKOH--0909-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub - Akoh-0909"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/min3802"><img src="https://img.shields.io/badge/min3802-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub - min3802"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/kyu5KIm"><img src="https://img.shields.io/badge/kyu5KIm-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub - kyu5KIm"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/Jeich-16"><img src="https://img.shields.io/badge/Jeich--16-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub - Jeich-16"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/lifeisgoodlg"><img src="https://img.shields.io/badge/lifeisgoodlg-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub - lifeisgoodlg"></a>
      </td>
    </tr>
  </tbody>
</table>


## 2. 프로젝트 개요
- **프로젝트 명**: 💘 OkCupid 데이팅앱 유저 데이터를 활용한 가입 고객 이탈 예측 (Churn Prediction)
- **프로젝트 소개**: 데이팅 앱 OkCupid 유저들의 가치관과 활동 데이터를 분석하여 이탈 가능성을 예측.
- **필요성**: 
- **목표**: 이진 분류 모델을 통해 이탈 고위험군 유저를 90% 이상의 정밀도로 식별

### 데이터셋 기본 정보
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


## 4. WBS (Work Breakdown Structure)


## 5. 데이터 전처리 결과서 (EDA)
### 모델 별 전처리 시 확인 포인트

범주형 object 타입 컬럼이 많아 전처리 기준 확립


### 결측치

(결측치 사진)
(height 결측치)

### 이상치

(age 이상치, height 이상치)

### 전처리

age(나이) : 나이대 별

status(연애중) : 연애를 하는 중, 안하는 중

orientation(성적지향) :  이성애자, 동성애자

body_type(체형) : 마름, 보통, 건강, 통통

education(학력) : 석사이상(4), 학사졸업(3), 학사재학(2), 고등이하(1), 그외(0)

last_online(마지막 접속) : 시간별 데이터를 일별 데이터 분류 -> 이탈율 계산 

religion(종교) : 종교가 있다(1), 없다(0)

diet(식단) : 유연함(0), 중간(1), 엄격함(5)

drinks(음주 빈도) : 안마신다(0), 적당히 마신다(1), 많이마신다(5)

drugs(약물 사용) : 안한다(0), 가끔한다(1), 자주한다(5)

smokes(흡연 여부) : 흡연을 안한다(0), 조금한다(1), 자주 한다(5)

job(직업) : 연봉 기준으로 0~4로 분류

response rate(답변성실도) : 전체의 빈칸이 적은 정도

total_essay_len(에세이 총 글자) : 에세이의 총 글자 수 합산

essay_answered_count(작성한 에세이 질문 개수) : 작성한 essay 질문 개수

niche_score(매칭 시장 내 배타성 지수) : smokes + drinks + drugs + diet 매칭 마찰력 누적
-> 음주 기준 0과 1의 지표는 성향차이라 판단 하지만 2의 지표는 성향차이가 아닐것이라 판단

churn(이탈) : 이탈(1), 잔류(0)


### 최종 데이터 구조
| 컬럼명                                              | 설명                         | 데이터타입 |
|-----------------------------------------------------|------------------------------|------------|
| sex                                                 | 성별                         | int8       |
| orientation                                         | 성적지향 여부                | int8       |
| diet                                                | 식단                         | int64      |
| drugs                                               | 약물 사용 여부               | int64      |
| education                                           | 학력 수준                    | float64    |
| height                                              | 키 (inch)                    | float64    |
| body_type_average                                   | 평균 체형 여부               | bool       |
| body_type_curvy                                     | 통통한 체형 여부             | bool       |
| body_type_fit                                       | 건강/탄탄 체형 여부          | bool       |
| body_type_slim                                      | 마른 체형 여부               | bool       |
| smokes                                              | 흡연자 여부                  | bool       |
| drinks_heavy                                        | 과음 여부                    | bool       |
| drinks_moderate                                     | 적당한 음주 여부             | bool       |
| drinks_no_drinks                                    | 비음주 여부                  | bool       |
| job_score                                           | 연봉기준  0~4                | float64    |
| religion_religion                                   | 종교 여부                    | bool       |
| status_encoding                                     | 연애 상태 인코딩값           | int64      |
| age_group                                           | 연령대 그룹                  | int64      |
| response rate                                       | 답변 성실도                  | float64    |
| total_essay_len                                     | 에세이 전체 글자 수 합산     | int64      |
| essay_answered_count                                | 작성한 에세이 질문 개수      | int64      |
| niche_score                                         | 매칭 시장 내 배타성지수      | float64    |
| churn                                               | 고객 이탈                    | int64     |



## 6. 인공지능 학습 결과서
| Model | Accuracy | F1-Score | 비고 |
|-------|----------|----------|------|


## 7. 수행결과 (시연)


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
      <td></td>
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
