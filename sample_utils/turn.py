import logging
import os

import requests
import streamlit as st

logger = logging.getLogger(__name__)


OPEN_RELAY_API_HOST = os.environ.get("OPEN_RELAY_API_HOST")
OPEN_RELAY_API_KEY = os.environ.get("OPEN_RELAY_API_KEY")


@st.cache_data
def get_ice_servers():
    if not OPEN_RELAY_API_HOST or not OPEN_RELAY_API_KEY:
        logger.warning(
            "Open Relay API host or key is not set. Fallback to a free STUN server from Google."  # noqa: E501
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    # Get response from Open Relay API
    response = requests.get(
        f"https://{OPEN_RELAY_API_HOST}/api/v1/turn/credentials?apiKey={OPEN_RELAY_API_KEY}"  # noqa: E501
    )
    return response.json()
