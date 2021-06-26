from news_scraper import NewsScraper as NS

def main():
    #create bot fetcher
    bot = NS()
    bot.fetch_data()

if __name__ == "__main__":
    main()