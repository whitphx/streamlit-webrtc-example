# streamlit-webrtc-example

Hosted on Streamlit Cloud: [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/whitphx/streamlit-webrtc-example/main/app.py) https://share.streamlit.io/whitphx/streamlit-webrtc-example/main/app.py 

Hosted on Heroku: https://streamlit-webrtc-example.herokuapp.com/

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D2ERWFG)

<a href="https://www.buymeacoffee.com/whitphx" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="180" height="50" ></a>

[![GitHub Sponsors](https://img.shields.io/github/sponsors/whitphx?label=Sponsor%20me%20on%20GitHub%20Sponsors&style=social)](https://github.com/sponsors/whitphx)

## Deployment notes

The deployment to Heroku is automated with GitHub actions: [./.github/workflows/heroku.yml](./.github/workflows/heroku.yml).

[Streamlit Cloud](https://streamlit.io/cloud) automatically triggers the deployment on its CI/CD.

## Manual deployment to heroku
### Prerequisites
1. Set up `heroku` command.

2. Add [`heroku-buildpack-apt`](https://github.com/heroku/heroku-buildpack-apt) to buildpacks.
   ```shell
   $ heroku buildpacks:add --index 1 heroku-community/apt
   ```

   See
   https://help.heroku.com/IYRYW6VB/how-do-i-install-additional-software-packages-that-my-application-requires
   and
   https://github.com/heroku/heroku-buildpack-apt
   for details.

### Deploy
#### If dependencies have changed, update `requirements.txt`
1. Update `requirements.txt`.
   ```shell
   $ make deps/update
   ```

2. Commit it.
   ```shell
   $ git add requirements.txt
   $ git commit -m "requirements.txt"
   ```
#### Deploy the current branch to Heroku
```shell
$ git push heroku <current-branch>:main
```
