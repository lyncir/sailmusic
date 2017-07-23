import QtQuick 2.0
import Sailfish.Silica 1.0

ApplicationWindow {
    id: root

	initialPage: Component { MainPage { } }
    cover: Qt.resolvedUrl("Cover.qml")
    bottomMargin: playerPanel.visibleSize

    //播放器控制面板
    DockedPanel {
        id: playerPanel

        width: parent.width
        height: Theme.itemSizeMedium

        dock: Dock.Bottom
        open: true

        //按钮
        BackgroundItem {
            id: pressItem

            anchors.fill: parent

            opacity: 1

            //进度播放详情页
            onClicked: pageStack.push("PlayingPage.qml")

            //进度条
            Item {
                id: progressBarItem

                height: Theme.paddingSmall
                width: parent.width

                //进度条左半部分高亮
                Rectangle {
                    id: progressBar

                    height: parent.height
                    //当前播放进度
                    width: 300
                    color: Theme.highlightColor
                    opacity: 0.5
                }

                //进度条有半部分透明
                Rectangle {
                    anchors {
                        left: progressBar.right
                        right: parent.right
                    }
                    height: parent.height
                    color: "black"
                    opacity: Theme.highlightBackgroundOpacity
                }
            }

            //按钮
            Item {
                anchors {
                    top: progressBarItem.bottom
                    bottom: parent.bottom
                }
                width: parent.width

                //左边图片
                Item {
                    id: mediaArt

                    width: pressItem.height
                    height: pressItem.height
                    opacity: 1.0

                    Image {
                        anchors.fill: parent
                        fillMode: Image.PreserveAspectCrop
                        sourceSize.height: parent.width
                        //source: "./images/main_icon1.png"

                        Rectangle {
                            anchors.fill: parent
                            color: Theme.highlightBackgroundColor
                            opacity: Theme.highlightBackgroundOpacity
                        }
                    }
                }

                //歌名和歌手
                Column {
                    anchors {
                        left: mediaArt.right
                        leftMargin: Theme.paddingMedium
                        right: buttonsRow.left
                        verticalCenter: parent.verticalCenter
                    }

                    //歌名
                    Label {
                        color: Theme.highlightColor
                        font.pixelSize:  Theme.fontSizeSmall
                        text: "这里是歌名"
                        truncationMode: TruncationMode.Fade
                        width: parent.width
                    }

                    Label {
                        font.pixelSize: Theme.fontSizeSmall
                        text: "这里是歌手"
                        truncationMode: TruncationMode.Fade
                        width: parent.width
                    }
                }

                //播放按钮
                Row {
                    id: buttonsRow

                    anchors {
                        right: parent.right
                        horizontalCenter: undefined
                    }

                    height: parent.height
                    spacing: 0

                    //上一首
                    IconButton {

                        height: parent.height
                        icon.source: "./images/icon-m-previous.png"
                    }

                    //播放暂停
                    IconButton {
                        height: parent.height
                        icon.source: "./images/icon-m-play.png"
                    }

                    //下一首
                    IconButton {
                        height: parent.height
                        icon.source: "./images/icon-m-next.png"
                    }
                }
            }
        }
    }
}
