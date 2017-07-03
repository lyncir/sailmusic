import QtQuick 2.2
import Sailfish.Silica 1.0


Page {
	SilicaFlickable {
		anchors.fill: parent
		contentHeight: column.height

		/* 下拉选项 */
		PullDownMenu {
			MenuItem {
				text: qsTranslate("sailmusic", "About")	
				onClicked: pageStack.push("AboutPage.qml")
			}
		}

		Column {
			id: column
			width: parent.width

			/* 页头 */
			PageHeader {
				title: "Sailmusic"	
			}

			/* 主页列表 */
			MainPageListItem {
				title: qsTranslate("sailmusic", "PlayList")	
				onClicked: pageStack.push("PlaylistPage.qml")
			}
		}
	}
}
