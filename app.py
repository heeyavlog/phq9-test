import streamlit as st

def run_phq9_test():
    st.title('우울증 자가진단 테스트 (PHQ-9)')
    st.write('지난 2주간 다음과 같은 문제들로 인해서 얼마나 자주 방해를 받았습니까?')
    
    questions = [
        "일에 대한 흥미나 재미가 거의 없음",
        "기분이 가라앉거나, 우울하거나, 희망이 없음",
        "잠들기 어렵거나, 자주 깨거나, 혹은 너무 많이 잠",
        "피곤하다고 느끼거나 기운이 거의 없음",
        "식욕 저하 또는 과식",
        "자신을 부정적으로 봄",
        "집중하기 어려움",
        "다른 사람들이 알아챌 정도로 거동이나 말이 느림",
        "자해하고 싶은 생각"
    ]
    
    options = {
        "전혀 없음": 0,
        "며칠 동안": 1,
        "일주일 이상": 2,
        "거의 매일": 3
    }
    
    scores = []
    
    st.write('---')
    
    for i, question in enumerate(questions, 1):
        st.subheader(f'{i}. {question}')
        answer = st.radio(
            "빈도를 선택하세요:",
            options.keys(),
            key=f"q{i}"
        )
        scores.append(options[answer])
        st.write('---')
    
    if st.button('결과 확인하기'):
        total_score = sum(scores)
        st.subheader('검사 결과')
        st.write(f'총점: {total_score}점')
        
        if total_score <= 4:
            st.success('정상 범위입니다.')
        elif total_score <= 9:
            st.info('가벼운 우울감이 있습니다.')
        elif total_score <= 14:
            st.warning('중등도의 우울감이 있습니다. 전문가와 상담을 고려해보세요.')
        elif total_score <= 19:
            st.error('중증의 우울감이 있습니다. 전문가의 도움을 받아보시길 권장합니다.')
        else:
            st.error('심각한 우울감이 있습니다. 즉시 전문가의 도움을 받으시길 강력히 권장합니다.')
        
        st.write('---')
        st.write('주의: 이 테스트는 참고용이며, 정확한 진단을 위해서는 반드시 전문가와 상담하시기 바랍니다.')
        
        if total_score >= 10:
            st.write('''
            ### 도움받을 수 있는 곳
            - 자살예방상담전화: 1393
            - 정신건강상담전화: (02) 2204-0114
            - 가까운 정신건강복지센터 찾기: [링크](https://www.mentalhealth.go.kr/portal/health/fac/PotalHealthFacListTab2.do)
            ''')

if __name__ == '__main__':
    run_phq9_test()
