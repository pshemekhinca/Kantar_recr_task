from utils.test_data import Input


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
    # advert_counter = '//*[@class="ytp-ad-duration-remaining"]'
    advert_counter = '//*[@class="video-ads ytp-ad-module"]'
    video_player = '//*[@id="movie_player"]'
    # sliderbar = '//*[@class="ytp-timed-markers-container"]'
    sliderbar_width = '//div[@class="ytp-chrome-bottom"]'
    sliderbar_pointer = '//*[@class="ytp-scrubber-container"]'
    # sliderbar_pointer = '//*[@class="ytp-progress-bar"]'
    play_button = '//*[@class="ytp-play-button ytp-button"]'
    mute_button = '//*[@class="ytp-mute-button ytp-button"]'
    video_title = f'//*[@class="style-scope ytd-video-primary-info-renderer" and contains(text(),"{Input.search_keyword}")]'
    video_duration = '//span[@class="ytp-time-duration"]'
    current_play_time = '//*[@class="ytp-time-current"]'
    channel_name = '//*[@class="style-scope ytd-video-owner-renderer"]'  # idx[1]
    views_amount = '//ytd-video-view-count-renderer'
    upload_date = '//div[@id="info-strings"]'
    likes_amount = '//yt-formatted-string[contains(@aria-label, "likes")]'  # idx[0]
    dislikes_amount = '//yt-formatted-string[@class="style-scope ytd-toggle-button-renderer style-text"]'  # idx[1]
    first_side_video = '//span[@class="style-scope ytd-compact-video-renderer"]'  # idx[0]
