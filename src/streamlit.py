import streamlit as st
import pandas as pd
import joblib


# 기본 설정
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load("../models/xgboost_model.joblib")

model = load_model()

if hasattr(model, "feature_names_in_"):
    feature_cols = list(model.feature_names_in_)
else:
    feature_cols = model.get_booster().feature_names



# 🔹 전처리 기준 매핑

SEX_MAP = {"여성": 0, "남성": 1}

ORIENTATION_MAP = {
    "이성애자": 0,
    "동성애자": 1,
    "양성애자": 1
}

STATUS_MAP = {
    "미혼": 0,
    "연애 중": 1,
    "기혼": 2
}

RELIGION_MAP = {
    "무종교": 0,
    "종교 있음": 1
}

DRINKS_MAP = {"안함": 0, "보통": 1, "과음": 5}

SMOKES_MAP = {"비흡연": 0, "흡연": 1}

DRUG_MAP = {
    "안함": 0,
    "가끔": 1,
    "자주": 2
}

DIET_MAP = {
    "유연함": 0,
    "중간": 1,
    "엄격함": 5
}

JOB_SCORE_MAP = {
    # 1
    "science / tech / engineering": 1,
    "computer / hardware / software": 1,

    # 2
    "sales / marketing / biz dev": 2,
    "executive / management": 2,
    "banking / financial / real estate": 2,

    # 3
    "artistic / musical / writer": 3,
    "entertainment / media": 3,

    # 4
    "education / academia": 4,
    "medicine / health": 4,
    "political / government": 4,
    "law / legal services": 4,

    # 5
    "hospitality / travel": 5,
    "construction / craftsmanship": 5,
    "clerical / administrative": 5,
    "transportation": 5,
    "military": 5,

    # 6
    "other": 6,
    "unemployed": 6,
    "retired": 6,
    "rather not say": 6,
    "student": 6
}


# 헤더
st.markdown("""
<h1 style='text-align:center;'>Customer Churn Prediction Simulator</h1>
<p style='text-align:center;color:gray;'>
프로필과 활동 수준을 기반으로 이탈 확률을 예측합니다.
</p>
""", unsafe_allow_html=True)

st.divider()

# 🧍 기본 프로필
st.markdown("## 🧍 기본 프로필")

col1, col2, col3 = st.columns(3)

with col1:
    sex = st.selectbox("성별", list(SEX_MAP.keys()))
    age = st.slider("나이", 18, 70, 25)
    height = st.slider("키 (inch)", 55, 85, 65)
    body_type = st.selectbox("체형", ["average", "curvy", "fit", "slim"])

with col2:
    orientation = st.selectbox("성적 지향", list(ORIENTATION_MAP.keys()))
    status = st.selectbox("연애 상태", list(STATUS_MAP.keys()))
    religion = st.selectbox("종교 여부", list(RELIGION_MAP.keys()))
    job_label = st.selectbox("직업군", list(JOB_SCORE_MAP.keys()))

with col3:
    drinks_label = st.selectbox("음주 수준", list(DRINKS_MAP.keys()))
    smokes_label = st.selectbox("흡연 여부", list(SMOKES_MAP.keys()))
    drugs_label = st.selectbox("약물 사용", list(DRUG_MAP.keys()))
    diet_label = st.selectbox("식단 엄격도", list(DIET_MAP.keys()))

st.divider()


# 📈 활동 수준
st.markdown("## 📈 활동 수준")

col4, col5 = st.columns(2)

with col4:
    response_rate_ui = st.slider("답변 성실도 (%)", 0, 100, 50)
    essay_len_ui = st.slider("에세이 작성 길이 (0~2000)", 0, 2000, 800)

with col5:
    essay_count_ui = st.slider("작성한 에세이 개수", 0, 10, 3)

st.divider()


# 🔮 예측
if st.button("🔮 예측하기", use_container_width=True):

    input_dict = {col: 0 for col in feature_cols}

    # 기본 인코딩
    input_dict["sex"] = SEX_MAP[sex]
    input_dict["age"] = age
    input_dict["height"] = height
    input_dict["orientation_1"] = ORIENTATION_MAP[orientation]
    input_dict["status_encoding"] = STATUS_MAP[status]
    input_dict["religion_religion"] = RELIGION_MAP[religion]
    input_dict["drinks"] = DRINKS_MAP[drinks_label]
    input_dict["smokes"] = SMOKES_MAP[smokes_label]
    input_dict["drugs"] = DRUG_MAP[drugs_label]
    input_dict["diet"] = DIET_MAP[diet_label]
    input_dict["job_score"] = JOB_SCORE_MAP[job_label]

    # 🔥 niche_score 자동 계산 (전처리와 동일)
    input_dict["niche_score"] = (
        input_dict["smokes"] +
        input_dict["drinks"] +
        input_dict["drugs"] +
        input_dict["diet"]
    )

    # 체형 원핫
    if body_type == "average":
        input_dict["body_type_average"] = True
    elif body_type == "curvy":
        input_dict["body_type_curvy"] = True
    elif body_type == "fit":
        input_dict["body_type_fit"] = True
    elif body_type == "slim":
        input_dict["body_type_slim"] = True

    # 직접 입력받는 행동 지표
    input_dict["Response rate"] = response_rate_ui / 100
    input_dict["total_essay_len"] = essay_len_ui
    input_dict["essay_answered_count"] = essay_count_ui

    # feature 순서 정렬
    input_df = pd.DataFrame([input_dict])
    input_df = input_df[feature_cols]

    prediction = model.predict(input_df)
    proba = model.predict_proba(input_df)
    churn_prob = float(proba[0][1])

    st.markdown("## 📊 예측 결과")
    st.progress(churn_prob)
    st.metric("이탈 확률", f"{churn_prob*100:.2f}%")

    if prediction[0] == 1:
        st.error("⚠ 이탈 가능성 높음")
    else:
        st.success("✅ 이탈 가능성 낮음")