
# ---- Download Atlas --------------------------------------
from brainglobe_atlasapi.bg_atlas import BrainGlobeAtlas

atlas = BrainGlobeAtlas("allen_mouse_25um")
# -------------------------------------------------------




# ---- Save Atlas to File --------------------------------
from tifffile import imwrite

imwrite('mouse_atlas.tif', atlas.reference)
# ---------------------------------------------------