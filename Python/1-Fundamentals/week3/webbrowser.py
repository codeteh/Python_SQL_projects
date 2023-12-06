import webbrowser


def open_link_in_browser(url):
    webbrowser.open(url)


if __name__ == "__main__":
    url = "https://yelp.com"  # Replace with the desired URL
    open_link_in_browser(url)
