import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def search(search_about):
    webbrowser.get(chrome_path).open_new_tab("https://www.google.com/search?q="+search_about)

