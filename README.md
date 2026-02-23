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
        <a href="https://github.com/Akoh-0909"><img src="" alt="GitHub - Akoh-0909"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/min3802"><img src="" alt="GitHub - min3802"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/kyu5KIm"><img src="" alt="GitHub - kyu5KIm"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/Jeich-16"><img src="" alt="GitHub - Jeich-16"></a>
      </td>
      <td style="text-align: center;">
        <a href="https://github.com/lifeisgoodlg"><img src="" alt="GitHub - lifeisgoodlg"></a>
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
| diet         | ❌        | 식단 성향       | object     |
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
| essay0       | ❌        | 자기소개        | object     |
| essay1       | ❌        | 인생 방향       | object     |
| essay2       | ❌        | 잘하는 것       | object     |
| essay3       | ❌        | 첫인상          | object     |
| essay4       | ❌        | 취향            | object     |
| essay5       | ❌        | 필수 요소       | object     |
| essay6       | ❌        | 많이 생각하는 것| object     |
| essay7       | ❌        | 금요일 밤       | object     |
| essay8       | ❌        | 가장 사적인 고백| object     |
| essay9       | ❌        | 메시지 조건     | object     |

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

drinks(음주 빈도) : 안마신다, 적당히 마신다, 많이마신다

drugs(약물 사용) : 안한다, 가끔한다, 자주한다

education(학력) : 석사이상, 학사졸업, 학사재학, 고등이하, 그외

last_online(마지막 접속) : 시간별 데이터를 일별 데이터 분류 -> 이탈율 계산 

religion(종교) : 종교가 있다, 없다

smokes(흡연 여부) : 흡연을 안한다, 조금한다, 자주 한다

job(직업) : 기술측면, 비지니스, 경영, 금융 측면, 미디어 측면, 
공공 교육 의료 측면, 서비스 측면, 그 이외

### 최종 데이터 구조
| 컬럼명                                              | 설명                         | 데이터타입 |
|-----------------------------------------------------|------------------------------|------------|
| sex                                                 | 성별                         | int8       |
| orientation                                         | 성적지향 여부                 | int8       |
| drugs                                               | 약물 사용 여부                | int64      |
| education                                           | 학력 수준                    | float64    |
| height                                              | 키 (inch)                   | float64   |
| body_type_average                                   | 평균 체형 여부               | bool       |
| body_type_curvy                                     | 통통한 체형 여부             | bool       |
| body_type_fit                                       | 건강/탄탄 체형 여부          | bool       |
| body_type_slim                                      | 마른 체형 여부               | bool       |
| smokes_smoke                                        | 흡연자 여부                  | bool       |
| smokes_sometime_smoke                               | 가끔 흡연 여부               | bool       |
| drinks_heavy                                        | 과음 여부                    | bool       |
| drinks_moderate                                     | 적당한 음주 여부             | bool       |
| drinks_no_drinks                                    | 비음주 여부                  | bool       |
| job_encoding_Creative / Media / Entertainment       | 직업군 (크리에이티브/미디어)  | bool       |
| job_encoding_No jobs/No reply                       | 직업 없음/무응답             | bool       |
| job_encoding_Public / Education / Healthcare / Legal| 공공/교육/의료/법률 직군     | bool       |
| job_encoding_STEM/Tech                              | STEM/기술 직군               | bool       |
| job_encoding_Service / Manual / Admin / Transport   | 서비스/사무/운송 직군         | bool       |
| religion_no_religion                                | 무종교 여부                  | bool       |
| religion_religion                                   | 종교 있음 여부               | bool       |
| status_encoding                                     | 연애 상태 인코딩값           | int64      |
| age_group                                           | 연령대 그룹                  | int64      |



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
