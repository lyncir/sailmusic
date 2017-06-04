# NOTICE:
#
# Application name defined in TARGET has a corresponding QML filename.
# If name defined in TARGET is changed, the following needs to be done
# to match new name:
#   - corresponding QML filename must be changed
#   - desktop icon filename must be changed
#   - desktop filename must be changed
#   - icon definition filename in desktop file must be changed
#   - translation filenames have to be changed

# The name of your application
TARGET = sailmusic

CONFIG += sailfishapp

SOURCES +=

OTHER_FILES += qml/sailmusic.qml \
    qml/pages/FirstPage.qml \
    rpm/sailmusic.changes.in \
    rpm/sailmusic.spec \
    rpm/sailmusic.yaml \
    sailmusic.desktop
