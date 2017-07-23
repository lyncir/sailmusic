import QtQuick 2.0
import Sailfish.Silica 1.0


Page {
    SilicaFlickable {
        anchors {
            fill: parent
            bottomMargin: panel.margin
        }

        clip: panel.expanded
        contentHeight: column.height + Theme.paddingLarge

        Column {
            id: column
            spacing: Theme.paddingLarge
            width: parent.width

            Button {
                text: playerPanel.open ? "Hide controls" : "Show controls"
                onClicked: playerPanel.open = !playerPanel.open
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
    }
}
