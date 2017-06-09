import QtQuick 2.0
import Sailfish.Silica 1.0
import io.thp.pyotherside 1.4
import QtMultimedia 5.5

Page {
	id: main

	Label {
		id: wlan0

		text: "WLAN: "
	}

	Text {
		text: "Click Me!"
		y: wlan0.height
		color: "#FFFFFF"
	}

	MediaPlayer {
		id: playMusic	
		source: "../src/media/Angel.mp3"
	}

    Image {
        id: wheel

        anchors.centerIn: parent

		Behavior on rotation {
			NumberAnimation {
				duration: 250
			}
		}

    }

	MouseArea {
		anchors.fill: parent
		onClicked: wheel.rotation += 90
		onPressed: { playMusic.play() }
	}

	Python {
		Component.onCompleted: {
			addImportPath(Qt.resolvedUrl('../src'));
			importModule_sync("os")

			if (evaluate("os.uname().machine") == "armv7l"){
				addImportPath(Qt.resolvedUrl('../src/pyPackages/pillow-armv7hl'));
			} else {
				addImportPath(Qt.resolvedUrl('../src/pyPackages/pillow-i686'));
			}

			setHandler('ip_address', function(newvalue) {
				wlan0.text = "WLAN: " + newvalue;	
			});

			importModule('main', function() {
				wheel.source = 'image://python/pinwheel.png';
			});
		}

		onError: console.log('Python error: ' + traceback)
	}
}

