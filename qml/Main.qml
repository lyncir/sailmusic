import QtQuick 2.0
import Sailfish.Silica 1.0
import io.thp.pyotherside 1.4

Page {
	id: main

    Image {
        id: wheel

        anchors.centerIn: parent

		Behavior on rotation {
			NumberAnimation {
				duration: 250
			}
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

                importModule('main', function() {
                    wheel.source = 'image://python/pinwheel.png';
                });
            }

            onError: console.log('Python error: ' + traceback)
        }
    }

	MouseArea {
		anchors.fill: parent
		onClicked: wheel.rotation += 90
	}
}

