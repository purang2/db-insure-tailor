import streamlit as st
import openai
from dotenv import load_dotenv
import os
from metadata import metadata
import streamlit as st
from PIL import Image

# 이미지 파일 로드
favicon = Image.open('images/favicon.png')

st.set_page_config(
    page_title="DB손해보험의 고객맞춤형 카드뉴스 문구 생성 AI",
    page_icon=favicon,
)



# Load environment variables
load_dotenv()

# Set up OpenAI API key
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["openai"]
def generate_prompt(age_group, job, household, region, scenario):
    age_data = metadata["A"][age_group]
    job_data = metadata["B"][job]
    household_data = metadata["C"][household]
    region_data = metadata["D"][region]
    scenario_data = metadata["E"][scenario]
    
    # 연령대별 프롬프트 기본 구조 가져오기
    age_specific_prompt = age_prompts[age_group]
    

    # 프롬프트 구성
    prompt = f"""
    당신은 ABC손해보험의 광고 카피라이팅 전문가입니다. 고객의 마음을 울리는 스토리텔링을 지향해야 합니다. 다음 고객 프로필과 특정 시나리오에 맞는 보험 관련 문자 메시지 카드뉴스를 작성해주세요:

    **고객 프로필:**
    - **연령대:** {age_group} (키워드: {', '.join(age_data.get('키워드', []))})
    - **직업:** {job} (특성: {', '.join(job_data.get('특성', []))})
    - **가구 형태:** {household} (특성: {', '.join(household_data.get('특성', []))})
    - **거주 지역:** {region}
      - **특성:** {', '.join(region_data.get('특성', []))}
      - **니즈:** {', '.join(region_data.get('니즈', []))}
      - **관심사:** {', '.join(region_data.get('관심사', []))}
      - **주요 산업:** {', '.join(region_data.get('주요_산업', []))}

    **특정 시나리오:** {scenario}
    - **설명:** {scenario_data.get('설명', '설명이 없습니다.')}

    카드뉴스 작성 시 주의사항:
    1. **직업 관련 니즈:** {job}의 니즈를 반영하세요. 예: {', '.join(job_data.get('니즈', []))}
    2. **가구 형태 관련 니즈:** {household}의 특성에 맞춰 메시지를 구성하세요. 예: {', '.join(household_data.get('니즈', []))}
    3. **지역 특성:** {region}의 관심사와 지역 특성을 반영하세요. 예: {', '.join(region_data.get('관심사', []))}
    4. **보험 아이템은 간접적 언급:** 직접적인 보험 권유 대신, 잠재적 리스크에 대한 정보 제공에 중점을 둡니다.
    5. **간결하고 명확한 표현:** 카드뉴스는 모바일 환경에서 쉽게 읽힐 수 있도록 합니다.

    {age_specific_prompt}

    **ABC손해보험의 UX 라이팅 원칙:**
    - **명확함 (Clear):** 고객이 쉽게 이해할 수 있는 언어 사용
    - **간결함 (Concise):** 핵심 메시지를 간결하게 전달하되, 필요한 정보는 충분히 제공
    - **친근함 (Casual):** 딱딱한 보험 회사 톤을 벗어나 친근하고 대화하는 듯한 톤 사용
    - **존중 (Respect):** 고객의 상황을 존중하고, 선택권을 주는 표현 사용
    - **공감 (Emotional):** 고객의 니즈와 감정에 공감하는 메시지를 포함

    **카드뉴스 구성 (모바일 환경에 특화):**
    - 주의를 끄는 제목 (10단어 이내)
    - 고객의 상황에 공감하는 따뜻한 메시지 (10단어 이내)
    - 실용적인 팁이나 조언 제공 (10단어 이내)
    - 희망적 미래와 함께하는 든든한 지원 약속 (10단어 이내)
    - 다음 단계를 위한 간결한 행동 유도 문구 (5단어 이내)

    전체 내용은 50단어 이내로, 친근하고 따뜻하되 간결하게 작성해주세요. 카드뉴스의 제목은 작성하지 말고, 카드뉴스 최종 텍스트만 생성해주세요.
    """

    return prompt

# age_prompts를 더 개인화하고, 중복된 텍스트를 제거하여 간결하게 구성
age_prompts = {
    "20대": """
    당신은 ABC손해보험의 따뜻하고 지혜로운 친구입니다. 20대의 삶에 깊이 공감하며, 유용한 정보와 따뜻한 응원을 담아 간결한 메시지를 작성해주세요.
    """,
    "30대": """
    당신은 ABC손해보험의 카피라이팅 전문가입니다. 30대의 삶을 이해하고, 관련된 보험 정보를 친근하게 전달해주세요.
    """,
    "40대": """
    당신은 ABC손해보험의 카피라이팅 전문가입니다. 40대의 관심사를 반영하여, 고객의 고민과 니즈를 공감하며 작성하세요.
    """,
    "50대": """
    당신은 ABC손해보험의 카피라이팅 전문가입니다. 50대 고객에게 노후 준비와 건강 관리에 관한 메시지를 전달하세요.
    """,
    "60대 이상": """
    당신은 ABC손해보험의 카피라이팅 전문가입니다. 60대 이상 고객에게 건강한 노후와 안정된 생활을 위한 메시지를 전해주세요.
    """
}





def generate_card_news(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": (
            "당신은 ABC손해보험의 광고 카피라이팅 전문가입니다. "
            "카피라이팅에서 중요한 것은 고객의 관심을 끌고 메시지를 명확하게 전달하는 것입니다. "
            "당신의 목표는 복잡한 표현보다는 단순하고 강력한 포인트를 통해 고객의 마음에 깊은 인상을 남기는 것입니다. "
            "각 고객의 프로필과 상황에 맞춰 적절한 감정과 정보를 전달하여, "
            "고객이 ABC손해보험을 선택하는 데 도움이 되는 명확하고 공감 가는 메시지를 작성하세요."
        )},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message['content']

st.title('고객맞춤형 카드뉴스 문구 생성 AI')

age_group = st.selectbox('연령대', list(metadata["A"].keys()))
job = st.selectbox('직업', list(metadata["B"].keys()))
household = st.selectbox('가구 형태', list(metadata["C"].keys()))
region = st.selectbox('거주 지역', list(metadata["D"].keys()))

# 시나리오 선택 옵션 추가
scenario = st.selectbox('시나리오', list(metadata["E"].keys()))
#scenario = "휴가철 운전"
if st.button('카드뉴스 생성'):
    prompt = generate_prompt(age_group, job, household, region, scenario)
    with st.spinner('카드뉴스를 생성 중입니다...'):
        card_news = generate_card_news(prompt)
    st.subheader('생성된 카드뉴스')
    st.write(card_news)
    
    #st.subheader('사용된 프롬프트')
    #st.text(prompt)
