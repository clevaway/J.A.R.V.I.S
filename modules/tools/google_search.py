# tools/google_search.py

import webbrowser

class SearchTool:
    @staticmethod
    def trigger_phrases():
        """
        Return a list of phrases that trigger the search tool.
        """
        return ["google the", "google for"]

    @staticmethod
    def perform_search(user_input):
        """
        Perform a Google search based on user input that includes a search command.
        """
   
        # Split the user input by 'search'
        parts_after_search = user_input.lower().split('google', 1)
        print("Search requested",parts_after_search)
        if len(parts_after_search) > 1:
            #Split the second part by spaces and join the words starting from the second word
            search_keyword = ' '.join(parts_after_search[1].split()[1:])

            # Open Google search results for the search keyword in the default web browser
            url = f"https://www.google.com/search?q={search_keyword}"
            webbrowser.open(url)
                
            # Provide spoken feedback
            return f"The browser was launched with the search keyword."