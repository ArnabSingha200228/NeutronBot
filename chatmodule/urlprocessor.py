from langchain_community.document_loaders import WebBaseLoader

def process_url(url):
    """
        Loads the text contents of the web page of the given URL

        Args:
            url: URL as string
        Returns:
            tokens of file content as Document
    """
    loader = WebBaseLoader(url)
    # Load the website content into Document objects
    documents = loader.load()
    return documents