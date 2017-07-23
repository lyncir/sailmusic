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

            ListElement { iconSource: "main_icon1.png"; iconText: "歌单"; iconUrl: "PlayListPage.qml" }
            ListElement { iconSource: "main_icon2.png"; iconText: "私人FM"; iconUrl: "FMPage.qml" }
            ListElement { iconSource: "main_icon3.png"; iconText: "专辑"; iconUrl: "AlbumPage.qml" }
            ListElement { iconSource: "main_icon4.png"; iconText: "歌手"; iconUrl: "ArtistPage.qml" }
            ListElement { iconSource: "main_icon5.png"; iconText: "本地音乐"; iconUrl: "LocalPage.qml" }
            ListElement { iconSource: "main_icon5.png"; iconText: "测试页面"; iconUrl: "PlayingPanel.qml" }
        }

        //委派,即循环填充列表元素
        delegate: ListItem {
            id: listItem

            contentHeight: Theme.itemSizeExtraSmall
            onClicked: pageStack.push(iconUrl)

            //把一行切成两段,这是左半部分icon
            Item {
                id: leftIcon

                width: contentHeight
                height: contentHeight
                x: Theme.horizontalPageMargin
                opacity: listItem.enabled ? 1.0 : 0.4


                //图标图片
                Image {
                    //anchors.fill: parent
                    anchors.centerIn: parent
                    fillMode: Image.PreserveAspectCrop
                    sourceSize.height: contentHeight
                    source: "./images/" + iconSource
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

                //文字
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
