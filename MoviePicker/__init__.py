import pandas as pd
from flask import (Flask, flash, redirect, render_template,
                   request, session, abort, url_for)

app = Flask(__name__)


@app.route("/")
def show_tables():
    df = pd.read_excel('/static/TopFilmsList.xlsx')
    #datatable = df.to_html()
    RandomSelection = df.sample(n=1)
    Title = RandomSelection['Title'].values[0]
    Critics = RandomSelection['Critics'].values[0]
    Audience= RandomSelection['Audience'].values[0]
    Screenshot= RandomSelection['Links'].values[0]
    Urllink= RandomSelection['RT'].values[0]
    #Selection = RandomSelection['Title'].values[0] #.to_html()
    return render_template('table.html', 
                            Title = Title,
                            Critics = Critics, 
                            Audience = Audience,
                            Screenshot = Screenshot,
                            Urllink = Urllink)

                            
if __name__ == "__main__":
    app.run()