import requests

from bs4 import BeautifulSoup

while True:
    inputArea = input("날씨를 조회하려는 지역의 이름을 입력하세요(끝->프로그램 종료):")
    # 날씨 조회 지역명을 입력 받기 위한 input 문
    if inputArea == "끝":
        break

    try:
        weatherHtml = requests.get(f"https://search.naver.com/search.naver?query={inputArea}날씨")
        # 네이버에서 input 문에 입력한 지역의 날씨 조회 결과를 html로 가져오기

        weatherSoup = BeautifulSoup(weatherHtml.text, "html.parser")
        # print(weatherSoup.prettify())

        todayWeatherText = weatherSoup.find("span", {"class": "weather before_slash"}).text.strip()  # 오늘 날씨(맑음, 흐림)

        areaText = weatherSoup.find("h2", {"class":"title"}).text.strip()  # 날씨 조회 지역명
        print(f"날씨 조회 지역: {areaText}")

        nowTempText = weatherSoup.find("div", {"class":"temperature_text"}).text.strip()  # 현재온도
        print(f"현재 온도: {nowTempText[5:]}")

        yesterdayTempText = weatherSoup.find("p",{"class":"summary"}).text.strip()  # 어제와의 날씨 비교
        print(f"날씨 비교: {yesterdayTempText[:15].strip()}")


        print(f"오늘 날씨: {todayWeatherText}")

        senseTempText = weatherSoup.find("dd",{"class":"desc"}).text.strip()  # 체감 온도
        print(f"체감 온도: {senseTempText}")

        # todayWeatherInfoText = weatherSoup.find("ul", {"class":"today_chart_list"})
        todayWeatherInfoText = weatherSoup.select("ul.today_chart_list>li")
        # print(todayWeatherInfoText)

        dust1Info = todayWeatherInfoText[0].find("span",{"class":"txt"}).text.strip()  # 미세먼지 정보
        print(f"미세먼지: {dust1Info}")
        dust2Info = todayWeatherInfoText[1].find("span",{"class":"txt"}).text.strip()  # 초미세먼지 정보
        print(f"초미세먼지: {dust1Info}")
        print("=================================")
    except:
        print(f"***** 입력하신 {inputArea}지역은 날씨 조회가 되지 않는 지역입니다. *****")