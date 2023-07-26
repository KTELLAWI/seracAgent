# import speedtest
import pyshorteners as short
from pystyle import *
import streamlit as st

# from speedtest import Speedtest


# ste = speedtest.Speedtest()
# download_speed = st.download()

# print(f"Download speed: {download_speed / 1024 / 1024:.2f} Mbps")

st.title('Digistacks Links Shortners')
st.subheader("get the shorntr form of link ")
title = st.text_input(label='Write your Line Below',)
if title == "":
    st.error("fff",icon=None)
# url= Write.Input("write your url : ",Colors.blue_to_green,interval=0.2)
sh= short.Shortener()
if st.button('get the short link'):
    with st.spinner("under processing "):
        short=sh.tinyurl.short(title)
        st.error("body",  icon=None)
        st.success("done")
        st.write("the shor link is :", short)

          
  

# Write.Print(sh.tinyurl.short(url),Colors.green,interval=0.3)
input('\npress any key ')

