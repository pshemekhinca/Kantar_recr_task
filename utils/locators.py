class YTHomeLocators:
    """Locators for the YouTube Home Page"""
    cookies_accept_button = '//tp-yt-paper-button[contains(@aria-label,"Accept")]'
    search_box = '//input[@id="search"]'
    search_button = '//button[@id="search-icon-legacy"]'


class ResultsListLocators:
    """Locators for searched results list page"""
    found_promoted = '//ytd-promoted-video-renderer'
    found_no_advert = '//*[@class="title-and-badge style-scope ytd-video-renderer"]'
    video_title = '//a[@id="video-title"]'  # idx[0]
    verify_xpath = '//*[@id="video-title" and contains(text(),'


class SelectedVideoLocators:
    """Locators for the selected video player page"""
    skip_advert_button = '//button[@class="ytp-ad-skip-button ytp-button"]'
    # advert_counter = '//*[@id="simple-ad-badge:f"]'
    advert_counter = '//*[@class="ytp-ad-duration-remaining"]'
    video_player = '//video'
    sliderbar = '//*[@class="ytp-timed-markers-container"]'
    slidebar_pointer = '//*[@class="ytp-scrubber-container"]'
    play_button = '//*[@class="ytp-play-button ytp-button"]'
    mute_button = '//*[@class="ytp-mute-button ytp-button"]'
    video_title = '//*[@class="style-scope ytd-video-primary-info-renderer" and contains(text(),"Python")]'
    video_duration = '//span[@class="ytp-time-duration"]'
    current_play_time = '//*[@class="ytp-time-current"]'
    channel_name = '//*[@id="channel-name"]'  # idx[0]
    views_amount = '//ytd-video-view-count-renderer'
    upload_date = '//div[@id="info-strings"]'
    likes_amount = '//yt-formatted-string[@class="style-scope ytd-toggle-button-renderer style-text"]'  # idx[0]
    dislikes_amount = '//yt-formatted-string[@class="style-scope ytd-toggle-button-renderer style-text"]'  # idx[1]
    first_side_video = '//ytd-compact-video-renderer'  # idx[0]
