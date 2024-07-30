metadata = {
    "A": {  # 연령대
        "20대": {
            "키워드": ["자기계발", "취업", "연애", "SNS", "트렌드", "여행"],
            "관심사": ["커리어 시작", "인간관계", "자아 정체성", "새로운 경험"],
            "재정_상태": ["학자금 대출", "초기 자산 형성", "제한된 예산"],
            "라이프스타일": ["활동적", "디지털 네이티브", "공유 경제 선호"],
            "건강_관심사": ["다이어트", "피트니스", "정신 건강"]
        },
        "30대": {
            "키워드": ["결혼", "육아", "주택마련", "경력 발전", "일-삶 균형"],
            "관심사": ["가정 형성", "자녀 교육", "재테크", "건강관리"],
            "재정_상태": ["대출 상환", "자산 증식", "보험 needs 증가"],
            "라이프스타일": ["가족 중심", "안정 추구", "편의성 중시"],
            "건강_관심사": ["스트레스 관리", "가족 건강", "만성질환 예방"]
        },
        "40대": {
            "키워드": ["자녀교육", "노후준비", "건강관리", "부모 부양"],
            "관심사": ["자녀 성공", "경력 안정", "재무 계획", "건강 유지"],
            "재정_상태": ["자산 관리", "교육비 부담", "노후 대비 시작"],
            "라이프스타일": ["책임감 증가", "안정 지향", "품질 중시"],
            "건강_관심사": ["정기 검진", "성인병 예방", "체력 유지"]
        },
        "50대": {
            "키워드": ["은퇴 준비", "건강 관리", "자기 돌봄", "새로운 취미"],
            "관심사": ["노후 생활", "건강 유지", "자녀 독립", "인생 2막"],
            "재정_상태": ["은퇴 자금 확보", "자산 재분배", "의료비 증가"],
            "라이프스타일": ["여유 추구", "건강 중시", "사회활동 참여"],
            "건강_관심사": ["만성질환 관리", "갱년기 증상", "영양 관리"]
        },
        "60대 이상": {
            "키워드": ["건강한 노후", "여가 활동", "사회적 관계", "손주 돌봄"],
            "관심사": ["활기찬 노년", "가족과의 시간", "의료 서비스"],
            "재정_상태": ["연금 수입", "의료비 지출 증가", "자산 관리"],
            "라이프스타일": ["여유로운 일상", "건강 관리 중심", "봉사활동"],
            "건강_관심사": ["노화 관련 질환", "치매 예방", "일상 생활 유지능력"]
        }
    },
    "B": {  # 직업군
        "학생": {
            "특성": ["시간 유연성", "제한된 예산", "학업 스트레스"],
            "니즈": ["학자금 관리", "미래 설계", "건강한 학업 생활"],
            "관심사": ["취업 준비", "자기 계발", "사회 경험"]
        },
        "직장인": {
            "특성": ["정기적 수입", "시간 제약", "경력 개발"],
            "니즈": ["일-삶 균형", "자산 관리", "스트레스 관리"],
            "관심사": ["승진", "재테크", "건강 관리"]
        },
        "자영업자": {
            "특성": ["불규칙한 수입", "높은 자율성", "사업 리스크"],
            "니즈": ["사업 안정화", "위험 관리", "효율적 시간 관리"],
            "관심사": ["세금 관리", "사업 확장", "건강 보험"]
        },
        "전문직": {
            "특성": ["높은 전문성", "상대적 고소득", "높은 책임감"],
            "니즈": ["전문성 유지", "자산 관리", "명성 관리"],
            "관심사": ["최신 기술/정보", "네트워킹", "프리미엄 서비스"]
        },
        "프리랜서": {
            "특성": ["유연한 근무", "불안정한 수입", "다양한 프로젝트"],
            "니즈": ["안정적 수입원", "시간 관리", "스킬 개발"],
            "관심사": ["네트워킹", "포트폴리오 관리", "건강 보험"]
        },
        "은퇴자": {
            "특성": ["여유 시간", "고정 수입", "건강 이슈"],
            "니즈": ["건강 관리", "소득 유지", "여가 활동"],
            "관심사": ["취미 생활", "가족 관계", "의료 서비스"]
        }
    },
    "C": {  # 가구 형태
        "1인 가구": {
            "특성": ["독립적 생활", "의사결정 자유", "외로움"],
            "니즈": ["효율적 생활", "안전", "사회적 연결"],
            "관심사": ["간편식", "홈 케어", "반려동물"]
        },
        "커플 (무자녀)": {
            "특성": ["자유로운 생활", "이중 소득", "미래 계획"],
            "니즈": ["여가 활동", "자산 관리", "관계 유지"],
            "관심사": ["여행", "취미 공유", "주택 마련"]
        },
        "핵가족 (부모+자녀)": {
            "특성": ["육아 중심", "높은 지출", "시간 부족"],
            "니즈": ["자녀 교육", "가족 건강", "주거 안정"],
            "관심사": ["학군", "가족 보험", "가족 여가"]
        },
        "대가족 (조부모 포함)": {
            "특성": ["세대 간 교류", "복잡한 가족 역학", "전통 중시"],
            "니즈": ["세대 간 소통", "노인 돌봄", "공간 활용"],
            "관심사": ["가족 건강", "세대 통합 활동", "가족 행사"]
        }
    },
    "D": {  # 지역
    "서울": {
        "특성": ["대도시", "높은 생활비", "문화적 다양성"],
        "니즈": ["편리한 도시 생활", "경쟁력 있는 교육", "안전한 주거환경"],
        "관심사": ["부동산", "직장/학군", "도시 문화"],
        "주요_산업": ["금융", "IT", "서비스업"]
    },
    "경기": {
        "특성": ["수도권", "주거 중심", "산업 단지"],
        "니즈": ["쾌적한 주거환경", "편리한 교통", "양질의 교육"],
        "관심사": ["교육", "출퇴근", "신도시 개발"],
        "주요_산업": ["제조업", "물류", "바이오"]
    },
    "인천": {
        "특성": ["국제공항", "항만 도시", "경제자유구역"],
        "니즈": ["국제적 생활 인프라", "해양 레저 시설", "물류 환경 개선"],
        "관심사": ["물류", "해양 레저", "국제 비즈니스"],
        "주요_산업": ["항공", "해운", "관광"]
    },
    "부산": {
        "특성": ["해양도시", "제2의 도시", "국제 행사"],
        "니즈": ["해양 관련 인프라", "국제 행사 지원", "관광 산업 발전"],
        "관심사": ["해변 활동", "영화 축제", "국제 무역"],
        "주요_산업": ["해운", "관광", "영화"]
    },
    "울산": {
        "특성": ["공업 도시", "자동차 산업", "조선 산업"],
        "니즈": ["산업 안전", "환경 보호", "근로자 복지"],
        "관심사": ["산업 안전", "환경", "레저 활동"],
        "주요_산업": ["자동차", "조선", "석유화학"]
    },
    "대전": {
        "특성": ["과학 기술 중심", "교육 도시", "행정 중심복합도시 인접"],
        "니즈": ["연구 개발 지원", "우수 교육 환경", "정주 여건 개선"],
        "관심사": ["연구 개발", "교육", "정부 정책"],
        "주요_산업": ["R&D", "교육", "공공행정"]
    },
    "대구": {
        "특성": ["섬유 패션 도시", "더운 날씨", "의료 중심지"],
        "니즈": ["패션 산업 지원", "폭염 대비 시설", "의료 서비스 향상"],
        "관심사": ["패션 산업", "건강 관리", "문화 예술"],
        "주요_산업": ["섬유", "의료", "기계"]
    },
    "광주": {
        "특성": ["예술 문화 도시", "민주화 운동의 역사", "자동차 산업"],
        "니즈": ["문화 예술 지원", "역사 보존", "산업 다각화"],
        "관심사": ["문화 예술", "지역 축제", "자동차 산업"],
        "주요_산업": ["자동차", "문화콘텐츠", "신재생에너지"]
    },
    "제주": {
        "특성": ["관광지", "섬 지역", "특별자치도"],
        "니즈": ["관광 인프라 개선", "환경 보존", "지역 경제 활성화"],
        "관심사": ["관광 산업", "환경 보존", "해양 활동"],
        "주요_산업": ["관광", "1차산업", "신재생에너지"]
    },
    "강원": {
        "특성": ["산악 지역", "관광지", "동계 스포츠"],
        "니즈": ["관광 산업 발전", "농업 지원", "레저 스포츠 인프라"],
        "관심사": ["레저 스포츠", "농업", "관광"],
        "주요_산업": ["관광", "농업", "광업"]
    }
},
"E": {  # 시나리오
    "휴가철 운전": {
        "설명": "휴가 시즌 장거리 운전과 관련된 연령대, 고객 프로필 별 발생 가능한 리스크"
    }
    # 추후 다른 시나리오를 여기에 쉽게 추가할 수 있습니다.
}
}
