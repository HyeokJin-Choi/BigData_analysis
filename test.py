for district in districts:   

    folium.CircleMarker(
        location=[district['lat'],district['lon']],
        radius=district['population']/10000,
        color='blue', fill=True,fill_color='blues',
        fill_opacity=0.6,
        popup=folium.Popup(f'{district["name"]} 인구: {district["population"]} 명',
                          parse_html=True )).add_to(map_pusan)
    folium.Marker(location = [district['lat'], district['lon']],
                  icon = folium.DivIcon(
                      icon_anchor = (0,0),
                      html = html_start + district["name"] + html_end
                      )).add_to(map_pusan)
