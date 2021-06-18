# Self Deployed Markdown Slides

By using Github Actions and Marp, the markdown slides can be deployed on github gapes automatically.

## How to

1. Create a folder in the root directory. Write down your slides in Markdown.
2. Push you source `.md` on Github. And open the github pages service in Settings.
3. The Github Action will be trigged by `push`. It will do the following things:
   - Setup Node
   - Install Marp
   - Setup Python
   - Run `md2html.py`
   - Deploy the generated website on the `gh-pages` branch

## Example

See the [Website](zybbigpy.github.io/pre) automatically generated.
