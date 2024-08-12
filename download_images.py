from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
keywords = ["building workers", "construction workers", "industry workers", "smelter workers"]
for kw in keywords:
    response().download(kw, 25)