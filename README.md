# streamlit-webrtc-example

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/whitphx/streamlit-webrtc-example/main/app.py)

Sample page hosted on Heroku: https://streamlit-webrtc-example.herokuapp.com/

The Deployment is automated with GitHub actions: [./.github/workflows/heroku.yml](./.github/workflows/heroku.yml)

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
