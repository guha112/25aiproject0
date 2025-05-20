import streamlit as st
import random
from datetime import datetime

# ------------------ 데이터 설정 ------------------
music_links = {
    "Lofi": [
        "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "https://www.youtube.com/watch?v=DWcJFNfaw9c",
        "https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "https://www.youtube.com/watch?v=ioNng23DkIM",
        "https://www.youtube.com/watch?v=7NOSDKb0HlU"
    ],
    "EDM": [
        "https://www.youtube.com/watch?v=60ItHLz5WEA",
        "https://www.youtube.com/watch?v=Zz6zHmZxF9U",
        "https://www.youtube.com/watch?v=pXRviuL6vMY",
        "https://www.youtube.com/watch?v=RgKAFK5djSk",
        "https://www.youtube.com/watch?v=UceaB4D0jpo"
    ],
    "OST": [
        "https://www.youtube.com/watch?v=c6ASQOwKkhk",
        "https://www.youtube.com/watch?v=Q2sF3g3p9Qg",
        "https://www.youtube.com/watch?v=rA0HZ9YzFsM",
        "https://www.youtube.com/watch?v=WNeLUngb-Xg",
        "https://www.youtube.com/watch?v=yKNxeF4KMsY"
    ],
    "재즈": [
        "https://www.youtube.com/watch?v=DSGyEsJ17cI",
        "https://www.youtube.com/watch?v=vmDDOFXSgAs",
        "https://www.youtube.com/watch?v=HMnrl0tmd3k",
        "https://www.youtube.com/watch?v=VMnjF1O4eH0",
        "https://www.youtube.com/watch?v=Dx5qFachd3A"
    ],
    "클래식": [
        "https://www.youtube.com/watch?v=GRxofEmo3HA",
        "https://www.youtube.com/watch?v=_4IRMYuE1hI",
        "https://www.youtube.com/watch?v=6z4KK7RWjmk",
        "https://www.youtube.com/watch?v=Rb0UmrCXxVA",
        "https://www.youtube.com/watch?v=6JQm5aSjX6g"
    ],
    "감성 발라드": [
        "https://www.youtube.com/watch?v=a7SouU3ECpU",
        "https://www.youtube.com/watch?v=nQWFzMvCfLE",
        "https://www.youtube.com/watch?v=X2mqrzKHb3w",
        "https://www.youtube.com/watch?v=LXUSaVw3Mvk",
        "https://www.youtube.com/watch?v=mtL4rI4r4uc"
    ],
    "몽환적 사운드": [
        "https://www.youtube.com/watch?v=8UVNT4wvIGY",
        "https://www.youtube.com/watch?v=ktvTqknDobU",
        "https://www.youtube.com/watch?v=HyHNuVaZJ-k",
        "https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "https://www.youtube.com/watch?v=E07s5ZYygMg"
    ],
    "정돈된 테마 음악": [
        "https://www.youtube.com/watch?v=Z1BCujX3pw8",
        "https://www.youtube.com/watch?v=UceaB4D0jpo",
        "https://www.youtube.com/watch?v=sCNlt5e4LZc",
        "https://www.youtube.com/watch?v=CduA0TULnow",
        "https://www.youtube.com/watch?v=uelHwf8o7_U"
    ],
    "다양성 있는 셔플 믹스": [
        "https://www.youtube.com/watch?v=OPf0YbXqDm0",
        "https://www.youtube.com/watch?v=YQHsXMglC9A",
        "https://www.youtube.com/watch?v=tAGnKpE4NCI",
        "https://www.youtube.com/watch?v=fLexgOxsZu0",
        "https://www.youtube.com/watch?v=09R8_2nJtjg"
    ],
    "신나는 팝": [
        "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
        "https://www.youtube.com/watch?v=fRh_vgS2dFE",
        "https://www.youtube.com/watch?v=3AtDnEC4zak",
        "https://www.youtube.com/watch?v=09R8_2nJtjg",
        "https://www.youtube.com/watch?v=OPf0YbXqDm0"
    ],
    "레트로팝": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=Zi_XLOBDo_Y",
        "https://www.youtube.com/watch?v=YQHsXMglC9A",
        "https://www.youtube.com/watch?v=8UVNT4wvIGY",
        "https://www.youtube.com/watch?v=60ItHLz5WEA"
    ],
    "드림팝": [
        "https://www.youtube.com/watch?v=JeB6KFYmUDk",
        "https://www.youtube.com/watch?v=pK8GRKnhHe8",
        "https://www.youtube.com/watch?v=ktvTqknDobU",
        "https://www.youtube.com/watch?v=nfWlot6h_JM",
        "https://www.youtube.com/watch?v=F90Cw4l-8NY"
    ],
    "가사 중심 감성곡": [
        "https://www.youtube.com/watch?v=uelHwf8o7_U",
        "https://www.youtube.com/watch?v=lp-EO5I60KA",
        "https://www.youtube.com/watch?v=Z1BCujX3pw8",
        "https://www.youtube.com/watch?v=RBumgq5yVrA",
        "https://www.youtube.com/watch?v=RgKAFK5djSk"
    ]
}

# 국가별 음악 스타일 선호도 추가
country_style_preference = {
    "대한민국": "감성 발라드",
    "일본": "OST",
    "미국": "EDM",
    "영국": "재즈",
    "기타": "신나는 팝"
}

# ------------------ 추천 함수 ------------------
def recommend_music(mbti, weather, mood, season, time_of_day, country):
    base_style = style_mapping.get(mbti.upper(), "다양성 있는 셔플 믹스")
    style_candidates = [base_style]

    for factor in [weather, mood, season, time_of_day]:
        if factor in mood_boost:
            style_candidates.append(mood_boost[factor])

    # 국가 선호 스타일도 후보에 포함
    if country in country_style_preference:
        style_candidates.append(country_style_preference[country])

    final_style = max(set(style_candidates), key=style_candidates.count)
    songs = music_links[final_style]
    random.shuffle(songs)
    count = country_song_count.get(country, 3) + 2
    return final_style, songs[:count]

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="MBTI 음악 추천기 🎧", page_icon="🎵")
st.title("🌤️ MBTI + 날씨 + 기분 + 계절 + 시간 + 국가 기반 음악 추천기 🎶")

mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(style_mapping.keys()))
weather = st.selectbox("오늘의 날씨는 어떤가요?", ["맑음", "흐림", "비", "눈"])
mood = st.selectbox("지금 기분은 어떤가요?", ["행복", "우울", "설렘", "집중"])
season = st.selectbox("현재 계절은?", ["봄", "여름", "가을", "겨울"])
country = st.selectbox("당신이 위치한 국가는 어디인가요?", ["대한민국", "일본", "미국", "영국", "기타"])
time_now = datetime.now().hour

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
