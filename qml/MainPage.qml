import QtQuick 2.0
import Sailfish.Silica 1.0

Page {
    //sailfish的ListView
    SilicaListView {
        anchors.fill: parent

        //定义header
        header: Column {
            width: parent.width

            //页头
            PageHeader {
                id: header
                title: "网易云音乐"
            }

            //下拉菜单
            PullDownMenu {
                MenuItem {
                    text: "搜索"
                    onClicked: pageStack.push("SearchPage.qml")
                }

                MenuItem {
                    text: "登录"
                    onClicked: pageStack.push("LoginPage.qml")
                }
            }
        }

        //定义列表模型
        model: ListModel {
            id: modelIcons

            ListElement { iconSource: "main_icon1.png"; iconText: "歌单" }
            ListElement { iconSource: "main_icon2.png"; iconText: "私人FM" }
            ListElement { iconSource: "main_icon3.png"; iconText: "专辑" }
            ListElement { iconSource: "main_icon4.png"; iconText: "歌手" }
            ListElement { iconSource: "main_icon5.png"; iconText: "本地音乐" }
        }

        //委派,即循环填充列表元素
        delegate: ListItem {
            id: listItem

            contentHeight: Theme.itemSizeExtraSmall

            //把一行切成两段,这是左半部分icon
            Item {
                id: leftIcon

                width: contentHeight
                height: contentHeight
                x: Theme.horizontalPageMargin
                opacity: listItem.enabled ? 1.0 : 0.4

                //创建一个矩形,透明
//                Rectangle {
//                    anchors.fill: parent
//                    gradient: Gradient {
//                        GradientStop {
//                            position: 0.0
//                            color: Theme.rgba(Theme.primaryColor, 0.1)
//                        }
//                        GradientStop {
//                            position: 1.0
//                            color: Theme.rgba(Theme.primaryColor, 0.05)
//                        }
//                    }

//                    Image {
//                        anchors.centerIn: parent
//                        source: "../images/" + iconSource
//                    }
//                }

                //上层遮罩
                Image {
                    //anchors.fill: parent
                    anchors.centerIn: parent
                    fillMode: Image.PreserveAspectCrop
                    sourceSize.height: contentHeight
                    source: "./images/" + iconSource

//                    Rectangle {
//                        anchors.fill: parent
//                        color: Theme.highlightBackgroundColor
//                        opacity: Theme.highlightBackgroundOpacity
//                        visible: listItem.highlighted
//                    }
                }
            }

            //这是右半部分
            Column {
                anchors {
                    left: leftIcon.right
                    leftMargin: Theme.paddingLarge
                    right: parent.right
                    rightMargin: Theme.horizontalPageMargin
                    verticalCenter: parent.verticalCenter
                }

                Label {
                    width: parent.width
                    opacity: listItem.enabled ? 1.0 : 0.4
                    color: highlighted ? Theme.highlightColor : Theme.primaryColor
                    font.pixelSize: Theme.fontSizeLarge
                    textFormat: Text.StyledText
                    truncationMode: TruncationMode.Fade
                    text: iconText
                }
            }
        }
    }
}
