import sys
import folium
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class InteractiveMap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Creating map
        self.map = folium.Map(tiles='https://tile.jawg.io/jawg-streets/{z}/{x}/{y}{r}.png?access-token=YOUR_TOKEN',
                 attr='<a href="https://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors')

        #Creating markers
        icon1 = folium.CustomIcon(
            icon_image='icons/1.png',
            icon_size=(70, 70),
        )

        folium.Marker(
            [25.197197, 55.2743764],
            popup='<b>Burj Khalifa</b>',
            icon=icon1
        ).add_to(self.map)

        icon2 = folium.CustomIcon(
            icon_image='icons/2.png',
            icon_size=(60, 60),
        )
        folium.Marker(
            [25.141306, 55.185348],
            popup='<b>Burj Al Arab</b>',
            icon=icon2
        ).add_to(self.map)


        icon3 = folium.CustomIcon(
            icon_image='icons/3.png',
            icon_size=(65, 65),
        )
        folium.Marker(
            [25.2354522, 55.3003409],
            popup='<b>Dubai Frame</b>',
            icon=icon3
        ).add_to(self.map)


        icon4 = folium.CustomIcon(
            icon_image='icons/4.png',
            icon_size=(65, 65),
        )
        folium.Marker(
            [25.2192034, 55.2819328],
            popup='<b>Museum of the future</b>',
            icon=icon4
        ).add_to(self.map)

        icon5 = folium.CustomIcon(
            icon_image='icons/5.png',
            icon_size=(50, 50),
        )
        folium.Marker(
            [24.412800, 54.474711],
            popup='<b>Sheikh Zayed Grand Mosque</b>',
            icon=icon5
        ).add_to(self.map)

        icon6 = folium.CustomIcon(
            icon_image='icons/6.png',
            icon_size=(40, 40),
        )
        folium.Marker(
            [25.076441843288364, 55.140503999993946],
            popup='<b>Marina Mall</b>',
            icon=icon6
        ).add_to(self.map)

        icon7 = folium.CustomIcon(
            icon_image='icons/7.png',
            icon_size=(40, 40),
        )
        folium.Marker(
            [25.118046, 55.200418],
            popup='<b>Mall of the Emirates</b>',
            icon=icon7
        ).add_to(self.map)

        folium.Marker(
            [25.114483, 55.365841],
            popup='Albero',
            icon=folium.Icon(color='red')
        ).add_to(self.map)

        folium.Marker(
            [25.097114, 55.314315],
            popup='Samana Barari',
            icon=folium.Icon(color='blue')
        ).add_to(self.map)

        folium.Marker(
            [24.997975, 55.169431],
            popup='Olivia Residences',
            icon=folium.Icon(color='orange')
        ).add_to(self.map)

        folium.Marker(
            [25.274177, 55.266984],
            popup='OceanZ',
            icon=folium.Icon(color='green')
        ).add_to(self.map)

        folium.Marker(
            [25.035900, 55.195400],
            popup='Samana Portofino',
            icon=folium.Icon(color='purple')
        ).add_to(self.map)

        folium.Marker(
            [25.042120, 55.188669],
            popup='FashionZ 1',
            icon=folium.Icon(color='darkblue')
        ).add_to(self.map)

        folium.Marker(
            [25.033052, 55.173458],
            popup='Altai Tower',
            icon=folium.Icon(color='gray')
        ).add_to(self.map)

        folium.Marker(
            [25.069738, 55.247339],
            popup='Aqua Dimore',
            icon=folium.Icon(color='pink')
        ).add_to(self.map)

        folium.Marker(
            [24.500301, 54.394011],
            popup='Renad Tower',
            icon=folium.Icon(color='beige')
        ).add_to(self.map)

        folium.Marker(
            [25.493073, 55.535095],
            popup='Sun Island Smart Villas',
            icon=folium.Icon(color='darkgreen')
        ).add_to(self.map)

        folium.Marker(
            [25.058063, 55.236394],
            popup='Empire Estates',
            icon=folium.Icon(color='lightblue')
        ).add_to(self.map)

        folium.Marker(
            [25.059191, 55.213642],
            popup='Binghatti Tulip',
            icon=folium.Icon(color='darkred')
        ).add_to(self.map)

        folium.Marker(
            [25.054907, 55.205679],
            popup='Luma Park Views',
            icon=folium.Icon(color='darkpurple')
        ).add_to(self.map)
        
        #QWebEngineView
        self.webView = QWebEngineView()

        #HTML representation of the map
        data = self.map._repr_html_()
        self.webView.setHtml(data)

        # Устанавливаем QWebEngineView как центральный виджет
        self.setCentralWidget(self.webView)

        #Sizes and Name of the window
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle('Interactive Map of Dubai')

        #Show the window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InteractiveMap()
    sys.exit(app.exec_())