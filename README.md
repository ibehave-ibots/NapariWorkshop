

# English

## Activity 1: Find the Barrel Cortex

![Barrel Cortex](https://upload.wikimedia.org/wikipedia/commons/1/1d/RatBarrelFieldCOstain.jpg)

[Barrel Cortex Diagram](https://www.cell.com/cms/10.1016/j.neuron.2007.09.017/asset/16329b95-3e79-4732-9e54-3a63ecae4f3c/main.assets/gr1_lrg.jpg)

  1. In terminal: `pixi run python download_atlas.py`
  2. In terminal: `pixi run napari`
  3. Load the File `mouse_atlas.tif`
  4. Explore the mouse brain and find the `left barrel cortex` in either 3D or 2D mode.



## Activity 2: Label Cells

[Calcium Imaging Video](https://www.youtube.com/shorts/DyFPv_aKQkI)

  1. In terminal: `pixi run napari`
  2. Load the Files `frames.tif` and `labels.tif`
  3. Label each cell you can find.
  4. Save the cell_labels layer as `labels.tif`


## Activity 3: View Cell Activity

![ROIs to Traces](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1006054/2/pcbi.1006054.g004.PNG_M?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20260423%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260423T063550Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=8765ddbfe33659d15c38c7a39d9e3a16b7e93de77b2cc1bcb17b36f0f7b0a6f516fc780215ae137d09c5afaea6b58f1e96e6bb0f6614fa9befc307a3441ab3ce1ee08bea596b8f260bba23e0a2731c038f2bf2667b3c0db04e1314ec14ed55aa960c77166799d12e0c8b079a173d06bceae1809aa2586c07b0b2806f40deb90423483559dfe664790e934b33bef88b3c86e9db8cf314655b93587518b6b7a74205e1033e3117f2b5343810916bb4c120b771017158b058410b3f6e9b6c21f0c36f7329b0ac284fea341835a3a26c310d15409f8ec7606200e4008bb4694309b16e3ffd1e2978492a75dea51a600848723cb9c10ec0c0f292446b9220da156212)

  1. In terminal: `pixi run python get_cell_activity.py frames.tif labels.tif`
  2. Open `results.png` to view the Average Cell Activities
  3. Do you see clear peaks, when the cell spiked?  Do the cells spike at the same time as each other?



---


# Deutsch

## Aufgabe 1: Finde den Barrel-Cortex

![Barrel-Cortex](https://upload.wikimedia.org/wikipedia/commons/1/1d/RatBarrelFieldCOstain.jpg)

[Barrel-Cortex-Diagramm](https://www.cell.com/cms/10.1016/j.neuron.2007.09.017/asset/16329b95-3e79-4732-9e54-3a63ecae4f3c/main.assets/gr1_lrg.jpg)

1. Im Terminal: `pixi run python download_atlas.py`
2. Im Terminal: `pixi run napari`
3. Lade die Datei `mouse_atlas.tif`
4. Erkunde das Mausgehirn und finde den linken Barrel-Cortex in 3D oder 2D.

## Aufgabe 2: Zellen beschriften

[Video zur Kalziumbildgebung](https://www.youtube.com/shorts/DyFPv_aKQkI)
  
1. Im Terminal: `pixi run napari`
2. Laden Sie die Dateien `frames.tif` und `labels.tif`.
3. Beschriften Sie jede gefundene Zelle.
4. Speichern Sie die Ebene `cell_labels` als `labels.tif`.

## Aufgabe 3: Zellenaktivität anzeigen

![Traces](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1006054/2/pcbi.1006054.g004.PNG_M?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20260423%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260423T063550Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=8765ddbfe33659d15c38c7a39d9e3a16b7e93de77b2cc1bcb17b36f0f7b0a6f516fc780215ae137d09c5afaea6b58f1e96e6bb0f6614fa9befc307a3441ab3ce1ee08bea596b8f260bba23e0a2731c038f2bf2667b3c0db04e1314ec14ed55aa960c77166799d12e0c8b079a173d06bceae1809aa2586c07b0b2806f40deb90423483559dfe664790e934b33bef88b3c86e9db8cf314655b93587518b6b7a74205e1033e3117f2b5343810916bb4c120b771017158b058410b3f6e9b6c21f0c36f7329b0ac284fea341835a3a26c310d15409f8ec7606200e4008bb4694309b16e3ffd1e2978492a75dea51a600848723cb9c10ec0c0f292446b9220da156212)


1. Im Terminal: `pixi run python get_cell_activity.py frames.tif labels.tif`
2. Öffnen Sie `results.png`, um die durchschnittliche Zellaktivität anzuzeigen.
3. Sind deutliche Aktivitätsspitzen erkennbar, wenn die Zellen ihre Aktivität steigern? Treten die Aktivitätsspitzen der Zellen gleichzeitig auf?