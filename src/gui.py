from tkinter import Button, Entry, Label, Tk

from web_scraper import WebScraper


class GUI:
    def __init__(self):
        pass

    def run_gui(self):
        window = Tk()
        window.title('Web Scraper')
        window.config(padx=100, pady=100)
        window.geometry('700x250')

        url_input_label = Label(text='Enter URL (e.g. https://example.com):')
        url_input_label.grid(column=0, row=0)

        url_input = Entry(width=30)
        url_input.grid(column=1, row=0)

        tags_input_label = Label(text='Enter tags (e.g. div p a):')
        tags_input_label.grid(column=0, row=1)

        tags_input = Entry(width=30)
        tags_input.grid(column=1, row=1)

        file_name_input_label = Label(text='Enter file name (e.g. scraped_data.json):')
        file_name_input_label.grid(column=0, row=2)

        file_name_input = Entry(width=30)
        file_name_input.grid(column=1, row=2)

        def gui_get_data():
            web_scraper = WebScraper(
                url_input.get(), tags_input.get().split(), file_name_input.get()
            )
            data = web_scraper.scrape()
            print(web_scraper.write_data_to_json_file(data))

        button = Button(text='Scrape Website', command=gui_get_data)
        button.grid(column=1, row=3)

        window.mainloop()
