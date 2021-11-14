import streamlit as stream_lit

from view.view_serializer import ViewSerializer

ROOT_PATH = "https://thegraph.com/hosted-service/subgraph/aavegotchi/aavegotchi-core-matic?Aavegotchi?id:1!"

stream_lit.set_page_config(page_title="Aavegotchi", page_icon="money", layout='wide', initial_sidebar_state='auto')

option = stream_lit.sidebar.selectbox('Home',
                                      ['HOME', 'Districts Visualizer', 'Floor Sniper', 'Price Estimator',
                                       'Neighbour Parcels',
                                       'Bazaar Stats'])

view_serializer = ViewSerializer(stream_lit)

if option == 'HOME':
    view_serializer.render_home()

if option == 'Districts Visualizer':
    view_serializer.render_district_visualizer()

if option == 'Floor Sniper':
    view_serializer.render_floor_sniper()

if option == 'Price Estimator':
    view_serializer.render_price_estimator()

if option == 'Neighbour Parcels':
    view_serializer.render_neighbour_parcels()

if option == 'Bazaar Stats':
    view_serializer.render_bazaar_stats()
