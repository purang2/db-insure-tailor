import streamlit as st
import openai
from dotenv import load_dotenv
import os
from metadata import metadata

# Load environment variables
load_dotenv()

# Set up OpenAI API key
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["openai"]

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
    prompt = f"""
    def generate_prompt(age_group, job, household, region):
    age_data = metadata["A"][age_group]
    job_data = metadata["B"][job]
    household_data = metadata["C"][household]
    region_data = metadata["D"][region]
    """
    
    prompt = f"""
    당신은 ABC손해보험의 UX 라이팅 전문가입니다. 다음 고객 프로필에 맞는 보험 관련 문자 메시지 카드뉴스를 작성해주세요:

    고객 프로필:
    - 연령대: {age_group} (키워드: {', '.join(age_data['키워드'])})
    - 직업: {job} (특성: {', '.join(job_data['특성'])})
    - 가구 형태: {household} (특성: {', '.join(household_data['특성'])})
    - 거주 지역: {region} (특성: {', '.join(region_data['특성'])})

    ABC손해보험의 UX 라이팅 시스템을 따라 다음 원칙을 준수하여 작성해주세요:

    1. Clear (명확한): 복잡한 보험 용어를 피하고, 고객이 쉽게 이해할 수 있는 언어를 사용하세요.
    2. Concise (간결한): 핵심 메시지를 간결하게 전달하되, 필요한 정보는 충분히 제공하세요.
    3. Casual (친근한): 딱딱한 보험 회사 톤을 벗어나 친근하고 대화하는 듯한 톤을 사용하세요.
    4. Respect (존중하는): 고객의 상황을 존중하고, 선택권을 주는 표현을 사용하세요.
    5. Emotional (공감하는): 고객의 니즈와 감정에 공감하는 메시지를 포함하세요.

    추가 지침:
    - Predictable hint: 다음 단계나 행동을 예측할 수 있는 힌트를 제공하세요.
    - Focus on key message: 이 고객에게 가장 중요한 보험 관련 정보나 혜택을 선별하여 전달하세요.
    - Easy to speak: 대화체로 자연스럽게 읽히는 문장을 사용하세요.
    - Suggest than force: 강요하지 않고 고객이 스스로 선택할 수 있도록 제안하는 톤을 사용하세요.
    - Find hidden emotion: 보험 정보 뒤에 숨은 고객의 안전, 안정, 보호에 대한 감정을 고려하세요.

    카드뉴스 구성:
    1. 주의를 끄는 제목 (15단어 이내)
    2. 도입부: 고객의 상황이나 니즈에 공감하는 1-2문장 (30단어 이내)
    3. 핵심 내용: 
       - 이 고객에게 적합한 보험 상품이나 서비스 소개 (2-3개 항목, 각 20단어 이내)
       - 각 항목의 주요 혜택이나 특징 (각 15단어 이내)
    4. 고객에게 제공하는 가치나 해결할 수 있는 문제 설명 (25단어 이내)
    5. 행동 유도 문구(CTA): 다음 단계를 안내하는 문장 (20단어 이내)

    전체 카드뉴스 내용은 200단어를 넘지 않도록 해주세요. 
    위 지침을 따라 고객 프로필에 맞는 구체적이면서도 간결한 카드뉴스를 생성해주세요.
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
    
    #st.subheader('사용된 프롬프트')
    #st.text(prompt)
