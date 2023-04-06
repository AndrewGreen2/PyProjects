from recipe_scrapers import scrape_me

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
scraper = scrape_me('https://www.taste.com.au/recipes/carrot-cake-4/33f5d166-2a0a-4e30-88a7-cdf931a7b952', wild_mode=True)

scraper.host()
scraper.title()
scraper.total_time()
scraper.image()
scraper.ingredients()
scraper.instructions()
scraper.instructions_list()
scraper.yields()
scraper.to_json()
scraper.links()
scraper.nutrients()  # if available

print(scraper.nutrients())
print(scraper.title())