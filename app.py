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
    page_title="AI 기반 고객맞춤형 카드뉴스 메시지 어시스턴트",
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
    
    age_specific_prompt = age_prompts[age_group]
    
    prompt = f"""
    당신은 ABC손해보험의 AI 어시스턴트입니다. {age_group}의 삶에 깊이 공감하며, 유용하고 균형 잡힌 정보를 제공하는 메시지를 작성해주세요. 이 메시지는 AI에 의해 생성되었음을 명시해야 합니다.

    **고객 프로필:**
    - **연령대:** {age_group} (키워드: {', '.join(age_data.get('키워드', []))})
    - **직업:** {job} (특성: {', '.join(job_data.get('특성', []))})
    - **가구 형태:** {household} (특성: {', '.join(household_data.get('특성', []))})
    - **거주 지역:** {region} (특성: {', '.join(region_data.get('특성', []))})
    - **시나리오:** {scenario}
      - 설명: {scenario_data.get('설명', '설명 없음')}
      - 세부 시나리오: {', '.join(scenario_data.get('세부_시나리오', {}).keys())}
      - 연령대별/직업군별 팁: {', '.join(scenario_data.get('연령대별_팁', scenario_data.get('직업군별_팁', {})).keys())}
      - 통계: {scenario_data.get('통계', '통계 정보 없음')}
      - 관련 보험: {scenario_data.get('관련_보험', '관련 보험 정보 없음')}

    작성 시 다음 사항을 고려해주세요:
    1. 제공된 통계 데이터로 시작하여 관심을 끌어주세요.
    2. {age_group}의 상황과 {scenario}에 대해 깊이 공감하되, 과도한 불안감을 조성하지 않도록 주의하세요.
    3. {job}과(와) {household}의 특성을 고려한 실용적인 팁을 제공하세요. 다양한 문화적 배경을 고려하세요.
    4. {region}의 특성과 주요 산업을 반영한 지역 맞춤 정보를 포함하세요.
    5. 선택된 세부 시나리오에 대한 구체적인 조언을 제공하세요.
    6. 해당 연령대나 직업군에 맞는 특화된 팁을 포함하세요.
    7. {scenario}와 관련된 안전과 대비의 중요성을 언급하되, 보험 외의 대안적 해결책도 함께 제시하세요.
    8. {age_group}의 디지털 친화도와 금융 이해도를 고려한 적절한 용어를 사용하세요.
    9. 관련 보험 상품을 자연스럽게 소개하되, 직접적인 판매 권유는 피하세요.
    10. 개인정보 보호와 관련하여, 이 메시지가 고객의 동의하에 제공되며 언제든 수신 거부할 수 있음을 명시하세요.


    카드뉴스 구성:
    1. 통계 데이터와 공감 메시지 결합 (12단어 이내)
    2. 고객 프로필을 고려한 실용적 조언과 팁 (최대 40단어)

    전체 내용은 이모티콘을 포함하여 60단어 이내로 작성하세요. 
    관련 해시태그 2-3개를 추가하고, AI 생성 콘텐츠임을 간단히 명시하세요. 
    반드시 고객에게 바로 보낼 수 있는 정도의 메시지 포맷으로 제공해주세요. 
    
    {age_specific_prompt}
    """
    return prompt

age_prompts = {
    "20대": "MZ세대의 언어와 최신 트렌드(예: 경험 중시, YOLO)를 반영하고, 이모티콘이나 해시태그를 적절히 활용하세요. 취업, 자기계발, 소셜미디어 활용 등의 관심사를 다루되, 경제적 불안정성에 대한 공감과 함께 긍정적인 미래 전망도 제시하세요.",
    
    "30대": "일과 삶의 균형, 가족에 대한 관심을 반영하고, 실용적이고 효율적인 정보를 제공하세요. 경력 발전, 육아, 재테크 등의 주제를 다루며, 미래에 대한 기대와 불안을 균형있게 다루세요. 다양한 가족 형태와 라이프스타일을 존중하는 표현을 사용하세요.",
    
    "40대": "자녀 교육과 노후 준비에 대한 관심을 반영하고, 건강 관리와 재무 계획에 대한 정보를 제공하세요. 부모 부양, 중년의 위기, 자기 재발견 등의 주제도 섬세하게 다루세요. 디지털 활용능력 향상에 대한 관심도 고려하되, 개인의 가치와 경험을 존중하는 메시지를 전달하세요.",
    
    "50대": "은퇴 준비와 건강 관리에 초점을 맞추고, 새로운 취미와 사회 공헌에 대한 관심을 반영하세요. 자녀의 독립, 부모 돌봄, 인생 2막 준비 등의 주제를 다루며, 경험을 통한 지혜를 공유하는 톤을 사용하세요. 다양한 은퇴 후 삶의 모습을 제시하고, 개인의 선택을 존중하는 메시지를 전달하세요.",
    
    "60대 이상": "건강한 노후와 가족과의 시간에 중점을 두고, 활기찬 노년을 위한 팁을 제공하세요. 디지털 기술 적응, 새로운 사회활동, 손주와의 관계 등을 다루되, 세대 간 지혜 전수의 중요성도 강조하세요. 존중과 독립성을 균형있게 표현하고, 다양한 노년의 모습을 긍정적으로 그려내세요."
}


def generate_card_news(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": (
            "당신은 ABC손해보험의 윤리적인 AI 카피라이팅 어시스턴트입니다. "
            "다음의 핵심 원칙을 준수하세요:\n"
            "1. 정확성과 투명성을 최우선으로 합니다.\n"
            "2. 다양성을 존중하고 포용적인 언어를 사용합니다.\n"
            "3. 고객의 자율성을 존중하고 균형 잡힌 정보를 제공합니다.\n"
            "4. 개인정보 보호와 데이터 사용에 대해 투명하게 소통합니다.\n"
            "사용자 프롬프트의 구체적인 지시사항을 따라 콘텐츠를 생성하세요."
        )},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    ai_generated_content = response.choices[0].message['content']

    disclaimer = ""
    #disclaimer = "\n\n[이 내용은 AI에 의해 생성되었으며, 개인의 상황에 따라 다를 수 있습니다. 중요한 결정에는 전문가와 상담하세요.]"
    
    return ai_generated_content + disclaimer
    
st.title('AI 기반 맞춤형 카드뉴스 메시지 어시스턴트')

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
