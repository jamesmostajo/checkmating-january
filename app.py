import streamlit as st
import getPieGameResults, getEloHistogram, getHeatmap, getPieceTakes, getCheckmateDistribution, getGamesNum
from Cleaning.Openings import openings

def show_histogram(timeControl, opening):
    import plotly.express as px
    st.subheader("How many Games are played by Game Elo?")
    st.write("A histogram showing the distribution of games played depending on the game’s elo rating.")
    data = getEloHistogram.getHistogramData(timeControl, opening)
    custom_colors = ['#125D63']
    fig = px.histogram(
        x=data['elo_ranges'], 
        y=data['values'], 
        nbins=len(data['elo_ranges']),
        color_discrete_sequence=custom_colors
    )
    
    fig.update_layout(
        margin=dict(t=0, b=0),
        xaxis_title='Elo Rating',
        yaxis_title='Number of Games',
    )
    st.plotly_chart(fig, theme="streamlit")

def show_checkmate_heatmap(start_elo, end_elo, timeControl, opening):
    import plotly.express as px
    
    st.subheader("Where do Pieces move to Checkmate?")
    st.write("A heatmap displaying any given chess pieces’ most common position on the board whenever they get a checkmate.")
    col1, col2, col3 = st.columns(3)

    with col1:
        filter_piece = st.selectbox(
                "Select piece",
                ("Select All", "Pawn", "Knight", "Bishop", "Rook", "Queen", "King")
        )
    with col2:
        filter_winner = st.selectbox(
                "Select winning side",
                ("Select Both", "Black", "White")
        )
        
    data = getHeatmap.getHeatmapData(filter_piece, start_elo, end_elo, filter_winner, timeControl, opening)

    fig = px.imshow(data,
                    labels=dict(color="# of checkmates"),
                    x=list("abcdefgh"),
                    y=list("87654321"),
                    color_continuous_scale = "mint"
                   )

    fig.update_layout(margin=dict(t=0, b=0), height=600, yaxis=dict(type='category'))


    st.plotly_chart(fig, theme="streamlit")

def show_game_results(start_elo, end_elo, timeControl, opening):
    import plotly.graph_objects as go

    st.subheader("How frequent do Checkmates occur?")
    st.write("A pie chart showing the comparison of how Chess games conclude between checkmates, draws, and other circumstances.")

    labels = ["Draw", "Checkmate", "Abandoned", "Resigned", "Time Forfeit"]
    values = getPieGameResults.getPieGameresults(start_elo, end_elo, timeControl, opening)
    if sum(values) == 0 :
        st.write("There are no games with the given categories")
        return

    custom_colors = ['#330036', '#A3001E', '#125D63', '#0D7296', '#F5B841', '#EC6F9B']
    hover_text = [
        "",
        "",
        "Resignations, time forfeit, and other game results"
    ]

    fig = go.Figure(
        data=[go.Pie(
                labels=labels, values=values, 
                marker=dict(colors=custom_colors),
                hoverinfo='label+percent+text',
                hovertext=hover_text
            )
        ]
    )

    fig.update_layout(margin=dict(t=0, b=0))

    st.plotly_chart(fig, theme="streamlit")

def show_piece_takes(start_elo, end_elo, timeControl, opening):
    import plotly.graph_objects as go

    st.subheader("How many captures does each Piece make?")
    st.write("A bar graph depicting which piece has the highest number of takes among the others.")

    is_divided = st.toggle("Divide by number of type of piece")

    x = ['Pawn', 'Rook', 'Knight', 'Bishop', 'Queen', 'King']
    y = getPieceTakes.getPieceTakesData(start_elo, end_elo, timeControl, opening)

    if is_divided:
        div = [16, 4, 4, 4, 2, 2]
        y = [y[i]//div[i] for i in range(6)]

    y_text = [f'{val:,}' for val in y]

    # Use textposition='auto' for direct text
    fig = go.Figure(data=[go.Bar(
                x=x, y=y,
                text=y_text,
                textposition='auto',
                marker=dict(color='#125D63')
            )])

    fig.update_layout(margin=dict(t=0, b=0))

    st.plotly_chart(fig, theme="streamlit")

def show_checkmate_graph(start_elo, end_elo, timeControl, opening):
    import plotly.express as px
    data = getCheckmateDistribution.getCheckmateData(start_elo, end_elo, timeControl, opening)

    st.subheader("What Piece is used the most to Checkmate?")
    st.write("A pie chart illustrating which piece is being used the most in order to get a checkmate.")
    if data == -1 :
        st.write("There are no checkmates within the given categories")
        return

    custom_colors = ['#330036', '#A3001E', '#125D63', '#0D7296', '#F5B841', '#EC6F9B']
    
    fig = px.pie(names=data['piece'], values = data['pieceCount'], color_discrete_sequence=custom_colors)

    fig.update_layout(margin=dict(t=0, b=0))
    st.plotly_chart(fig, theme="streamlit")

def show_big_number(start_elo, end_elo):
    game_num = getGamesNum.getGamesNum(start_elo, end_elo)
    st.metric("Number of games being analyzed", game_num)

def main():
    st.set_page_config(
        page_title="Chess Visualizations", 
        page_icon=":chess_pawn:",
        layout="wide",
        menu_items={
            'About': "This app is made for a Data Visualization class in Ateneo de Manila University."
        }
    )

    st.title("January 2023 Lichess Visualizations :chess_pawn:")
    st.caption("By Bryan Francisco, James Mostajo, and Robin Vicente")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        start_elo, end_elo = st.select_slider(
            "Select range of game elo rating",
            options=range(2400, 3001),
            value=(2400, 3000)
        )
    with col2:
        timeControl = st.selectbox(
            "Select time control",
            ("All", "Blitz", "Rapid", "Classical")
        )
    with col3:
        opening = st.selectbox(
            "Select opening",
            openings
        )
    
    # show_big_number(start_elo, end_elo)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Games Played?",
        "Move to Checkmate?",
        "Piece Captures?",
        "Results Frequency?",
        "Piece to Checkmate?",
    ])

    with tab1:
        show_histogram(timeControl, opening)
    with tab2:
        show_checkmate_heatmap(start_elo, end_elo, timeControl, opening)  
    with tab3:
        show_piece_takes(start_elo, end_elo, timeControl, opening)
        pass
    with tab4:
        show_game_results(start_elo, end_elo, timeControl, opening)
        pass
    with tab5:
        show_checkmate_graph(start_elo, end_elo, timeControl, opening)


if __name__ == '__main__':
    main()
