from datetime import datetime, timedelta

# Third-party imports
from arxiv import Client, Search, SortCriterion, SortOrder
import srsly
today = datetime.today() - timedelta(days=7)


def download_data():
	# Search for the 10 most recent articles matching the keyword "quantum."
	search = Search(
		query = "active learning",
		sort_by = SortCriterion.SubmittedDate,
		sort_order=SortOrder.Descending,
		max_results=100, # arbitrary number
	)

	client = Client()
	results = client.results(search)
	articles = []

	for r in results:
			# If published or updated date is today, print the article.
		if r.published.date() >= today.date() or r.updated.date() >= today.date():
			if r.primary_category.startswith('cs'):
				article = {
					"Title": r.title,
					"Primary Category": r.primary_category,
					"Categories": r.categories,
					"Summary": r.summary,
					"Link": r.pdf_url,
					"Published": r.published,
					}
			articles.append(article)
	
	srsly.write_jsonl(f"data/results_{today.date()}.jsonl", articles)
