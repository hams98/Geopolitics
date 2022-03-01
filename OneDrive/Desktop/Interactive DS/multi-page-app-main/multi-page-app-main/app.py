import streamlit as st
from multiapp import MultiApp
from apps import japan, somalia # import your app modules here

app = MultiApp()



# Add all your application here
app.add_app("Japan", japan.app)
app.add_app("Somalia", somalia.app)

# The main app
app.run()
