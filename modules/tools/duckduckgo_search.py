# tools/duckduckgo_search.py

from duckduckgo_search import DDGS

class DuckDuckGoSearch:
    @staticmethod
    def trigger_phrases():
        return [
            "search for", "find", "look up", "can you search for", "could you find",
            "please look up", "I want to know about",  "tell me about",
            "give me information on", "do you know", "any information on", "I need to find",
            "do a web search for"
        ]

    @staticmethod
    def duckduckgo_search(query):
        try:
            # Use the ddg function to fetch search results from DuckDuckGo
            results = DDGS().text(query, region="us-en", safesearch="off",
                              timelimit='y', max_results=10)
            if not results:
                return "No results found for your query."
 
            # Format the results as a response
            response = "Top search results:\n"
            for idx, result in enumerate(results, start=1):
                response += f"{idx}. {result['title']}: {result['href']}\n"
            return response.strip()

        except Exception as e:
            return f"There was an error while searching DuckDuckGo: {e}, please try again later."