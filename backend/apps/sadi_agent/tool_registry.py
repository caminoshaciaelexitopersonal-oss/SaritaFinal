import requests
import asyncio
import os
from .tool import Tool

# --- Tool Implementations ---

async def search_web(query: str) -> str:
    """
    Searches the web for a given query using a basic request.
    This is a simplified example. A real implementation would use a search API.
    """
    loop = asyncio.get_running_loop()
    try:
        # Use to_thread to run the synchronous requests.get in a separate thread
        response = await loop.run_in_executor(
            None,
            lambda: requests.get(f"https://www.google.com/search?q={query.replace(' ', '+')}", headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            })
        )
        response.raise_for_status()
        # NOTE: This returns the full HTML. A real tool would parse this.
        return response.text[:2000] # Return the first 2000 chars to avoid being too large
    except Exception as e:
        return f"Error searching web: {e}"

def write_file(path: str, content: str) -> str:
    """
    Writes content to a file at the specified path.
    """
    try:
        # Basic security to prevent writing outside of a dedicated 'workspace' directory
        workspace_dir = "workspace"
        if not os.path.exists(workspace_dir):
            os.makedirs(workspace_dir)

        safe_path = os.path.join(workspace_dir, os.path.basename(path))

        with open(safe_path, 'w') as f:
            f.write(content)
        return f"File '{safe_path}' written successfully."
    except Exception as e:
        return f"Error writing file: {e}"


# --- Tool Registry ---

def get_tools() -> list[Tool]:
    """
    Returns a list of all available tools for the agent.
    """
    return [
        Tool(
            name="search_web",
            description="Searches the web for a given query and returns the raw HTML content.",
            function=search_web,
            params={"query": "The search query string."}
        ),
        Tool(
            name="write_file",
            description="Writes the given content to a file. Use this to save your work.",
            function=write_file,
            params={"path": "The path of the file to write.", "content": "The content to write into the file."}
        ),
    ]
