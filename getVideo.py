import os

video_urls = [
    "https://www.bilibili.com/video/BV1yT411q76Y/?spm_id_from=333.999.top_right_bar_window_history.content.click",
    "https://www.bilibili.com/video/BV1Fr4y1d7aE/?spm_id_from=333.999.0.0",
    "https://www.bilibili.com/video/BV1fg411v7M3/?spm_id_from=333.999.0.0&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1iV4y1R7jv/?vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1i3411k7Qj/?spm_id_from=333.337.search-card.all.click&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1Ya411673b/?spm_id_from=333.337.search-card.all.click&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1JQ4y1S7c4/?spm_id_from=333.999.0.0&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1TV4y1d71V/?spm_id_from=333.337.search-card.all.click&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV14K4y1L7Ht/?spm_id_from=333.337.search-card.all.click&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1we4y1b7EX/?spm_id_from=333.337.search-card.all.click&vd_source=26e068fb0e86a3481e9cfee189e08062",
    "https://www.bilibili.com/video/BV1bd4y1i7VJ/?spm_id_from=333.999.0.0&vd_source=26e068fb0e86a3481e9cfee189e08062"
    # 添加更多的视频URL
]
cookies_file = "cookies.txt"
for url in video_urls:
    os.system(f"you-get {url} --cookies {cookies_file}")