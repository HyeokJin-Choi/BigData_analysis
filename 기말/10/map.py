import folium
import json
import pandas as pd

def popup_function(feature):
    return folium.Popup(feature['properties']['SIB_KOR_NM'])

districts = [
    {"name": "중구", "lat": 35.1065, "lon": 129.0323, "population": 46208},
    {"name": "서구", "lat": 35.0824, "lon": 129.0206, "population": 109742},
    {"name": "동구", "lat": 35.1293, "lon": 129.0450, "population": 93417},
    {"name": "영도구", "lat": 35.0911, "lon": 129.0680, "population": 114673},
    {"name": "부산진구", "lat": 35.1634, "lon": 129.0533, "population": 363678},
    {"name": "남구", "lat": 35.1367, "lon": 129.0842, "population": 281959},
    {"name": "해운대구", "lat": 35.1631, "lon": 129.1636, "population": 423660}
]

population_data = {d["name"]: d["population"] for d in districts}
# print(population_data)

geo_busan = json.load(open('Population_SIG/sigoo.geojson', encoding='UTF-8')) # 위도 경도가 있는 데이터
feature = [x for x in geo_busan['features'] if x['properties']['SIG_CD'].startswith('26')] # 부산의 구를 가지고 옴.
# features 리스트가 잘 필터링되었는지 확인하고 싶다면:
# for f in geo_busan['features']:
#     print(f['properties']['SIG_KOR_NM'] if f['properties']['SIG_CD'].startswith('26') else 0) # 또는 startswith 확인



geo_busan['features'] = feature # geo_busan에 features라는 컬럼을 추가하여 해당 데이터는 부산의 구를 가짐.

df_pop = pd.read_csv('Population_SIG/Population_SIG.csv')
df_pop.info()

df_pop['code'] = df_pop['code'].astype(str)
pcode_df = df_pop.query('code.str.startswith("26")').copy()

pusan_pop = pd.read_csv('Population_SIG/pusan_pop(1).csv', encoding='euc-kr')

pcode_df.drop(['pop'], axis=1, inplace=True)

pusan_pop['총인구'] = pusan_pop['총인구'].astype(int)
pcode = pd.merge(pcode_df, pusan_pop, how='inner', on='region') # 여기서 region이 부산의 행정구임

# print(pcode)

html_start = html = '<div \
style="\
font-size: 20px;\
color: red;\
background-color:rgba(255, 255, 255, 0);\
width:85px;\
text-align:left;\
margin:0px;\
"><b>'

html_end = '</b></div>'

# 이를 통해 아래의 Choropleth에서 bins를 기준으로 색상을 8단계로 나눔
bins = list(pcode['총인구'].quantile([0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))

map_pusan = folium.Map(location=[35.17, 129.07],
                       zoom_start=12,
                       tiles='cartodbpositron')


folium.Choropleth(
    geo_data=geo_busan, # 지도데이터
    data=pcode, # 색별로 표현할 통계 데이터
    columns=('code', '총인구'), # 통계 데이터의 행정 구역 코드 변수, 색갈로 표현할 변수(인구수)
    key_on='feature.properties.SIG_CD', # 지도데이터의 행정 구역 코드
    fill_color='YlGnBu', # 채울 색상
    legend_name='부산 구/군별 인구', # 범례명
    nan_fill_color='White',  # 결측치 색상
    fill_opacity=0.3, # 채우는 투명도
    line_opacity=0.5, # 구분선 투명도
    bins=bins # 색상의 단계
).add_to(map_pusan)

for district in districts:
    folium.CircleMarker(
        location=[district['lat'], district['lon']], # 위도 경도
        radius=district['population'] / 10000, # 원의 반지름
        color='blue', fill=True, fill_color='blues', # 원을 채울 색상 설정
        fill_opacity=0.6, # 원의 투명도
        popup=folium.Popup( # 클릭시 뜨는 팝업
            f'{district["name"]} 인구: {district["population"]}명',
            parse_html=True
        )
    ).add_to(map_pusan)

folium.GeoJson(
    geo_busan,
    name='geojson',
    tooltip=folium.GeoJsonTooltip(
        fields=['SIG_KOR_NM'],
        aliases=['시군구'],
        localize=True
    )
).add_to(map_pusan)



file_path = 'busan_map.html'
map_pusan.save(file_path)

import webbrowser
webbrowser.open(file_path)
