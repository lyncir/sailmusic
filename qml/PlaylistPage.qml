import QtQuick 2.2
import Sailfish.Silica 1.0


Page {
	SilicaListView {
		id: listView

		header: PageHeader {
			title: "Playlist"	
		}

		delegate: BaseTrackDelegate {
			showArtistAndAlbum: "Nomi" && "Let Me In"	
		}
	}
}
