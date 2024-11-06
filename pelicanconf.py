# Import the necessary module
from datetime import datetime


'''
Build configuration settings
'''

# Defines whether Pelican should use document-relative URLs or not. Only set this to True when developing/testing and only if you fully understand the effect it can have on links/feeds

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme color settings
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

'''
Site configuration settings
'''

# Configuration settings for the blog
AUTHOR = 'Phillip Bruno'  # Author's name
SITENAME = "Phillip Bruno's Professional Portfolio"  # Site title
SITETITLE = "Phillip Bruno"  # Short site title (used in meta tags)
SITESUBTITLE = "Professional Portfolio"  # Site subtitle
SITEURL = 'https://phillip-bruno.github.io'  # URL of the site
SITEDESCRIPTION = """A bit about me and my career."""  # Description of the site
SITELOGO = '/extra/computer_fire.png'  # Logo for the site ( favicon, header image)
FAVICON = '/extra/favicon.ico'  # Favicon for the site


# Domain and Feed settings
DOMAIN = SITEURL  # Domain name of the site
FEED_DOMAIN = SITEURL  # Domain name to use in feeds
HTTPS = True  # Use HTTPS for the site

# Robots configuration
ROBOTS = "index, follow"  # Instructions for search engine robots

# Styling and layout settings
BROWSER_COLOR = "#333333"  # Color scheme for the browser tab
PYGMENTS_STYLE = "github-dark"  # Syntax highlighting theme
THEME_COLOR = 'dark'  # Theme color (can be overridden by users)

# Path to content files
PATH = "content"

# Timezone and localization settings
TIMEZONE = 'America/Toronto'  # Timezone for the site

# Default language and feed settings
DEFAULT_LANG = 'en'  # Default language of the site

# Social media links and other metadata
GITHUB_URL = "https://github.com/phillip-bruno"  # GitHub URL

DEFAULT_PAGINATION = 5  # Default number of items per page

# Theme settings
THEME = 'Flex'  # Theme to use (Flex, default)

# Social media links
SOCIAL = (
    ("envelope", 'mailto:phillip.bruno@outlook.com'),  # Email address
    ("github", "https://github.com/phillip-bruno"),  # GitHub link
    ("linkedin", "https://www.linkedin.com/in/phillip-b-39b3884a")  # LinkedIn link
)

# License information
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",  # License identifier (e.g., by-sa, cc-by-nd)
    "icon": True,  # Display license icon
    "language": "en_US"  # Language of the license text
}

# Copyright information and date
COPYRIGHT_YEAR = datetime.now().year

