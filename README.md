# Self Deployed Markdown Slides

By using [Github Actions](https://github.com/features/actions) and [Marp](https://marp.app/), the markdown slides can be deployed on [Github Pages](https://pages.github.com/) automatically.

## How to

1. Create a folder in the root directory. Write down your slides in Markdown.
2. Push you source `.md` file on Github. Open the github pages service in Settings.
3. The Github Action will be trigged by `push`. It will do the following things:
   - Setup Node environment
   - Install Marp
   - Setup Python environment
   - Run `md2html.py`
   - Deploy the generated website on the `gh-pages` branch

## Example

See the [Website](https://zybbigpy.github.io/pre) automatically generated.
