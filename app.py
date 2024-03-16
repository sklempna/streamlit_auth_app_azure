import streamlit as st
from flask import Request
from streamlit.server.server import Server

st.title("Welcome to the app")


def get_user_details():
    # The current server object
    ctx = Server.get_current()._get_app()
    # The Flask request object
    request: Request = ctx.request_context.request

    # Get the user details from the headers
    user_email = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
    return user_email


user_email = get_user_details()

if user_email:
    st.write(f"Welcome {user_email}")
else:
    st.error("User not authenticated.")
