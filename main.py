import streamlit as st
import random
from datetime import datetime

# ------------------ 데이터 설정 ------------------
music_links = {
    "Lofi": [...],
    "EDM": [...],
    "OST": [...],
    "재즈": [...],
    "클래식": [...],
    "감성 발라드": [...],
    "몽환적 사운드": [...],
    "정돈된 테마 음악": [...],
    "다양성 있는 셔플 믹스": [...],
    "신나는 팝": [...],
    "레트로팝": [...],
    "드림팝": [...],
    "가사 중심 감성곡": [...]
}

style_mapping = {
    "INTJ": "정돈된 테마 음악",
    "INFP": "감성 발라드",
    "ENFP": "신나는 팝",
    "ENTP": "다양성 있는 셔플 믹스",
    "ISFJ": "클래식",
    "ISTP": "EDM",
    "INFJ": "몽환적 사운드",
    "ESFJ": "OST",
    "ISTJ": "재즈",
    "ESTP": "레트로팝",
    "ENFJ": "가사 중심 감성곡",
    "ESFP": "드림팝",
    "ISFP": "Lofi",
    "INTP": "정돈된 테마 음악",
    "ESTJ": "신나는 팝",
    "ENTJ": "EDM"
}

mood_boost = {
    "맑음": "신나는 팝",
    "비": "감성 발라드",
    "눈": "클래식",
    "흐림": "몽환적 사운드",
    "행복": "다양성 있는 셔플 믹스",
    "우울": "감성 발라드",
    "설렘": "드림팝",
    "집중": "정돈된 테마 음악",
    "봄": "OST",
    "여름": "레트로팝",
    "가을": "재즈",
    "겨울": "클래식",
    "아침": "Lofi",
    "점심": "신나는 팝",
    "저녁": "재즈",
    "밤": "몽환적 사운드"
}

country_song_count = {
    "대한민국": 3,
    "일본": 4,
    "미국": 5,
    "영국": 5,
    "기타": 3
}

# ------------------ 추천 함수 ------------------
def recommend_music(mbti, weather, mood, season, time_of_day, country):
    base_style = style_mapping.get(mbti.upper(), "다양성 있는 셔플 믹스")
    style_candidates = [base_style]

    for factor in [weather, mood, season, time_of_day]:
        if factor in mood_boost:
            style_candidates.append(mood_boost[factor])

    final_style = max(set(style_candidates), key=style_candidates.count)
    songs = music_links[final_style]
    random.shuffle(songs)
    count = country_song_count.get(country, 3) + 2  # 국가 기준 + 2곡 추가
    return final_style, songs[:count]

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="MBTI 음악 추천기 🎧", page_icon="🎵")
st.title("🌤️ MBTI + 날씨 + 기분 + 계절 + 시간 기반 음악 추천기 🎶")

mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(style_mapping.keys()))
weather = st.selectbox("오늘의 날씨는 어떤가요?", ["맑음", "흐림", "비", "눈"])
mood = st.selectbox("지금 기분은 어떤가요?", ["행복", "우울", "설렘", "집중"])
season = st.selectbox("현재 계절은?", ["봄", "여름", "가을", "겨울"])
country = st.selectbox("당신이 위치한 국가는 어디인가요?", ["대한민국", "일본", "미국", "영국", "기타"])
time_now = datetime.now().hour

# 시간대 자동 추출
time_of_day = "아침" if 5 <= time_now < 11 else \
               "점심" if 11 <= time_now < 16 else \
               "저녁" if 16 <= time_now < 21 else "밤"
st.write(f"🕒 현재 시간대: **{time_of_day}**")

if st.button("🎵 음악 추천받기"):
    style, recommendations = recommend_music(mbti, weather, mood, season, time_of_day, country)
    st.success(f"💡 추천 스타일: **{style}**")
    for i, url in enumerate(recommendations, 1):
        st.markdown(f"{i}. [YouTube 링크]({url})")
        st.video(url)


