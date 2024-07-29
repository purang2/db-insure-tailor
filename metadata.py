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
    "D": {  # 지역 (예시로 몇 개만 포함)
        "서울": {
            "특성": ["높은 생활비", "빠른 생활 템포", "문화적 다양성"],
            "니즈": ["주거 안정", "교통 편의", "문화생활"],
            "관심사": ["부동산", "직장/학군", "도시 문화"]
        },
        "부산": {
            "특성": ["해양도시", "온화한 기후", "관광지"],
            "니즈": ["해양 레저", "지역 경제 활성화", "교통 개선"],
            "관심사": ["해변 활동", "지역 축제", "해산물"]
        },
        "대전": {
            "특성": ["과학 기술 중심", "교육 도시", "자연 환경"],
            "니즈": ["교육 인프라", "연구 개발 지원", "자연 친화적 생활"],
            "관심사": ["과학 기술", "교육", "등산/캠핑"]
        },
        # 여기에 다른 지역들 추가...
    }
}