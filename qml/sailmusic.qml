import QtQuick 2.0
import Sailfish.Silica 1.0

ApplicationWindow {
    id: root

	initialPage: Component { Main { } }
    cover: Qt.resolvedUrl("Cover.qml")
}
