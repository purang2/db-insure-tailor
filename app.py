import streamlit as st
import openai
from dotenv import load_dotenv
import os
from metadata import metadata

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_prompt(age_group, job, household, region):
    age_data = metadata["A"][age_group]
    job_data = metadata["B"][job]
    household_data = metadata["C"][household]
    region_data = metadata["D"][region]
    
    prompt = f"""
    고객 프로필:
    - 연령대: {age_group} (키워드: {', '.join(age_data['키워드'])})
    - 직업: {job} (특성: {', '.join(job_data['특성'])})
    - 가구 형태: {household} (특성: {', '.join(household_data['특성'])})
    - 거주 지역: {region} (특성: {', '.join(region_data['특성'])})

    위 고객 프로필을 바탕으로, 다음 사항을 고려하여 보험 관련 문자 메시지 카드뉴스를 작성해주세요:
    1. 고객의 연령대별 관심사인 {', '.join(age_data['관심사'])}를 반영하세요.
    2. {job}으로서의 니즈인 {', '.join(job_data['니즈'])}를 고려하세요.
    3. {household} 가구의 니즈인 {', '.join(household_data['니즈'])}에 맞춰주세요.
    4. {region} 지역의 특성을 반영하여 {', '.join(region_data['관심사'])}와 관련된 내용을 포함하세요.
    5. 보험사 특유의 딱딱한 어조를 피하고, 친근하고 자연스러운 톤으로 작성해주세요.
    6. 카드뉴스 형식에 맞게 간결하고 시각적으로 표현할 수 있는 내용으로 구성해주세요.
    7. 고객이 자연스럽게 추가 정보나 상담을 요청할 수 있도록 유도하는 내용을 포함해주세요.

    카드뉴스 구성:
    1. 흥미로운 제목
    2. 3-4개의 주요 포인트
    3. 관련 이미지나 아이콘 제안
    4. 행동 유도 문구(CTA)
    """
    
    return prompt

def generate_card_news(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "당신은 보험 회사의 마케팅 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message['content']

st.title('맞춤형 보험 카드뉴스 생성기')

age_group = st.selectbox('연령대', list(metadata["A"].keys()))
job = st.selectbox('직업', list(metadata["B"].keys()))
household = st.selectbox('가구 형태', list(metadata["C"].keys()))
region = st.selectbox('거주 지역', list(metadata["D"].keys()))

if st.button('카드뉴스 생성'):
    prompt = generate_prompt(age_group, job, household, region)
    with st.spinner('카드뉴스를 생성 중입니다...'):
        card_news = generate_card_news(prompt)
    st.subheader('생성된 카드뉴스')
    st.write(card_news)
    
    st.subheader('사용된 프롬프트')
    st.text(prompt)