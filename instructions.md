1) Install Pelican: `python -m pip install "pelican[markdown]"`
2) Clone this repository into the */source/* folder.
3) Clone the Flex theme using the instructions from [pelican-themes](https://github.com/alexandrevicenzi/flex) into the */themes/* folder.
4) Run Pelican command: `pelican /path/to/your/resume_website/source/content -s /path/to/your/resume_website/source/pelicanconf.py
`
    - Optionally: run `pelican --listen` or `pelican --autoreload --listen` to view changes locally first
5) Commit and push changed files to git repository.