from datetime import datetime, timedelta

# Third-party imports
from arxiv import Client, Search, SortCriterion, SortOrder
from click import
# Construct the default API client.
client = Client()
today = datetime.today() - timedelta(days=1)
CATEGORIES = ["cs.LG", "cs.AI", "cs.CL", "cs.CV", "cs.DB", "cs.ET", "cs.GL"]


# Search for the 10 most recent articles matching the keyword "quantum."
search = Search(
  query = "active learning",
  sort_by = SortCriterion.SubmittedDate,
  sort_order=SortOrder.Descending,
  max_results=100, # arbitrary number
)

results = client.results(search)
for r in results:
    # If published or updated date is today, print the article.
    if r.published.date() == today.date() or r.updated.date() == today.date():
        print(f"Title: {r.title}")
        print(f"Primary Category: {r.primary_category}")
        print(f"Categories: {r.categories}")
        print(f"Summary: {r.summary}")
        print(f"Link: {r.pdf_url}")


if __name__ == '__main__':
    main()
